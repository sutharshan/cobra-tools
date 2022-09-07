from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class UserinterfaceicondataRoot(MemStruct):

	__name__ = 'UserinterfaceicondataRoot'

	_import_path = 'generated.formats.userinterfaceicondata.compounds.UserinterfaceicondataRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.tex_name = Pointer(self.context, 0, ZString)
		self.ovl_name = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.tex_name = Pointer(self.context, 0, ZString)
		self.ovl_name = Pointer(self.context, 0, ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.tex_name = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.ovl_name = Pointer.from_stream(stream, instance.context, 0, ZString)
		if not isinstance(instance.tex_name, int):
			instance.tex_name.arg = 0
		if not isinstance(instance.ovl_name, int):
			instance.ovl_name.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.tex_name)
		Pointer.to_stream(stream, instance.ovl_name)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'tex_name', Pointer, (0, ZString), (False, None)
		yield 'ovl_name', Pointer, (0, ZString), (False, None)

	def get_info_str(self, indent=0):
		return f'UserinterfaceicondataRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
