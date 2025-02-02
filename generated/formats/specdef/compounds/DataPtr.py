from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class DataPtr(MemStruct):

	"""
	#ARG# is dtype
	"""

	__name__ = 'DataPtr'

	_import_key = 'specdef.compounds.DataPtr'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.data_ptr = Pointer(self.context, self.arg.dtype, DataPtr._import_map["specdef.compounds.Data"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('data_ptr', Pointer, (None, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'data_ptr', Pointer, (instance.arg.dtype, DataPtr._import_map["specdef.compounds.Data"]), (False, None)
