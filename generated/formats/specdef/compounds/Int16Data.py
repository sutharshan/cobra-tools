from generated.formats.base.basic import Short
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class Int16Data(MemStruct):

	"""
	8 bytes
	"""

	__name__ = 'Int16Data'

	_import_path = 'generated.formats.specdef.compounds.Int16Data'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.imin = 0
		self.imax = 0
		self.ivalue = 0
		self.ioptional = 0
		self.enum = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.imin = 0
		self.imax = 0
		self.ivalue = 0
		self.ioptional = 0
		self.enum = Pointer(self.context, 0, None)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.imin = Short.from_stream(stream, instance.context, 0, None)
		instance.imax = Short.from_stream(stream, instance.context, 0, None)
		instance.ivalue = Short.from_stream(stream, instance.context, 0, None)
		instance.ioptional = Short.from_stream(stream, instance.context, 0, None)
		instance.enum = Pointer.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.enum, int):
			instance.enum.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Short.to_stream(stream, instance.imin)
		Short.to_stream(stream, instance.imax)
		Short.to_stream(stream, instance.ivalue)
		Short.to_stream(stream, instance.ioptional)
		Pointer.to_stream(stream, instance.enum)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'imin', Short, (0, None), (False, None)
		yield 'imax', Short, (0, None), (False, None)
		yield 'ivalue', Short, (0, None), (False, None)
		yield 'ioptional', Short, (0, None), (False, None)
		yield 'enum', Pointer, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Int16Data [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
