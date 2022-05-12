from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class AssetEntry:

	"""
	refers to root entries so they can be grouped into set entries.
	It seems to point exclusively to RootEntry's whose Ext Hash is FF FF FF FF aka max uint32
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.file_hash = 0
		self.zero_0 = 0
		self.ext_hash = 0
		self.zero_1 = 0

		# index into root entries array; hash of targeted file matches this assetentry's hash.
		self.file_index = 0
		self.zero_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.file_hash = 0
		self.zero_0 = 0
		if self.context.version >= 19:
			self.ext_hash = 0
		if self.context.version >= 19:
			self.zero_1 = 0
		self.file_index = 0
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
		instance.file_hash = stream.read_uint()
		instance.zero_0 = stream.read_uint()
		if instance.context.version >= 19:
			instance.ext_hash = stream.read_uint()
			instance.zero_1 = stream.read_uint()
		instance.file_index = stream.read_uint()
		instance.zero_2 = stream.read_uint()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint(instance.file_hash)
		stream.write_uint(instance.zero_0)
		if instance.context.version >= 19:
			stream.write_uint(instance.ext_hash)
			stream.write_uint(instance.zero_1)
		stream.write_uint(instance.file_index)
		stream.write_uint(instance.zero_2)

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
		return f'AssetEntry [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* file_hash = {fmt_member(self.file_hash, indent+1)}'
		s += f'\n	* zero_0 = {fmt_member(self.zero_0, indent+1)}'
		s += f'\n	* ext_hash = {fmt_member(self.ext_hash, indent+1)}'
		s += f'\n	* zero_1 = {fmt_member(self.zero_1, indent+1)}'
		s += f'\n	* file_index = {fmt_member(self.file_index, indent+1)}'
		s += f'\n	* zero_2 = {fmt_member(self.zero_2, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
