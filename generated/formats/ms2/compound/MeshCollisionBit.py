from source.formats.base.basic import fmt_member
import numpy
from generated.array import Array
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort
from generated.struct import StructBase


class MeshCollisionBit(StructBase):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# ?
		self.countd = 0

		# always 2954754766?
		self.consts = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.countd = numpy.zeros((34,), dtype=numpy.dtype('uint16'))
		self.consts = numpy.zeros((3,), dtype=numpy.dtype('uint32'))

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
		instance.countd = stream.read_ushorts((34,))
		instance.consts = stream.read_uints((3,))

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_ushorts(instance.countd)
		stream.write_uints(instance.consts)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('countd', Array, ((34,), Ushort, 0, None))
		yield ('consts', Array, ((3,), Uint, 0, None))

	def get_info_str(self, indent=0):
		return f'MeshCollisionBit [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* countd = {fmt_member(self.countd, indent+1)}'
		s += f'\n	* consts = {fmt_member(self.consts, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
