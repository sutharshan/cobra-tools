# START_GLOBALS
import logging
import math
import numpy as np
from generated.formats.ms2.compound.packing_utils import *
from plugin.utils.tristrip import triangulate
# END_GLOBALS


class ZtMeshData:

	# START_CLASS

	def init_arrays(self):
		self.vertices = np.empty((self.vertex_count, 3), np.float32)
		self.normals = np.empty((self.vertex_count, 3), np.float32)
		self.tangents = np.empty((self.vertex_count, 3), np.float32)
		try:
			uv_shape = self.dt_colors["uvs"].shape
			self.uvs = np.empty((self.vertex_count, *uv_shape), np.float32)
		except:
			self.uvs = None
		try:
			colors_shape = self.dt_colors["colors"].shape
			self.colors = np.empty((self.vertex_count, *colors_shape), np.float32)
		except:
			self.colors = None
		self.weights_info = {}

	def update_dtype(self):
		"""Update MeshData.dt (numpy dtype) according to MeshData.flag"""
		# basic shared stuff
		dt = [
			("bone ids", np.ubyte, (4,)),
			("bone weights", np.ubyte, (4,)),
			("pos", np.float16, (3,)),
			("one", np.float16),
			("normal", np.ubyte, (3,)),
			("winding", np.ubyte, ),
			("tangent", np.ubyte, (3,)),
			("bone index", np.ubyte, ),
		]
		vert_count_in_stream = self.sum_uv_dict[self.stream_index]
		# hack for zt monitor
		if self.buffer_info.uvs_size // vert_count_in_stream == 4:
			dt_colors = [
				("uvs", np.ushort, (1, 2)),
			]
		else:
			dt_colors = [
				("colors", np.ubyte, (1, 4)),
				("uvs", np.ushort, (1 + self.some_index, 2)),
			]
		self.dt = np.dtype(dt)
		self.dt_colors = np.dtype(dt_colors)
		self.update_shell_count()

	def read_verts(self):
		logging.debug(f"Tri info address {self.tri_info_offset}")
		logging.debug(f"Vertex info address {self.vert_info_offset}")
		# get dtype according to which the vertices are packed
		self.update_dtype()
		# create arrays for the unpacked ms2_file
		self.init_arrays()
		# read a vertices of this mesh
		if 4294967295 == self.vertex_offset:
			logging.warning(f"vertex_offset is -1")
			# return
			if self.last_vertex_offset == 0:
				logging.warning(f"Zero, starting at buffer start {self.buffer_info.verts.tell()}")
			else:
				self.buffer_info.verts.seek(self.last_vertex_offset)
		else:
			self.buffer_info.verts.seek(self.vertex_offset)
		self.start_of_vertices = self.buffer_info.verts.tell()
		# logging.debug(f"{self.vertex_count} VERTS at {self.buffer_info.verts.tell()}")
		self.verts_data = np.empty(dtype=self.dt, shape=self.vertex_count)
		self.buffer_info.verts.readinto(self.verts_data)
		self.end_of_vertices = self.buffer_info.verts.tell()
		size = self.end_of_vertices - self.start_of_vertices
		logging.info(
			f"{self.vertex_count} vertices from {self.start_of_vertices:5} to {self.end_of_vertices:5} "
			f"in stream {self.get_stream_index()}, size {size:5}")
		# print(self.verts_data.shape)
		self.buffer_info.uvs.seek(self.uv_offset)
		# logging.debug(f"UV at {self.buffer_info.uvs.tell()}")
		self.colors_data = np.empty(dtype=self.dt_colors, shape=self.vertex_count)
		self.buffer_info.uvs.readinto(self.colors_data)
		# first cast to the float uvs array so unpacking doesn't use int division
		if self.colors is not None:
			# first cast to the float colors array so unpacking doesn't use int division
			self.colors[:] = self.colors_data["colors"]
			self.colors /= 255
		if self.uvs is not None:
			self.uvs[:] = self.colors_data["uvs"]
			self.uvs /= 2048
		# logging.debug(self.normals.shape)
		self.normals[:] = self.verts_data["normal"]
		self.tangents[:] = self.verts_data["tangent"]
		self.vertices[:] = self.verts_data["pos"]
		unpack_ubyte_vector(self.normals)
		unpack_ubyte_vector(self.tangents)
		unpack_swizzle_vectorized(self.vertices)
		unpack_swizzle_vectorized_b(self.normals)
		unpack_swizzle_vectorized(self.tangents)

		# if "bone weights" in self.dt.fields:
		bone_weights = self.verts_data["bone weights"].astype(np.float32) / 255
		self.get_blended_weights(self.verts_data["bone ids"], bone_weights)
		# self.get_static_weights(self.verts_data["bone index"], self.use_blended_weights)

