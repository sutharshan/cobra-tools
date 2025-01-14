from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class TerrainDetailsLayerItem(MemStruct):

	__name__ = 'TerrainDetailsLayerItem'

	_import_key = 'terrainindexeddetaillayers.compounds.TerrainDetailsLayerItem'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.info_count = 0
		self.layer_name = Pointer(self.context, 0, ZString)
		self.info_list = ArrayPointer(self.context, self.info_count, TerrainDetailsLayerItem._import_map["terrainindexeddetaillayers.compounds.BrushitemStruct"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('layer_name', Pointer, (0, ZString), (False, None), None),
		('info_list', ArrayPointer, (None, None), (False, None), None),
		('info_count', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'layer_name', Pointer, (0, ZString), (False, None)
		yield 'info_list', ArrayPointer, (instance.info_count, TerrainDetailsLayerItem._import_map["terrainindexeddetaillayers.compounds.BrushitemStruct"]), (False, None)
		yield 'info_count', Uint64, (0, None), (False, None)
