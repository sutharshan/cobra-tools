class Triplet:

	"""
	3 bytes - seemingly constant per mime
	"""

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# ?
		self.a = 0

		# ?
		self.b = 0

		# ?
		self.c = 0

	def read(self, stream):

		self.io_start = stream.tell()
		self.a = stream.read_ubyte()
		self.b = stream.read_ubyte()
		self.c = stream.read_ubyte()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_ubyte(self.a)
		stream.write_ubyte(self.b)
		stream.write_ubyte(self.c)

		self.io_size = stream.tell() - self.io_start

	def get_info_str(self):
		return f'Triplet [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* a = {self.a.__repr__()}'
		s += f'\n	* b = {self.b.__repr__()}'
		s += f'\n	* c = {self.c.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s