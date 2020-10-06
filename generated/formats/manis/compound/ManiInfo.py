import typing


class ManiInfo:

	"""
	120 bytes
	"""
	zeros_start: typing.List[int]
	duration: float

	# likely
	frame_count: int
	b: int

	# rest
	zeros_0: typing.List[int]
	c: int
	name_count: int

	# rest
	zeros_1: typing.List[int]
	e: int

	# always FF FF
	ffff: int
	g: int

	# rest
	zeros_2: typing.List[int]
	i: int
	j: int

	# always FF
	ff: int

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.zeros_start = []
		self.duration = 0
		self.frame_count = 0
		self.b = 0
		self.zeros_0 = []
		self.c = 0
		self.name_count = 0
		self.zeros_1 = []
		self.e = 0
		self.ffff = 0
		self.g = 0
		self.zeros_2 = []
		self.i = 0
		self.j = 0
		self.ff = 0

	def read(self, stream):

		io_start = stream.tell()
		self.zeros_start = [stream.read_ushort() for _ in range(5)]
		self.duration = stream.read_float()
		self.frame_count = stream.read_uint()
		self.b = stream.read_uint()
		self.zeros_0 = [stream.read_ushort() for _ in range(7)]
		self.c = stream.read_ushort()
		self.name_count = stream.read_ushort()
		self.zeros_1 = [stream.read_ushort() for _ in range(4)]
		self.e = stream.read_ushort()
		self.ffff = stream.read_ushort()
		self.g = stream.read_ushort()
		self.zeros_2 = [stream.read_uint() for _ in range(57)]
		self.i = stream.read_ushort()
		self.j = stream.read_ushort()
		self.ff = stream.read_ushort()

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		for item in self.zeros_start: stream.write_ushort(item)
		stream.write_float(self.duration)
		stream.write_uint(self.frame_count)
		stream.write_uint(self.b)
		for item in self.zeros_0: stream.write_ushort(item)
		stream.write_ushort(self.c)
		stream.write_ushort(self.name_count)
		for item in self.zeros_1: stream.write_ushort(item)
		stream.write_ushort(self.e)
		stream.write_ushort(self.ffff)
		stream.write_ushort(self.g)
		for item in self.zeros_2: stream.write_uint(item)
		stream.write_ushort(self.i)
		stream.write_ushort(self.j)
		stream.write_ushort(self.ff)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'ManiInfo [Size: '+str(self.io_size)+']'
		s += '\n	* zeros_start = ' + self.zeros_start.__repr__()
		s += '\n	* duration = ' + self.duration.__repr__()
		s += '\n	* frame_count = ' + self.frame_count.__repr__()
		s += '\n	* b = ' + self.b.__repr__()
		s += '\n	* zeros_0 = ' + self.zeros_0.__repr__()
		s += '\n	* c = ' + self.c.__repr__()
		s += '\n	* name_count = ' + self.name_count.__repr__()
		s += '\n	* zeros_1 = ' + self.zeros_1.__repr__()
		s += '\n	* e = ' + self.e.__repr__()
		s += '\n	* ffff = ' + self.ffff.__repr__()
		s += '\n	* g = ' + self.g.__repr__()
		s += '\n	* zeros_2 = ' + self.zeros_2.__repr__()
		s += '\n	* i = ' + self.i.__repr__()
		s += '\n	* j = ' + self.j.__repr__()
		s += '\n	* ff = ' + self.ff.__repr__()
		s += '\n'
		return s