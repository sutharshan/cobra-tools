import io
import logging
import os
import struct

from generated.formats.dds import DdsFile
from generated.formats.dds.enum.D3D10ResourceDimension import D3D10ResourceDimension
from generated.formats.dds.enum.DxgiFormat import DxgiFormat
from generated.formats.dds.enum.FourCC import FourCC
from generated.formats.ovl.versions import *
from generated.formats.tex import TexFile
from generated.formats.tex.compound.Header3Data0 import Header3Data0
from generated.formats.tex.compound.Header3Data0Pc import Header3Data0Pc
from generated.formats.tex.compound.Header3Data1 import Header3Data1
from generated.formats.tex.compound.Header3Data1Pc import Header3Data1Pc
from generated.formats.tex.compound.Header3Data1Ztuac import Header3Data1Ztuac
from generated.formats.tex.compound.Header7Data1 import Header7Data1
from modules.formats.BaseFormat import BaseFile
from modules.formats.shared import get_versions
from modules.helpers import split_path

from ovl_util import texconv, imarray


def align_to(width, comp, alignment=64):
	"""Return input padded to the next closer multiple of alignment"""
	# get bpp from compression type
	if "BC1" in comp or "BC4" in comp:
		alignment *= 2
	# print("alignment",alignment)
	m = width % alignment
	if m:
		return width + alignment - m
	return width


class DdsLoader(BaseFile):

	def create(self):
		pass

	def collect(self):
		self.assign_ss_entry()
		# verify that it's empty - not always true
		# assert self.sized_str_entry.pointers[0].data == b"\x00" * 16
		if is_jwe(self.ovl) or is_pz(self.ovl) or is_pz16(self.ovl) or is_jwe2(self.ovl):
			self.assign_fixed_frags(2)
		elif is_pc(self.ovl) or is_ztuac(self.ovl):
			self.assign_fixed_frags(1)

	def load(self, file_path):
		logging.debug(f"Loading image {file_path}")
		name_ext, name, ext = split_path(file_path)
		if ext == ".png":
			self.load_png(file_path)
		elif ext == ".dds":
			self.load_dds(file_path)

	def load_dds(self, file_path):
		versions = get_versions(self.ovl)
		if is_pc(self.ovl):
			header_3_0, headers_3_1, header_7 = self.get_tex_structs_pc(self.sized_str_entry)
			tex_h = header_7.height
			tex_w = header_7.width
			tex_d = header_3_0.one_0
			tex_a = header_7.array_size
		else:
			header_3_0, header_3_1, header_7 = self.get_tex_structs(self.sized_str_entry, versions)
			tex_h = header_7.height
			tex_w = header_7.width
			tex_d = header_7.depth
			tex_a = header_7.array_size
		comp = header_3_0.compression_type.name
		tex_w = align_to(tex_w, comp)
	
		# read archive tex header to make sure we have the right mip count
		# even when users import DDS with mips when it should have none
	
		# load dds
		dds_file = DdsFile()
		dds_file.load(file_path)
		self.ensure_size_match(dds_file, tex_h, tex_w, tex_d, tex_a, comp)
		if is_pc(self.ovl):
			for buffer, tex_header_3 in zip(self.sized_str_entry.data_entry.sorted_streams, headers_3_1):
				dds_buff = dds_file.pack_mips_pc(tex_header_3.num_mips)
				if len(dds_buff) < buffer.size:
					print(f"Last {buffer.size - len(dds_buff)} bytes of DDS buffer are not overwritten!")
					dds_buff = dds_buff + buffer.data[len(dds_buff):]
				buffer.update_data(dds_buff)
		else:
			out_bytes = dds_file.pack_mips(header_7.num_mips)
			# with dds_file.writer(file_path+"dump.dds") as stream:
			# 	dds_file.write(stream)
			# 	stream.write(out_bytes)
	
			sorted_streams = sorted(self.sized_str_entry.data_entry.sorted_streams, key=lambda b: len(b.data), reverse=True)
			sum_of_buffers = sum(buffer.size for buffer in sorted_streams)
			if len(out_bytes) != sum_of_buffers:
				print(
					f"Packing of MipMaps failed. OVL expects {sum_of_buffers} bytes, but packing generated {len(out_bytes)} bytes.")
	
			with io.BytesIO(out_bytes) as reader:
				for buffer in sorted_streams:
					print(buffer)
					dds_buff = reader.read(buffer.size)
					if len(dds_buff) < buffer.size:
						print(f"Last {buffer.size - len(dds_buff)} bytes of DDS buffer are not overwritten!")
						dds_buff = dds_buff + buffer.data[len(dds_buff):]
					buffer.update_data(dds_buff)

	def get_tex_structs(self, sized_str_entry, ovl_version):
		# we have exactly two fragments, pointing into these pool_types
		f_3_3, f_3_7 = sized_str_entry.fragments
	
		header_3_0 = f_3_7.pointers[0].load_as(Header3Data0, version_info=ovl_version)[0]
		headers_3_1 = f_3_3.pointers[1].load_as(Header3Data1, num=f_3_3.pointers[1].data_size//24, version_info=ovl_version)
		# print(f_3_3.pointers[1].data_size // 24)
		print(header_3_0)
		print(headers_3_1)
		header_7 = f_3_7.pointers[1].load_as(Header7Data1, version_info=ovl_version)[0]
		print(header_7)
		return header_3_0, headers_3_1, header_7
	
	def get_tex_structs_pc(self, sized_str_entry):
		frag = sized_str_entry.fragments[0]
		print(frag.pointers[0].address, frag.pointers[0].data_size)
		print(frag.pointers[1].address, frag.pointers[1].data_size)
		header_3_0 = frag.pointers[0].load_as(Header3Data0Pc)[0]
		# headers_3_1 = frag.pointers[1].load_as(Header3Data1Pc, num=header_3_0.one_2)
		# alternative?
		headers_3_1 = frag.pointers[1].load_as(Header3Data1Pc, num=frag.pointers[1].data_size//8, args=())
		print(header_3_0)
		print(headers_3_1)
		# this corresponds to a stripped down header_7
		header_7 = headers_3_1[0]
		return header_3_0, headers_3_1, header_7
	
	def get_tex_structs_ztuac(self, sized_str_entry):
		frag = sized_str_entry.fragments[0]
		# print(frag.pointers[0].address, frag.pointers[0].data_size)
		# print(frag.pointers[1].address, frag.pointers[1].data_size)
		header_3_0 = frag.pointers[0].load_as(Header3Data0Pc)[0]
		# print(header_3_0)
		header_3_1 = frag.pointers[1].load_as(Header3Data1Ztuac, args=(header_3_0.one_1,))[0]
		# print(header_3_1)
		# this corresponds to a stripped down header_7
		header_7 = header_3_1.lods[0]
		return header_3_0, header_3_1.lods, header_7	
	
	def create_dds_struct(self):
		dds_file = DdsFile()
		dds_file.header_string.data = b"DDS "
	
		# header flags
		dds_file.flags.height = 1
		dds_file.flags.width = 1
		dds_file.flags.mipmap_count = 1
		dds_file.flags.linear_size = 1
	
		# pixel format flags
		dds_file.pixel_format.flags.four_c_c = 1
		dds_file.pixel_format.four_c_c = FourCC.DX10

		dds_file.dx_10.resource_dimension = D3D10ResourceDimension.D3D10_RESOURCE_DIMENSION_TEXTURE2D
		dds_file.dx_10.array_size = 1
	
		# caps 1
		dds_file.caps_1.texture = 0
		return dds_file

	def extract(self, out_dir, show_temp_files, progress_callback):
		tex_name = self.sized_str_entry.name
		basename = os.path.splitext(tex_name)[0]
		dds_name = basename + ".dds"
		logging.info(f"Writing {tex_name}")
		logging.debug(f"Num streams: {len(self.sized_str_entry.data_entry.stream_datas)}")
		# get joined output buffer
		buffer_data = b"".join(sorted(self.sized_str_entry.data_entry.stream_datas, key=len, reverse=True))

		out_files = []
		tex_path = out_dir(tex_name)
		if show_temp_files:
			out_files.append(tex_path)
		with open(tex_path, "wb") as tex_file:
			tex_file.write(self.pack_header(b"TEX"))
			# num_buffers
			# tex_file.write(struct.pack("I", 1+len(self.file_entry.streams)))
			tex_file.write(self.sized_str_entry.pointers[0].data)
			for frag in self.sized_str_entry.fragments:
				tex_file.write(frag.pointers[0].data)
			for frag in self.sized_str_entry.fragments:
				tex_file.write(frag.pointers[1].data)
			tex_file.write(buffer_data)

		tex_file = TexFile(self.ovl.context)
		tex_file.load(tex_path)
		# print(tex_file)
		# return out_files
		dds_file = self.create_dds_struct()
		dds_file.buffer = buffer_data
		# versions = get_versions(self.ovl)
		# if is_ztuac(self.ovl):
		# 	header_3_0, headers_3_1, header_7 = self.get_tex_structs_ztuac(self.sized_str_entry)
		# 	dds_file.width = header_7.width
		# 	dds_file.height = header_7.height
		# 	dds_file.mipmap_count = header_7.num_mips
		# 	dds_file.linear_size = len(buffer_data)
		# 	header_7.array_size = 1
		# 	dds_file.depth = header_3_0.one_0
		# elif is_pc(self.ovl):
		# 	header_3_0, headers_3_1, header_7 = self.get_tex_structs_pc(self.sized_str_entry)
		# 	# print(header_7)
		# 	dds_file.width = header_7.width
		# 	# hack until we have proper support for array_size on the image editors
		# 	# todo - this is most assuredly not array size for ED
		# 	dds_file.height = header_7.height# * max(1, header_7.array_size)
		# 	dds_file.mipmap_count = header_7.num_mips
		# 	dds_file.linear_size = len(buffer_data)
		# 	dds_file.depth = header_3_0.one_0
		#
		# else:
		# 	header_3_0, headers_3_1, header_7 = self.get_tex_structs(self.sized_str_entry, versions)
		#
		if not len(buffer_data) == tex_file.frag_11.data_size:
			print(
				f"7_1 data size ({tex_file.frag_11.data_size}) and actual data size of combined buffers ({len(buffer_data)}) do not match up (bug)")

		dds_file.width = tex_file.frag_11.width
		# hack until we have proper support for array_size on the image editors
		dds_file.height = tex_file.frag_11.height * tex_file.frag_11.array_size
		dds_file.depth = tex_file.frag_11.depth
		dds_file.linear_size = tex_file.frag_11.data_size
		dds_file.mipmap_count = tex_file.frag_11.num_mips
	
		try:
			dds_type = tex_file.frag_10.compression_type.name
			print(tex_file.frag_10.compression_type)
			# account for aliases
			if dds_type.endswith(("_B", "_C")):
				dds_type = dds_type[:-2]
			dds_compression_types = ((dds_type, DxgiFormat[dds_type]),)
		except KeyError:
			dds_compression_types = [(x.name, x) for x in DxgiFormat]
			print(f"Unknown compression type {tex_file.frag_10.compression_type}, trying all compression types")
		print("dds_compression_type", dds_compression_types)

		# write out everything for each compression type
		for dds_type, dds_value in dds_compression_types:
			# print(dds_file.width)
			# header attribs
			if not is_ztuac(self.ovl):
				dds_file.width = align_to(dds_file.width, dds_type)
	
			# dx 10 stuff
			dds_file.dx_10.dxgi_format = dds_value
	
			# start out
			dds_path = out_dir(dds_name)
			if len(dds_compression_types) > 1:
				dds_path += f"_{dds_type}.dds"
	
			# write dds
			dds_file.save(dds_path)
			# print(dds_file)
			if show_temp_files:
				out_files.append(dds_path)
	
			# convert the dds to PNG, PNG must be visible so put it in out_dir
			png_file_path = texconv.dds_to_png(dds_path, dds_file.height)
	
			if os.path.isfile(png_file_path):
				# postprocessing of the png
				out_files.extend(imarray.wrapper(png_file_path, tex_file.frag_11, self.ovl))
		return out_files

	def load_png(self, file_path):
		# convert the png into a dds, then inject that
		versions = get_versions(self.ovl)
		if is_pc(self.ovl):
			header_3_0, headers_3_1, header_7 = self.get_tex_structs_pc(self.sized_str_entry)
		else:
			header_3_0, header_3_1, header_7 = self.get_tex_structs(self.sized_str_entry, versions)
		# texconv works without prefix
		dds_compression_type = header_3_0.compression_type.name
		compression = dds_compression_type.replace("DXGI_FORMAT_", "")
		dds_file_path = texconv.png_to_dds(
			file_path, header_7.height * header_7.array_size, True, codec=compression, mips=header_7.num_mips)
	
		# inject the dds generated by texconv
		self.load_dds(dds_file_path)
		# remove the temp file if desired
		texconv.clear_tmp(dds_file_path, True)

	def ensure_size_match(self, dds_header, tex_h, tex_w, tex_d, tex_a, comp):
		"""Check that DDS files have the same basic size"""
		dds_h = dds_header.height
		dds_w = dds_header.width
		dds_d = dds_header.depth
		dds_a = dds_header.dx_10.array_size
	
		if dds_h * dds_w * dds_d * dds_a != tex_h * tex_w * tex_d * tex_a:
			raise AttributeError(
				f"Dimensions do not match for {self.file_entry.name}!\n\n"
				f"Dimensions: height x width x depth [array size]\n"
				f"OVL Texture: {tex_h} x {tex_w} x {tex_d} [{tex_a}]\n"
				f"Injected texture: {dds_h} x {dds_w} x {dds_d} [{dds_a}]\n\n"
				f"Make the external texture's dimensions match the OVL texture and try again!")
	
