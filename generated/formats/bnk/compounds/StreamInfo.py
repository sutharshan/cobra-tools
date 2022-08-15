from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Uint64


class StreamInfo(BaseStruct):

	"""
	Describes a wem file in an s type bank stream
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.offset = 0
		self.size = 0

		# referred to by the events aux file
		self.event_id = 0
		self.zero = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.offset = 0
		self.size = 0
		self.event_id = 0
		self.zero = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.offset = stream.read_uint64()
		instance.size = stream.read_uint64()
		instance.event_id = stream.read_uint()
		instance.zero = stream.read_uint()

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_uint64(instance.offset)
		stream.write_uint64(instance.size)
		stream.write_uint(instance.event_id)
		stream.write_uint(instance.zero)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'offset', Uint64, (0, None)
		yield 'size', Uint64, (0, None)
		yield 'event_id', Uint, (0, None)
		yield 'zero', Uint, (0, None)

	def get_info_str(self, indent=0):
		return f'StreamInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* offset = {self.fmt_member(self.offset, indent+1)}'
		s += f'\n	* size = {self.fmt_member(self.size, indent+1)}'
		s += f'\n	* event_id = {self.fmt_member(self.event_id, indent+1)}'
		s += f'\n	* zero = {self.fmt_member(self.zero, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
