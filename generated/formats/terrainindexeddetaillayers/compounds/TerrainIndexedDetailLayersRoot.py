from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class TerrainIndexedDetailLayersRoot(MemStruct):

	"""
	# 16 bytes
	"""

	__name__ = 'TerrainIndexedDetailLayersRoot'

	_import_key = 'terrainindexeddetaillayers.compounds.TerrainIndexedDetailLayersRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.layer_count = 0
		self.layer_list = ArrayPointer(self.context, self.layer_count, TerrainIndexedDetailLayersRoot._import_map["terrainindexeddetaillayers.compounds.TerrainDetailsLayerItem"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('layer_list', ArrayPointer, (None, None), (False, None), None),
		('layer_count', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'layer_list', ArrayPointer, (instance.layer_count, TerrainIndexedDetailLayersRoot._import_map["terrainindexeddetaillayers.compounds.TerrainDetailsLayerItem"]), (False, None)
		yield 'layer_count', Uint64, (0, None), (False, None)
