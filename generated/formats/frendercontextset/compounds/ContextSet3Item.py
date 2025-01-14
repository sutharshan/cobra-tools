from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class ContextSet3Item(MemStruct):

	__name__ = 'ContextSet3Item'

	_import_key = 'frendercontextset.compounds.ContextSet3Item'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.stuff_3_id_allways_1 = 0
		self.stuff_3_name_1 = Pointer(self.context, 0, ZString)
		self.stuff_3_sub = Pointer(self.context, 0, ContextSet3Item._import_map["frendercontextset.compounds.ContextSet3SubItem"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('stuff_3_name_1', Pointer, (0, ZString), (False, None), None),
		('stuff_3_sub', Pointer, (0, None), (False, None), None),
		('stuff_3_id_allways_1', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'stuff_3_name_1', Pointer, (0, ZString), (False, None)
		yield 'stuff_3_sub', Pointer, (0, ContextSet3Item._import_map["frendercontextset.compounds.ContextSet3SubItem"]), (False, None)
		yield 'stuff_3_id_allways_1', Uint64, (0, None), (False, None)
