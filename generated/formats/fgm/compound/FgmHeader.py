from source.formats.base.basic import fmt_member
import generated.formats.fgm.compound.AttributeInfo
import generated.formats.fgm.compound.TextureInfo
from generated.formats.ovl_base.compound.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class FgmHeader(MemStruct):

	"""
	Sized str entry of 16 bytes, then ptrs, then padding
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.texture_count = 0
		self.texture_count = 0
		self.attribute_count = 0
		self.attribute_count = 0
		self.unk_0 = 0
		self.unk_1 = 0
		self.textures = ArrayPointer(self.context, self.texture_count, generated.formats.fgm.compound.TextureInfo.TextureInfo)
		self.attributes = ArrayPointer(self.context, self.attribute_count, generated.formats.fgm.compound.AttributeInfo.AttributeInfo)
		self.dependencies = Pointer(self.context, 0, None)
		self.data_lib = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		if self.context.version <= 15:
			self.texture_count = 0
		if self.context.version >= 17:
			self.texture_count = 0
		if self.context.version <= 15:
			self.attribute_count = 0
		if self.context.version >= 17:
			self.attribute_count = 0
		self.unk_0 = 0
		self.unk_1 = 0
		self.textures = ArrayPointer(self.context, self.texture_count, generated.formats.fgm.compound.TextureInfo.TextureInfo)
		self.attributes = ArrayPointer(self.context, self.attribute_count, generated.formats.fgm.compound.AttributeInfo.AttributeInfo)
		self.dependencies = Pointer(self.context, 0, None)
		self.data_lib = Pointer(self.context, 0, None)

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
		if instance.context.version <= 15:
			instance.texture_count = stream.read_uint()
		if instance.context.version >= 17:
			instance.texture_count = stream.read_uint64()
		if instance.context.version <= 15:
			instance.attribute_count = stream.read_uint()
		if instance.context.version >= 17:
			instance.attribute_count = stream.read_uint64()
		instance.textures = ArrayPointer.from_stream(stream, instance.context, instance.texture_count, generated.formats.fgm.compound.TextureInfo.TextureInfo)
		instance.attributes = ArrayPointer.from_stream(stream, instance.context, instance.attribute_count, generated.formats.fgm.compound.AttributeInfo.AttributeInfo)
		instance.dependencies = Pointer.from_stream(stream, instance.context, 0, None)
		instance.data_lib = Pointer.from_stream(stream, instance.context, 0, None)
		instance.unk_0 = stream.read_uint64()
		instance.unk_1 = stream.read_uint64()
		instance.textures.arg = instance.texture_count
		instance.attributes.arg = instance.attribute_count
		instance.dependencies.arg = 0
		instance.data_lib.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		if instance.context.version <= 15:
			stream.write_uint(instance.texture_count)
		if instance.context.version >= 17:
			stream.write_uint64(instance.texture_count)
		if instance.context.version <= 15:
			stream.write_uint(instance.attribute_count)
		if instance.context.version >= 17:
			stream.write_uint64(instance.attribute_count)
		ArrayPointer.to_stream(stream, instance.textures)
		ArrayPointer.to_stream(stream, instance.attributes)
		Pointer.to_stream(stream, instance.dependencies)
		Pointer.to_stream(stream, instance.data_lib)
		stream.write_uint64(instance.unk_0)
		stream.write_uint64(instance.unk_1)

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
		return f'FgmHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* texture_count = {fmt_member(self.texture_count, indent+1)}'
		s += f'\n	* attribute_count = {fmt_member(self.attribute_count, indent+1)}'
		s += f'\n	* textures = {fmt_member(self.textures, indent+1)}'
		s += f'\n	* attributes = {fmt_member(self.attributes, indent+1)}'
		s += f'\n	* dependencies = {fmt_member(self.dependencies, indent+1)}'
		s += f'\n	* data_lib = {fmt_member(self.data_lib, indent+1)}'
		s += f'\n	* unk_0 = {fmt_member(self.unk_0, indent+1)}'
		s += f'\n	* unk_1 = {fmt_member(self.unk_1, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
