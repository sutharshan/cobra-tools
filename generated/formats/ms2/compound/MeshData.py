
import logging
import math
import numpy as np
from plugin.utils.tristrip import triangulate

FUR_OVERHEAD = 2


from source.formats.base.basic import fmt_member
import generated.formats.ms2.compound.BufferInfo
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class MeshData(MemStruct):

	"""
	used for shared functions
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# index into streamed buffers
		self.stream_index = 0

		# increments somewhat in ZTUAC platypus, apparently unused from JWE1 onward
		self.some_index = 0

		# PZ and JWE have a ptr at the start instead of the stream index
		self.buffer_info = Pointer(self.context, 0, generated.formats.ms2.compound.BufferInfo.BufferInfo)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		if self.context.version <= 32:
			self.stream_index = 0
		self.some_index = 0
		if self.context.version >= 47:
			self.buffer_info = Pointer(self.context, 0, generated.formats.ms2.compound.BufferInfo.BufferInfo)

	def read(self, stream):
		self.io_start = stream.tell()
		self.read_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		self.write_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		if instance.context.version <= 32:
			instance.stream_index = stream.read_uint64()
		if instance.context.version >= 47:
			instance.buffer_info = Pointer.from_stream(stream, instance.context, 0, generated.formats.ms2.compound.BufferInfo.BufferInfo)
		instance.some_index = stream.read_uint64()
		instance.buffer_info.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		if instance.context.version <= 32:
			stream.write_uint64(instance.stream_index)
		if instance.context.version >= 47:
			Pointer.to_stream(stream, instance.buffer_info)
		stream.write_uint64(instance.some_index)

	@classmethod
	def from_stream(cls, stream, context, arg=0, template=None):
		instance = cls(context, arg, template, set_default=False)
		instance.io_start = stream.tell()
		cls.read_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	@classmethod
	def to_stream(cls, stream, instance):
		instance.io_start = stream.tell()
		cls.write_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	def get_info_str(self, indent=0):
		return f'MeshData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* stream_index = {fmt_member(self.stream_index, indent+1)}'
		s += f'\n	* buffer_info = {fmt_member(self.buffer_info, indent+1)}'
		s += f'\n	* some_index = {fmt_member(self.some_index, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s

	# def read_bytes(self, buffer_2_offset, vertex_data_size, stream):
	# 	"""Used to store raw binary vertex and tri data on the mesh, for merging"""
	# 	# print("reading binary mesh data")
	# 	# read a vertices of this mesh
	# 	stream.seek(buffer_2_offset + self.vertex_offset)
	# 	self.verts_bytes = stream.read(self.size_of_vertex * self.vertex_count)
	# 	stream.seek(buffer_2_offset + vertex_data_size + self.tri_offset)
	# 	self.tris_bytes = stream.read(2 * self.tri_index_count)
	#
	# def read_bytes_map(self, buffer_2_offset, stream):
	# 	"""Used to document byte usage of different vertex formats"""
	# 	# read a vertices of this mesh
	# 	stream.seek(buffer_2_offset + self.vertex_offset)
	# 	# read the packed ms2_array
	# 	ms2_array = np.fromfile(stream, dtype=np.ubyte, count=self.size_of_vertex * self.vertex_count)
	# 	ms2_array = ms2_array.reshape((self.vertex_count, self.size_of_vertex))
	# 	self.bytes_max = np.max(ms2_array, axis=0)
	# 	self.bytes_min = np.min(ms2_array, axis=0)
	# 	self.bytes_mean = np.mean(ms2_array, axis=0)
	# 	if self.size_of_vertex != 48:
	# 		raise AttributeError(f"size_of_vertex != 48: size_of_vertex {self.size_of_vertex}, flag {self.flag}", )
	
	@property
	def _stream_index(self):
		logging.debug(f"Using stream {self.stream_index}")
		return self.stream_index

	def populate(self, ms2_file, base=512, last_vertex_offset=0, sum_uv_dict={}):
		self.sum_uv_dict = sum_uv_dict
		self.last_vertex_offset = last_vertex_offset
		self.new_vertex_offset = 0
		self.stream = ms2_file.streams[self._stream_index]
		self.stream_info = ms2_file.buffer_infos[self._stream_index]
		logging.debug(f"Tri info address {self.tri_info_offset}")
		logging.debug(f"Vertex info address {self.vert_info_offset}")
		# print(self)
		self.base = base
		self.shapekeys = None
		self.read_verts()
		self.read_tris()
		# self.validate_tris()
		return self.new_vertex_offset
	
	def write_verts(self, stream):
		stream.write(self.verts_data.tobytes())

	@property
	def tris_address(self):
		return self.stream_info.vertex_buffer_size + self.tri_offset

	def read_tris(self):
		# read all tri indices for this mesh, but only as many as needed if there are shells
		self.stream.seek(self.tris_address)
		index_count = self.tri_index_count // self.shell_count
		logging.debug(f"Reading {index_count} indices at {self.stream.tell()}")
		self.tri_indices = np.empty(dtype=np.uint16, shape=index_count)
		self.stream.readinto(self.tri_indices)
		# check if there's no empty value left in the array
		# if len(self.tri_indices) != index_count:
		# 	raise BufferError(f"{len(self.tri_indices)} were read into tri index buffer, should have {index_count}")

	def write_tris(self, stream):
		tri_bytes = self.tri_indices.tobytes()
		# extend tri array according to shell count
		logging.debug(f"Writing {self.shell_count} shells of {len(self.tri_indices)} triangles")
		for shell in range(self.shell_count):
			stream.write(tri_bytes)

	@property
	def lod_index(self, ):
		try:
			lod_i = int(math.log2(self.poweroftwo))
		except:
			lod_i = 0
			logging.warning(f"math domain for lod {self.poweroftwo}")
		return lod_i

	@lod_index.setter
	def lod_index(self, lod_i):
		self.poweroftwo = int(math.pow(2, lod_i))

	def update_shell_count(self):
		# 853 in aardvark is a shell mesh, but has no tri shells
		if self.flag.repeat_tris:
			self.shell_count = 6
		else:
			self.shell_count = 1

	@property
	def tris(self, ):
		if hasattr(self.flag, "stripify") and self.flag.stripify:
			return triangulate((self.tri_indices,))
		else:
			# todo - DLA stripify field is different
			try:
				# create non-overlapping tris from flattened tri indices
				tris_raw = np.reshape(self.tri_indices, (len(self.tri_indices)//3, 3))
				# reverse each tri to account for the flipped normals from mirroring in blender
				return np.flip(tris_raw, axis=-1)
			except:
				return triangulate((self.tri_indices,))

	@tris.setter
	def tris(self, b_tris):
		# cast to uint16
		raw_tris = np.array(b_tris, dtype=np.uint16)
		# reverse tris
		raw_tris = np.flip(raw_tris, axis=-1)
		# flatten array
		self.tri_indices = np.reshape(raw_tris, len(raw_tris)*3)

	def validate_tris(self):
		"""See if all tri indices point into the vertex buffer, raise an error if they don't"""
		# this is fairly costly (10 % of total loading time), so don't do it by default
		# max_ind = np.max(self.tri_indices)
		# if max_ind >= len(self.verts_data):
		for max_ind in self.tri_indices:
			if max_ind >= len(self.verts_data):
				raise IndexError(f"Tri index {max_ind} does not point into {len(self.verts_data)} vertices")
		logging.debug("All tri indices are valid")

