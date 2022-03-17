from generated.array import Array
from generated.context import ContextReference
from generated.formats.base.basic import ZString
from generated.formats.ms2.compound.Buffer0 import Buffer0
from generated.formats.ms2.compound.BufferInfo import BufferInfo
from generated.formats.ms2.compound.BufferInfoPC import BufferInfoPC
from generated.formats.ms2.compound.BufferInfoZT import BufferInfoZT
from generated.formats.ms2.compound.ModelInfo import ModelInfo
from generated.formats.ms2.compound.ModelReader import ModelReader
from generated.formats.ms2.compound.Ms2SizedStrData import Ms2SizedStrData


class Ms2InfoHeader:

	"""
	Custom header struct
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.bone_info_size = 0
		self.info = Ms2SizedStrData(self.context, 0, None)
		self.mdl_2_names = Array((self.info.mdl_2_count,), ZString, self.context, 0, None)
		self.buffer_0 = Buffer0(self.context, self.info, None)
		self.buffer_info = BufferInfo(self.context, 0, None)
		self.buffer_info = BufferInfoZT(self.context, self.info.vertex_buffer_count, None)
		self.buffer_info = BufferInfoPC(self.context, 0, None)
		self.model_infos = Array((self.info.mdl_2_count,), ModelInfo, self.context, 0, None)

		# handles interleaved (old) or separate (new) styles for models and bone infos
		self.models_reader = ModelReader(self.context, self.model_infos, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.bone_info_size = 0
		self.info = Ms2SizedStrData(self.context, 0, None)
		self.mdl_2_names = Array((self.info.mdl_2_count,), ZString, self.context, 0, None)
		self.buffer_0 = Buffer0(self.context, self.info, None)
		if self.context.version >= 47 and self.info.vertex_buffer_count:
			self.buffer_info = BufferInfo(self.context, 0, None)
		if self.context.version == 13:
			self.buffer_info = BufferInfoZT(self.context, self.info.vertex_buffer_count, None)
		if self.context.version == 32:
			self.buffer_info = BufferInfoPC(self.context, 0, None)
		self.model_infos = Array((self.info.mdl_2_count,), ModelInfo, self.context, 0, None)
		self.models_reader = ModelReader(self.context, self.model_infos, None)

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
		instance.bone_info_size = stream.read_uint()
		instance.info = Ms2SizedStrData.from_stream(stream, instance.context, 0, None)
		instance.mdl_2_names = stream.read_zstrings((instance.info.mdl_2_count,))
		instance.buffer_0 = Buffer0.from_stream(stream, instance.context, instance.info, None)
		if instance.context.version >= 47 and instance.info.vertex_buffer_count:
			instance.buffer_info = BufferInfo.from_stream(stream, instance.context, 0, None)
		if instance.context.version == 13:
			instance.buffer_info = BufferInfoZT.from_stream(stream, instance.context, instance.info.vertex_buffer_count, None)
		if instance.context.version == 32:
			instance.buffer_info = BufferInfoPC.from_stream(stream, instance.context, 0, None)
		instance.model_infos = Array.from_stream(stream, (instance.info.mdl_2_count,), ModelInfo, instance.context, 0, None)
		instance.models_reader = ModelReader.from_stream(stream, instance.context, instance.model_infos, None)

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint(instance.bone_info_size)
		Ms2SizedStrData.to_stream(stream, instance.info)
		stream.write_zstrings(instance.mdl_2_names)
		Buffer0.to_stream(stream, instance.buffer_0)
		if instance.context.version >= 47 and instance.info.vertex_buffer_count:
			BufferInfo.to_stream(stream, instance.buffer_info)
		if instance.context.version == 13:
			BufferInfoZT.to_stream(stream, instance.buffer_info)
		if instance.context.version == 32:
			BufferInfoPC.to_stream(stream, instance.buffer_info)
		Array.to_stream(stream, instance.model_infos, (instance.info.mdl_2_count,), ModelInfo, instance.context, 0, None)
		ModelReader.to_stream(stream, instance.models_reader)

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

	def get_info_str(self):
		return f'Ms2InfoHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* bone_info_size = {self.bone_info_size.__repr__()}'
		s += f'\n	* info = {self.info.__repr__()}'
		s += f'\n	* mdl_2_names = {self.mdl_2_names.__repr__()}'
		s += f'\n	* buffer_0 = {self.buffer_0.__repr__()}'
		s += f'\n	* buffer_info = {self.buffer_info.__repr__()}'
		s += f'\n	* model_infos = {self.model_infos.__repr__()}'
		s += f'\n	* models_reader = {self.models_reader.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
