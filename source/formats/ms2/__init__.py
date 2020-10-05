import os
import itertools
import struct
import io
import time

from generated.formats.ms2.compound.Ms2InfoHeader import Ms2InfoHeader
from generated.formats.ms2.compound.Mdl2InfoHeader import Mdl2InfoHeader
from generated.formats.ms2.compound.Ms2BoneInfo import Ms2BoneInfo
from generated.formats.ms2.compound.PcModel import PcModel
from generated.formats.ms2.compound.PcBuffer1 import PcBuffer1
from generated.io import IoFile, BinaryStream


def findall(p, s):
	'''Yields all the positions of
	the pattern p in the string s.'''
	i = s.find(p)
	while i != -1:
		yield i
		i = s.find(p, i+1)


class Ms2File(Ms2InfoHeader, IoFile):

	def __init__(self, ):
		super().__init__()

	def is_pc(self):
		return self.general_info.ms_2_version == 32

	def load(self, filepath, mdl2, quick=False, map_bytes=False):
		start_time = time.time()
		# eof = super().load(filepath)

		# extra stuff
		self.bone_names = []
		self.bone_info = None
		with self.reader(filepath) as stream:
			self.read(stream)
			self.eoh = stream.tell()
			print("end of header: ", self.eoh)
			if self.is_pc():
				self.pc_buffer1 = stream.read_type(PcBuffer1, (self.general_info,))
				# this is for the PC format
				for mdl2_info in self.pc_buffer1.model_infos:
					mdl2_info.pc_model = stream.read_type(PcModel, (mdl2_info,))
					print(mdl2_info.pc_model)

					break
			else:
				# first get all bytes of the whole bone infos block
				self.bone_info_bytes = stream.read(self.bone_info_size)
				# find the start of each using this identifier
				zero_f = bytes.fromhex("00 00 00 00")
				one_f = bytes.fromhex("00 00 80 3F")
				# lion has a 1 instead of a 4
				bone_info_marker_1 = bytes.fromhex("FF FF 00 00 00 00 00 00 01")
				# this alone is not picky enough for mod_f_wl_unq_laboratory_corner_002_dst
				bone_info_marker_4 = bytes.fromhex("FF FF 00 00 00 00 00 00 04")
				# there's 8 bytes before this
				bone_info_starts = []
				for a, b in ((zero_f, bone_info_marker_1),
							 (one_f, bone_info_marker_1),
							 (zero_f, bone_info_marker_4),
							 (one_f, bone_info_marker_4),
							 ):
					bone_info_starts.extend(x - 4 for x in findall(a + b, self.bone_info_bytes))

				bone_info_starts = list(sorted(bone_info_starts))
				print("bone_info_starts", bone_info_starts)

				if bone_info_starts:
					idx = mdl2.index
					if idx >= len(bone_info_starts):
						print("reset boneinfo index")
						idx = 0
					bone_info_address = self.eoh + bone_info_starts[idx]
					print("using bone info {} at address {}".format(idx, bone_info_address))
					stream.seek(bone_info_address)
					try:
						self.bone_info = Ms2BoneInfo()
						self.bone_info.read(stream)
						print(self.bone_info)
						print("end of bone info at", stream.tell())
						self.bone_names = [self.names[i] for i in self.bone_info.name_indices]
					except:
						print("Bone info failed")

				else:
					print("No bone info found")

		# numpy chokes on bytes io objects
		with open(filepath, "rb") as stream:
			stream.seek(self.eoh + self.bone_info_size)
			# get the starting position of buffer #2, vertex & face array
			self.start_buffer2 = stream.tell()
			if self.general_info.ms_2_version == 32:
				print("PC model...")
				mdl2.models = []
				if not quick:
					base = 512
					for model in self.pc_buffer1.model_infos:
						for model_data in model.pc_model.model_data:
							model_data.populate(self, stream, self.start_buffer2, self.bone_names, base)

							model_data.material = "test"
							mdl2.models.append(model_data)
						break
			else:
				print("vert array start", self.start_buffer2)
				print("tri array start", self.start_buffer2 + self.buffer_info.vertexdatasize)

				if not quick:
					base = mdl2.model_info.pack_offset
					for model in mdl2.models:
						model.populate(self, stream, self.start_buffer2, self.bone_names, base)

				if map_bytes:
					for model in mdl2.models:
						model.read_bytes_map(self.start_buffer2, stream)
					return

	def save(self, filepath, mdl2):
		print("Writing verts and tris to temporary buffer")
		# write each model's vert & tri block to a temporary buffer
		temp_vert_writer = io.BytesIO()
		temp_tris_writer = io.BytesIO()
		vert_offset = 0
		tris_offset = 0

		with BinaryStream() as temp_bone_writer:
			temp_bone_writer.version = self.version
			temp_bone_writer.user_version = self.user_version
			temp_bone_writer.ms_2_version = self.general_info.ms_2_version
			self.bone_info.write(temp_bone_writer)
			bone_bytes = temp_bone_writer.getvalue()
			print("new bone info length: ", len(bone_bytes))

		for i, model in enumerate(mdl2.models):
			model.write_verts(temp_vert_writer)
			model.write_tris(temp_tris_writer)
			print("vert_offset", vert_offset)
			print("tris_offset", tris_offset)

			# update ModelData struct
			model.vertex_offset = vert_offset
			model.tri_offset = tris_offset
			model.vertex_count = len(model.verts)
			model.tri_index_count = len(model.tri_indices)

			# offsets for the next model
			vert_offset = temp_vert_writer.tell()
			tris_offset = temp_tris_writer.tell()

		# update lod fragment
		print("update lod fragment")
		for lod in mdl2.lods:
			# print(lod)
			lod_models = tuple(
				model for model in mdl2.models[lod.first_model_index:lod.last_model_index])
			# print(lod_models)
			lod.vertex_count = sum(model.vertex_count for model in lod_models)
			lod.tri_index_count = sum(model.tri_index_count for model in lod_models)
			print("lod.vertex_count", lod.vertex_count)
			print("lod.tri_index_count", lod.tri_index_count)
		print("Writing final output")
		# get original header and buffers 0 & 1
		# first get all bytes of the whole bone infos block
		print("old bone info length: ", len(self.bone_info_bytes))
		cut = len(bone_bytes) - len(self.bone_info_bytes)

		# get bytes from IO object
		vert_bytes = temp_vert_writer.getvalue()
		tris_bytes = temp_tris_writer.getvalue()
		# modify buffer size
		self.buffer_info.vertexdatasize = len(vert_bytes)
		self.buffer_info.facesdatasize = len(tris_bytes)
	
		# write output ms2
		with self.writer(filepath) as f:
			self.write(f)
			f.write(bone_bytes)
			if cut != 0:
				f.write(self.bone_info_bytes[cut:])
			f.write(vert_bytes)
			f.write(tris_bytes)
	

class Mdl2File(Mdl2InfoHeader, IoFile):

	def __init__(self, ):
		super().__init__()

	def load(self, filepath, quick=False):

		self.file = filepath
		self.dir, self.basename = os.path.split(filepath)
		self.file_no_ext = os.path.splitext(self.file)[0]
		start_time = time.time()
		# eof = super().load(filepath)

		# read the file
		with self.reader(filepath) as stream:
			self.read(stream)
		# print(self)

		self.ms2_path = os.path.join(self.dir, self.name)
		self.ms2_file = Ms2File()
		self.ms2_file.load(self.ms2_path, self, quick=quick)

		# set material links
		for mat_1 in self.materials_1:
			try:
				name = self.ms2_file.names[mat_1.material_index]
				model = self.models[mat_1.model_index]
				model.material = name
			except:
				print(f"Couldn't match material {mat_1.material_index} to model {mat_1.model_index} - bug?")
		# todo - doesn't seem to be correct, at least not for JWE dinos
		self.lod_names = [self.ms2_file.names[lod.strznameidx] for lod in self.lods]
		print("lod_names", self.lod_names)
		print(f"Finished reading in {time.time() - start_time:.2f} seconds!")

	def save(self, filepath):
		exp = "export"
		exp_dir = os.path.join(self.dir, exp)
		os.makedirs(exp_dir, exist_ok=True)

		mdl2_name = os.path.basename(filepath)

		# create name of output ms2
		new_ms2_name = mdl2_name.rsplit(".", 1)[0] + ".ms2"
		ms2_path = os.path.join(exp_dir, new_ms2_name)
		self.ms2_file.save(ms2_path, self)
		# set new ms2 name to mdl2 header
		self.name = new_ms2_name

		# write final mdl2
		mdl2_path = os.path.join(exp_dir, mdl2_name)
		with self.writer(mdl2_path) as stream:
			self.write(stream)


if __name__ == "__main__":
	m = Mdl2File()
	m.load("C:/Users/arnfi/Desktop/prim/models.ms2")
	print(m)
