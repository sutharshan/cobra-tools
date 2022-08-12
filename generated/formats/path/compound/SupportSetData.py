from generated.formats.base.basic import fmt_member
from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compound.MemStruct import MemStruct


class SupportSetData(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default)
		self.unk_index = 0
		self.unk_int_1 = 0
		self.unk_int_2 = 0
		self.unk_float_1 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.unk_index = 0
		self.unk_int_1 = 0
		self.unk_int_2 = 0
		self.unk_float_1 = 0.0

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
		instance.unk_index = stream.read_uint()
		instance.unk_int_1 = stream.read_uint()
		instance.unk_int_2 = stream.read_uint()
		instance.unk_float_1 = stream.read_float()

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_uint(instance.unk_index)
		stream.write_uint(instance.unk_int_1)
		stream.write_uint(instance.unk_int_2)
		stream.write_float(instance.unk_float_1)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('unk_index', Uint, (0, None))
		yield ('unk_int_1', Uint, (0, None))
		yield ('unk_int_2', Uint, (0, None))
		yield ('unk_float_1', Float, (0, None))

	def get_info_str(self, indent=0):
		return f'SupportSetData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* unk_index = {fmt_member(self.unk_index, indent+1)}'
		s += f'\n	* unk_int_1 = {fmt_member(self.unk_int_1, indent+1)}'
		s += f'\n	* unk_int_2 = {fmt_member(self.unk_int_2, indent+1)}'
		s += f'\n	* unk_float_1 = {fmt_member(self.unk_float_1, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
