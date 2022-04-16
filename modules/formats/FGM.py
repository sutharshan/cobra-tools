import logging
import struct

from generated.formats.fgm.compound.FgmHeader import FgmHeader
from generated.formats.ovl_base.versions import is_ztuac
from modules.formats.BaseFormat import MemStructLoader
from modules.formats.shared import get_versions, get_padding
from modules.helpers import as_bytes, zstr
from generated.formats.fgm import FgmFile


class FgmLoader(MemStructLoader):
	target_class = FgmHeader

	def create(self):
		fgm_data = self._get_data(self.file_entry.path)
		# first create dependencies
		for tex_name in fgm_data.texture_files:
			self.create_dependency(f"{tex_name}.tex")
		datas, sizedstr_bytes = self._get_frag_datas(fgm_data)
		# now check for frags
		self.header = fgm_data.fgm_info
		frag_count = self._get_frag_count()
		# JWE2 patternset fgms seem to be in pool type 3, everything else in 2

		self.sized_str_entry = self.create_ss_entry(self.file_entry)
		self.write_to_pool(self.sized_str_entry.pointers[0], 2, sizedstr_bytes)
		self.create_data_entry(self.sized_str_entry, (fgm_data.buffer_bytes,))
		self.create_fragments(self.sized_str_entry, frag_count)
		self._tag_fragments()

		# self.tex_info, self.attr_info, self.dependencies_ptr, self.data_lib
		offsets = []
		if self.header.attribute_count:
			offsets.append(24)
			offsets.append(40)
		if self.header.texture_count:
			offsets.append(16)
		if self.file_entry.dependencies:
			offsets.append(32)
		for frag, rel_offset in zip(self.sized_str_entry.fragments, sorted(offsets)):
			self.ptr_relative(frag.pointers[0], self.sized_str_entry.pointers[0], rel_offset)

		# write the actual data
		for frag, data in zip(self._valid_frags(), datas):
			self.write_to_pool(frag.pointers[1], 2, data)

		if fgm_data.texture_files:
			for dependency in self.file_entry.dependencies:
				self.write_to_pool(dependency.pointers[0], 2, b"\x00" * 8)
			# points to the start of the dependencies region
			self.ptr_relative(self.dependencies_ptr.pointers[1], self.file_entry.dependencies[0].pointers[0])

	def collect(self):
		super().collect()
		# print(self.header)
		self._tag_fragments()
		if self.tex_info:
			# size of a texture info varies
			if is_ztuac(self.ovl):
				tex_size = self.header.texture_count * 12
			else:
				tex_size = self.header.texture_count * 24
			ptr = self.tex_info.pointers[1]
			ptr.split_data_padding(tex_size)
			logging.debug(f"Texture data {len(ptr.data)} padding {len(ptr.padding)}")
		if self.attr_info:
			# this likely has no padding anyway
			ptr = self.attr_info.pointers[1]
			ptr.split_data_padding(self.header.attribute_count * 16)
			logging.debug(f"Attribute data {len(ptr.data)} padding {len(ptr.padding)}")
		# for i, f in enumerate(self.sized_str_entry.fragments):
		# 	p = f.pointers[1]
		# 	logging.debug(f"{self.sized_str_entry.name} {i} {len(p.data)} {len(p.padding)}")

	def _tag_fragments(self):
		self.tex_info = self.header.textures.frag
		self.attr_info = self.header.attributes.frag
		self.dependencies_ptr = self.header.dependencies.frag
		self.data_lib = self.header.data_lib.frag

	def _get_frag_count(self):
		frag_count = 0
		if self.header.texture_count:
			frag_count += 1
		if self.header.attribute_count:
			# attrib + data frag
			frag_count += 2
		if self.file_entry.dependencies:
			frag_count += 1
		logging.debug(f"Count {frag_count}: textures {bool(self.header.texture_count)} attributes {bool(self.header.attribute_count)} dependencies {bool(self.file_entry.dependencies)}")
		return frag_count

	def load(self, file_path):
		fgm_data = self._get_data(file_path)
		datas, sizedstr_bytes = self._get_frag_datas(fgm_data)

		self.sized_str_entry.data_entry.update_data((fgm_data.buffer_bytes,))
		self.sized_str_entry.pointers[0].update_data(sizedstr_bytes)

		# inject fragment datas
		for frag, data in zip(self._valid_frags(), datas):
			logging.debug(f"frag: len old {len(frag.pointers[1].data)} len padding {len(frag.pointers[1].padding)} len new {len(data)}")
			frag.pointers[1].update_data(data, update_copies=True)

		# update dependencies on ovl
		for dependency, tex_name in zip(self.file_entry.dependencies, fgm_data.texture_files):
			self.set_dependency_identity(dependency, f"{tex_name}.tex")

	@staticmethod
	def _get_data(file_path):
		fgm_data = FgmFile()
		fgm_data.load(file_path)
		return fgm_data

	def _get_frag_datas(self, fgm_data):
		versions = get_versions(self.ovl)
		sizedstr_bytes = as_bytes(fgm_data.fgm_info, version_info=versions)
		textures_bytes = as_bytes(fgm_data.textures, version_info=versions)
		attributes_bytes = as_bytes(fgm_data.attributes, version_info=versions)
		# todo - this is definitely NOT right/ needed padding by comparing to stock FGMs
		# no clue what the 'rule' here is, it may not be padding but be appear if another ptr is missing
		# textures_bytes += get_padding(len(textures_bytes), alignment=16)
		# attributes never seem to have padding
		# attributes_bytes += get_padding(len(attributes_bytes), alignment=16)
		self.header = fgm_data.fgm_info
		datas = []
		if self.header.texture_count:
			datas.append(textures_bytes)
		if self.header.attribute_count:
			datas.append(attributes_bytes)
			datas.append(fgm_data.data_bytes)
		return datas, sizedstr_bytes

	def extract(self, out_dir, show_temp_files, progress_callback):
		name = self.sized_str_entry.name
		logging.info(f"Writing {name}")
		buffer_data = self.sized_str_entry.data_entry.buffer_datas[0]

		out_path = out_dir(name)
		with open(out_path, 'wb') as outfile:
			outfile.write(self.pack_header(b"FGM "))
			# we need this as its size is not predetermined
			data_lib_size = len(self.data_lib.pointers[1].data) if self.data_lib else 0
			outfile.write(struct.pack("II", data_lib_size, len(self.file_entry.dependencies)))
			outfile.write(self.sized_str_entry.pointers[0].data)
			for tex in self.file_entry.dependencies:
				outfile.write(zstr(tex.basename.encode()))
			# write each of the fragments
			for frag in self._valid_frags():
				outfile.write(frag.pointers[1].data)
			# write the buffer
			outfile.write(buffer_data)
		return out_path,

	def _valid_frags(self):
		"""Only yields fragments with data, ignores dependency pointers fragment and missing fragments"""
		for frag in (self.tex_info, self.attr_info, self.data_lib):
			if frag:
				yield frag
