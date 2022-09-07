from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class TwoPtrFirst(MemStruct):

	"""
	16 bytes
	"""

	__name__ = 'TwoPtrFirst'

	_import_path = 'generated.formats.motiongraph.compounds.TwoPtrFirst'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count_0 = 0
		self.ptr = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.count_0 = 0
		self.ptr = Pointer(self.context, 0, None)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.ptr = Pointer.from_stream(stream, instance.context, 0, None)
		instance.count_0 = Uint64.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.ptr, int):
			instance.ptr.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.ptr)
		Uint64.to_stream(stream, instance.count_0)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'ptr', Pointer, (0, None), (False, None)
		yield 'count_0', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'TwoPtrFirst [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
