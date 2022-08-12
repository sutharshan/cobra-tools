from generated.formats.base.basic import fmt_member
import generated.formats.base.basic
import generated.formats.motiongraph.compound.Sixtyfour
import generated.formats.motiongraph.compound.TwoPtrFirst
from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class ThirdFrag(MemStruct):

	"""
	72 bytes
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count_0 = 0
		self.count_1 = 0
		self.count_2 = 0
		self.count_3 = 0
		self.count_4 = 0
		self.lua_method = 0
		self.ptr_1 = 0
		self.ptr_2 = 0
		self.member = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		print(f'set_defaults {self.__class__.__name__}')
		self.count_0 = 0
		self.count_1 = 0
		self.count_2 = 0
		self.count_3 = 0
		self.count_4 = 0
		self.lua_method = Pointer(self.context, 0, generated.formats.base.basic.ZString)
		self.ptr_1 = Pointer(self.context, 0, generated.formats.motiongraph.compound.TwoPtrFirst.TwoPtrFirst)
		self.ptr_2 = Pointer(self.context, 0, generated.formats.motiongraph.compound.Sixtyfour.Sixtyfour)
		self.member = Pointer(self.context, 0, generated.formats.base.basic.ZString)

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
		instance.lua_method = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.count_0 = stream.read_uint64()
		instance.count_1 = stream.read_uint64()
		instance.ptr_1 = Pointer.from_stream(stream, instance.context, 0, generated.formats.motiongraph.compound.TwoPtrFirst.TwoPtrFirst)
		instance.count_2 = stream.read_uint64()
		instance.count_3 = stream.read_uint64()
		instance.ptr_2 = Pointer.from_stream(stream, instance.context, 0, generated.formats.motiongraph.compound.Sixtyfour.Sixtyfour)
		instance.count_4 = stream.read_uint64()
		instance.member = Pointer.from_stream(stream, instance.context, 0, generated.formats.base.basic.ZString)
		instance.lua_method.arg = 0
		instance.ptr_1.arg = 0
		instance.ptr_2.arg = 0
		instance.member.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.lua_method)
		stream.write_uint64(instance.count_0)
		stream.write_uint64(instance.count_1)
		Pointer.to_stream(stream, instance.ptr_1)
		stream.write_uint64(instance.count_2)
		stream.write_uint64(instance.count_3)
		Pointer.to_stream(stream, instance.ptr_2)
		stream.write_uint64(instance.count_4)
		Pointer.to_stream(stream, instance.member)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('lua_method', Pointer, (0, generated.formats.base.basic.ZString))
		yield ('count_0', Uint64, (0, None))
		yield ('count_1', Uint64, (0, None))
		yield ('ptr_1', Pointer, (0, generated.formats.motiongraph.compound.TwoPtrFirst.TwoPtrFirst))
		yield ('count_2', Uint64, (0, None))
		yield ('count_3', Uint64, (0, None))
		yield ('ptr_2', Pointer, (0, generated.formats.motiongraph.compound.Sixtyfour.Sixtyfour))
		yield ('count_4', Uint64, (0, None))
		yield ('member', Pointer, (0, generated.formats.base.basic.ZString))

	def get_info_str(self, indent=0):
		return f'ThirdFrag [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* lua_method = {fmt_member(self.lua_method, indent+1)}'
		s += f'\n	* count_0 = {fmt_member(self.count_0, indent+1)}'
		s += f'\n	* count_1 = {fmt_member(self.count_1, indent+1)}'
		s += f'\n	* ptr_1 = {fmt_member(self.ptr_1, indent+1)}'
		s += f'\n	* count_2 = {fmt_member(self.count_2, indent+1)}'
		s += f'\n	* count_3 = {fmt_member(self.count_3, indent+1)}'
		s += f'\n	* ptr_2 = {fmt_member(self.ptr_2, indent+1)}'
		s += f'\n	* count_4 = {fmt_member(self.count_4, indent+1)}'
		s += f'\n	* member = {fmt_member(self.member, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
