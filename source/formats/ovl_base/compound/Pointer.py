# START_GLOBALS
import struct
from generated.context import ContextReference
# from generated.formats.ovl.compound.Fragment import Fragment

# END_GLOBALS


class Pointer:

	"""
	a pointer in an ovl memory layout
	"""

	context = ContextReference()

# START_CLASS

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.offset = 0
		# todo - test if it is better to already create the template here, or on demand from MemStruct
		# self.data = template(context, arg=0, template=None)
		self.data = None
		self.frag = None
		self.pool_type = None
		if set_default:
			self.set_defaults()

	def get_info_str(self):
		return f'Pointer [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* offset = {self.offset.__repr__()}'
		s += f'\n	* data = {self.data.__repr__()}'
		return s

	def read_ptr(self, pool):
		"""Looks up the address of the pointer, checks if a frag points to pointer and reads the data at its address as
		the specified template."""
		# find the frag entry with matching pointers[0].data_offset
		self.frag = pool.offset_2_link_entry.get(self.io_start, None)
		# pointer may be a nullptr, so ignore
		if not self.frag:
			# print("is a nullptr")
			return
		# it is a fragment, not a dependency
		if hasattr(self.frag, "struct_ptr"):
			# now read an instance of template class at the offset
			self.read_template()
		else:
			# store dependency name
			self.data = self.frag.name

	def read_template(self):
		if self.template:
			self.data = self.template.from_stream(self.frag.struct_ptr.stream, self.context, self.arg)

	def write_pointer(self):
		assert (self.data is not None) and self.frag
		# if bytes have been set (usually manually), don't ask, just write
		if isinstance(self.data, (bytes, bytearray)):
			# seek to end, set data_offset, write
			self.frag.struct_ptr.write_to_pool(self.data)
		else:
			# process the generated data
			try:
				self.write_template()
			except struct.error:
				raise TypeError(f"Failed to write pointer data {self.data} type: {type(self.data)} as {self.template}")

	def write_template(self):
		assert self.template is not None
		# align pointer
		if isinstance(self.data, str):
			alignment = 1
		else:
			alignment = 16
		self.frag.struct_ptr.write_instance(self.template, self.data, alignment=alignment)

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
