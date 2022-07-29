from generated.formats.base.basic import fmt_member
from generated.array import Array
from generated.formats.base.basic import Uint
from generated.formats.bnk.compound.DataPointer import DataPointer
from generated.struct import StructBase


class DIDXSection(StructBase):

	"""
	second Section of a soundback aux
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default)

		# length of following data
		self.length = 0
		self.data_pointers = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.length = 0
		self.data_pointers = Array((int(self.length / 12),), DataPointer, self.context, 0, None)

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
		instance.length = stream.read_uint()
		instance.data_pointers = Array.from_stream(stream, (int(instance.length / 12),), DataPointer, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_uint(instance.length)
		Array.to_stream(stream, instance.data_pointers, (int(instance.length / 12),), DataPointer, instance.context, 0, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('length', Uint, (0, None))
		yield ('data_pointers', Array, ((int(instance.length / 12),), DataPointer, 0, None))

	def get_info_str(self, indent=0):
		return f'DIDXSection [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* length = {fmt_member(self.length, indent+1)}'
		s += f'\n	* data_pointers = {fmt_member(self.data_pointers, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
