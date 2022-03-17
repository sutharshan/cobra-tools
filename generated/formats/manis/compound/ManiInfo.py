import numpy
from generated.context import ContextReference


class ManiInfo:

	"""
	288 bytes for JWE / PZ
	304 bytes for PC
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.duration = 0.0
		self.frame_count = 0

		# ?
		self.b = 0
		self.zeros_0 = numpy.zeros((6,), dtype=numpy.dtype('uint16'))
		self.extra_pc_1 = 0
		self.pos_bone_count = 0
		self.ori_bone_count = 0

		# likely
		self.scl_bone_count = 0

		# zero
		self.extra_pc = 0
		self.pos_bone_count_repeat = 0
		self.ori_bone_count_repeat = 0
		self.scl_bone_count_repeat = 0
		self.zeros_1 = 0
		self.zeros_1_new = 0
		self.float_count = 0

		# FF if unused
		self.count_a = 0

		# FF if unused
		self.count_b = 0

		# usually matches ms2 bone count, at least for JWE2 dinos. Doesn't match for PZ water wheel 5 vs ms2 2
		self.target_bone_count = 0

		# zero
		self.g = 0

		# rest 228 bytes
		self.zeros_2 = numpy.zeros((57,), dtype=numpy.dtype('uint32'))

		# rest 14 bytes
		self.extra_zeros_pc = numpy.zeros((6,), dtype=numpy.dtype('uint16'))
		self.pos_bone_min = 0
		self.pos_bone_max = 0
		self.ori_bone_min = 0
		self.ori_bone_max = 0

		# always FF
		self.scl_bone_min = 0

		# always 00
		self.scl_bone_max = 0
		self.pos_bone_count_related = 0
		self.pos_bone_count_repeat = 0
		self.ori_bone_count_related = 0
		self.ori_bone_count_repeat = 0

		# maybe, not observed yet
		self.scl_bone_count_related = 0
		self.scl_bone_count_repeat = 0
		self.zeros_end = 0
		self.zero_2_end = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.duration = 0.0
		self.frame_count = 0
		self.b = 0
		self.zeros_0 = numpy.zeros((6,), dtype=numpy.dtype('uint16'))
		if self.context.version == 18:
			self.extra_pc_1 = 0
		self.pos_bone_count = 0
		self.ori_bone_count = 0
		self.scl_bone_count = 0
		if self.context.version == 18:
			self.extra_pc = 0
		if self.context.version == 18:
			self.pos_bone_count_repeat = 0
		if self.context.version == 18:
			self.ori_bone_count_repeat = 0
		if self.context.version == 18:
			self.scl_bone_count_repeat = 0
		self.zeros_1 = 0
		if not (self.context.version == 18):
			self.zeros_1_new = 0
		self.float_count = 0
		self.count_a = 0
		self.count_b = 0
		self.target_bone_count = 0
		self.g = 0
		self.zeros_2 = numpy.zeros((57,), dtype=numpy.dtype('uint32'))
		if self.context.version == 18:
			self.extra_zeros_pc = numpy.zeros((6,), dtype=numpy.dtype('uint16'))
		self.pos_bone_min = 0
		self.pos_bone_max = 0
		self.ori_bone_min = 0
		self.ori_bone_max = 0
		self.scl_bone_min = 0
		self.scl_bone_max = 0
		if not (self.context.version == 18):
			self.pos_bone_count_related = 0
		if not (self.context.version == 18):
			self.pos_bone_count_repeat = 0
		if not (self.context.version == 18):
			self.ori_bone_count_related = 0
		if not (self.context.version == 18):
			self.ori_bone_count_repeat = 0
		if not (self.context.version == 18):
			self.scl_bone_count_related = 0
		if not (self.context.version == 18):
			self.scl_bone_count_repeat = 0
		if not (self.context.version == 18):
			self.zeros_end = 0
		self.zero_2_end = 0

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
		instance.duration = stream.read_float()
		instance.frame_count = stream.read_uint()
		instance.b = stream.read_uint()
		instance.zeros_0 = stream.read_ushorts((6,))
		if instance.context.version == 18:
			instance.extra_pc_1 = stream.read_ushort()
		instance.pos_bone_count = stream.read_ushort()
		instance.ori_bone_count = stream.read_ushort()
		instance.scl_bone_count = stream.read_ushort()
		if instance.context.version == 18:
			instance.extra_pc = stream.read_uint64()
			instance.pos_bone_count_repeat = stream.read_ushort()
		if instance.context.version == 18:
			instance.ori_bone_count_repeat = stream.read_ushort()
			instance.scl_bone_count_repeat = stream.read_ushort()
		instance.zeros_1 = stream.read_ushort()
		if not (instance.context.version == 18):
			instance.zeros_1_new = stream.read_uint()
		instance.float_count = stream.read_ushort()
		instance.count_a = stream.read_ubyte()
		instance.count_b = stream.read_ubyte()
		instance.target_bone_count = stream.read_ushort()
		instance.g = stream.read_ushort()
		instance.zeros_2 = stream.read_uints((57,))
		if instance.context.version == 18:
			instance.extra_zeros_pc = stream.read_ushorts((6,))
		instance.pos_bone_min = stream.read_ubyte()
		instance.pos_bone_max = stream.read_ubyte()
		instance.ori_bone_min = stream.read_ubyte()
		instance.ori_bone_max = stream.read_ubyte()
		instance.scl_bone_min = stream.read_byte()
		instance.scl_bone_max = stream.read_byte()
		if not (instance.context.version == 18):
			instance.pos_bone_count_related = stream.read_ubyte()
			instance.pos_bone_count_repeat = stream.read_ubyte()
		if not (instance.context.version == 18):
			instance.ori_bone_count_related = stream.read_ubyte()
			instance.ori_bone_count_repeat = stream.read_ubyte()
		if not (instance.context.version == 18):
			instance.scl_bone_count_related = stream.read_byte()
			instance.scl_bone_count_repeat = stream.read_byte()
		if not (instance.context.version == 18):
			instance.zeros_end = stream.read_ushort()
		instance.zero_2_end = stream.read_ushort()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_float(instance.duration)
		stream.write_uint(instance.frame_count)
		stream.write_uint(instance.b)
		stream.write_ushorts(instance.zeros_0)
		if instance.context.version == 18:
			stream.write_ushort(instance.extra_pc_1)
		stream.write_ushort(instance.pos_bone_count)
		stream.write_ushort(instance.ori_bone_count)
		stream.write_ushort(instance.scl_bone_count)
		if instance.context.version == 18:
			stream.write_uint64(instance.extra_pc)
			stream.write_ushort(instance.pos_bone_count_repeat)
		if instance.context.version == 18:
			stream.write_ushort(instance.ori_bone_count_repeat)
			stream.write_ushort(instance.scl_bone_count_repeat)
		stream.write_ushort(instance.zeros_1)
		if not (instance.context.version == 18):
			stream.write_uint(instance.zeros_1_new)
		stream.write_ushort(instance.float_count)
		stream.write_ubyte(instance.count_a)
		stream.write_ubyte(instance.count_b)
		stream.write_ushort(instance.target_bone_count)
		stream.write_ushort(instance.g)
		stream.write_uints(instance.zeros_2)
		if instance.context.version == 18:
			stream.write_ushorts(instance.extra_zeros_pc)
		stream.write_ubyte(instance.pos_bone_min)
		stream.write_ubyte(instance.pos_bone_max)
		stream.write_ubyte(instance.ori_bone_min)
		stream.write_ubyte(instance.ori_bone_max)
		stream.write_byte(instance.scl_bone_min)
		stream.write_byte(instance.scl_bone_max)
		if not (instance.context.version == 18):
			stream.write_ubyte(instance.pos_bone_count_related)
			stream.write_ubyte(instance.pos_bone_count_repeat)
		if not (instance.context.version == 18):
			stream.write_ubyte(instance.ori_bone_count_related)
			stream.write_ubyte(instance.ori_bone_count_repeat)
		if not (instance.context.version == 18):
			stream.write_byte(instance.scl_bone_count_related)
			stream.write_byte(instance.scl_bone_count_repeat)
		if not (instance.context.version == 18):
			stream.write_ushort(instance.zeros_end)
		stream.write_ushort(instance.zero_2_end)

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
		return f'ManiInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* duration = {self.duration.__repr__()}'
		s += f'\n	* frame_count = {self.frame_count.__repr__()}'
		s += f'\n	* b = {self.b.__repr__()}'
		s += f'\n	* zeros_0 = {self.zeros_0.__repr__()}'
		s += f'\n	* extra_pc_1 = {self.extra_pc_1.__repr__()}'
		s += f'\n	* pos_bone_count = {self.pos_bone_count.__repr__()}'
		s += f'\n	* ori_bone_count = {self.ori_bone_count.__repr__()}'
		s += f'\n	* scl_bone_count = {self.scl_bone_count.__repr__()}'
		s += f'\n	* extra_pc = {self.extra_pc.__repr__()}'
		s += f'\n	* pos_bone_count_repeat = {self.pos_bone_count_repeat.__repr__()}'
		s += f'\n	* ori_bone_count_repeat = {self.ori_bone_count_repeat.__repr__()}'
		s += f'\n	* scl_bone_count_repeat = {self.scl_bone_count_repeat.__repr__()}'
		s += f'\n	* zeros_1 = {self.zeros_1.__repr__()}'
		s += f'\n	* zeros_1_new = {self.zeros_1_new.__repr__()}'
		s += f'\n	* float_count = {self.float_count.__repr__()}'
		s += f'\n	* count_a = {self.count_a.__repr__()}'
		s += f'\n	* count_b = {self.count_b.__repr__()}'
		s += f'\n	* target_bone_count = {self.target_bone_count.__repr__()}'
		s += f'\n	* g = {self.g.__repr__()}'
		s += f'\n	* zeros_2 = {self.zeros_2.__repr__()}'
		s += f'\n	* extra_zeros_pc = {self.extra_zeros_pc.__repr__()}'
		s += f'\n	* pos_bone_min = {self.pos_bone_min.__repr__()}'
		s += f'\n	* pos_bone_max = {self.pos_bone_max.__repr__()}'
		s += f'\n	* ori_bone_min = {self.ori_bone_min.__repr__()}'
		s += f'\n	* ori_bone_max = {self.ori_bone_max.__repr__()}'
		s += f'\n	* scl_bone_min = {self.scl_bone_min.__repr__()}'
		s += f'\n	* scl_bone_max = {self.scl_bone_max.__repr__()}'
		s += f'\n	* pos_bone_count_related = {self.pos_bone_count_related.__repr__()}'
		s += f'\n	* pos_bone_count_repeat = {self.pos_bone_count_repeat.__repr__()}'
		s += f'\n	* ori_bone_count_related = {self.ori_bone_count_related.__repr__()}'
		s += f'\n	* ori_bone_count_repeat = {self.ori_bone_count_repeat.__repr__()}'
		s += f'\n	* scl_bone_count_related = {self.scl_bone_count_related.__repr__()}'
		s += f'\n	* scl_bone_count_repeat = {self.scl_bone_count_repeat.__repr__()}'
		s += f'\n	* zeros_end = {self.zeros_end.__repr__()}'
		s += f'\n	* zero_2_end = {self.zero_2_end.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
