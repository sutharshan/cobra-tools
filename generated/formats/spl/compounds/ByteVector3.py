from generated.formats.base.basic import Byte
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class ByteVector3(MemStruct):

	"""
	A vector in 3D space (x,y,z).
	"""

	__name__ = 'ByteVector3'

	_import_path = 'generated.formats.spl.compounds.ByteVector3'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# First coordinate.
		self.x = 0

		# Second coordinate.
		self.y = 0

		# Third coordinate.
		self.z = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.x = 0
		self.y = 0
		self.z = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.x = Byte.from_stream(stream, instance.context, 0, None)
		instance.y = Byte.from_stream(stream, instance.context, 0, None)
		instance.z = Byte.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Byte.to_stream(stream, instance.x)
		Byte.to_stream(stream, instance.y)
		Byte.to_stream(stream, instance.z)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'x', Byte, (0, None), (False, None)
		yield 'y', Byte, (0, None), (False, None)
		yield 'z', Byte, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'ByteVector3 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
