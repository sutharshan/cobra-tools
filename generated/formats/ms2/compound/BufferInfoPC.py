from source.formats.base.basic import fmt_member
import numpy
from generated.context import ContextReference


class BufferInfoPC:

	"""
	PC: 32 bytes
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.zeros_1 = numpy.zeros((2,), dtype=numpy.dtype('uint64'))

		# Total size of vertex buffer for PC, starting with the 0 - 16 byte indices
		self.vertex_buffer_size = 0
		self.zero_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.zeros_1 = numpy.zeros((2,), dtype=numpy.dtype('uint64'))
		self.vertex_buffer_size = 0
		self.zero_2 = 0

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
		instance.zeros_1 = stream.read_uint64s((2,))
		instance.vertex_buffer_size = stream.read_uint64()
		instance.zero_2 = stream.read_uint64()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint64s(instance.zeros_1)
		stream.write_uint64(instance.vertex_buffer_size)
		stream.write_uint64(instance.zero_2)

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
		return f'BufferInfoPC [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* zeros_1 = {fmt_member(self.zeros_1, indent+1)}'
		s += f'\n	* vertex_buffer_size = {fmt_member(self.vertex_buffer_size, indent+1)}'
		s += f'\n	* zero_2 = {fmt_member(self.zero_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
