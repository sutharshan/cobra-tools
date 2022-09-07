from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class PathType(MemStruct):

	__name__ = 'PathType'

	_import_path = 'generated.formats.path.compounds.PathType'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.enum_value = 0
		self.min_width = 4.0
		self.max_width = 10.0
		self._unk_int_2 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.enum_value = 0
		self.min_width = 4.0
		self.max_width = 10.0
		self._unk_int_2 = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.enum_value = Uint.from_stream(stream, instance.context, 0, None)
		instance.min_width = Float.from_stream(stream, instance.context, 0, None)
		instance.max_width = Float.from_stream(stream, instance.context, 0, None)
		instance._unk_int_2 = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.enum_value)
		Float.to_stream(stream, instance.min_width)
		Float.to_stream(stream, instance.max_width)
		Uint.to_stream(stream, instance._unk_int_2)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'enum_value', Uint, (0, None), (False, None)
		yield 'min_width', Float, (0, None), (False, 4.0)
		yield 'max_width', Float, (0, None), (False, 10.0)
		yield '_unk_int_2', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'PathType [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
