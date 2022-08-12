from generated.formats.base.basic import fmt_member
import generated.formats.base.basic
from generated.array import Array
from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compound.MemStruct import MemStruct
from generated.formats.ovl_base.compound.Pointer import Pointer


class NextResearch(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_1 = 0
		self.item_name = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		print(f'set_defaults {self.__class__.__name__}')
		self.unk_1 = 0
		self.item_name = Array((self.arg,), Pointer, self.context, 0, generated.formats.base.basic.ZString)

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
		instance.item_name = Array.from_stream(stream, (instance.arg,), Pointer, instance.context, 0, generated.formats.base.basic.ZString)
		instance.unk_1 = stream.read_uint64()
		instance.item_name.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Array.to_stream(stream, instance.item_name, (instance.arg,), Pointer, instance.context, 0, generated.formats.base.basic.ZString)
		stream.write_uint64(instance.unk_1)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('item_name', Array, ((instance.arg,), Pointer, 0, generated.formats.base.basic.ZString))
		yield ('unk_1', Uint64, (0, None))

	def get_info_str(self, indent=0):
		return f'NextResearch [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* item_name = {fmt_member(self.item_name, indent+1)}'
		s += f'\n	* unk_1 = {fmt_member(self.unk_1, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
