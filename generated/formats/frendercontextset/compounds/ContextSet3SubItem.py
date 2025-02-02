from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class ContextSet3SubItem(MemStruct):

	__name__ = 'ContextSet3SubItem'

	_import_key = 'frendercontextset.compounds.ContextSet3SubItem'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.stuff_31_id_allways_0 = 0
		self.stuff_31_name_1 = Pointer(self.context, 0, ZString)
		self.stuff_31_name_2 = Pointer(self.context, 0, ZString)
		self.stuff_31_name_3 = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('stuff_31_name_1', Pointer, (0, ZString), (False, None), None),
		('stuff_31_name_2', Pointer, (0, ZString), (False, None), None),
		('stuff_31_name_3', Pointer, (0, ZString), (False, None), None),
		('stuff_31_id_allways_0', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'stuff_31_name_1', Pointer, (0, ZString), (False, None)
		yield 'stuff_31_name_2', Pointer, (0, ZString), (False, None)
		yield 'stuff_31_name_3', Pointer, (0, ZString), (False, None)
		yield 'stuff_31_id_allways_0', Uint64, (0, None), (False, None)
