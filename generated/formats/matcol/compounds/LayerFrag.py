from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class LayerFrag(MemStruct):

	__name__ = 'LayerFrag'

	_import_key = 'matcol.compounds.LayerFrag'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.u_0 = 0
		self.u_1 = 0
		self.info_count = 0
		self.u_2 = 0
		self.u_3 = 0
		self.attrib_count = 0
		self.layer_name = Pointer(self.context, 0, ZString)
		self.infos = ArrayPointer(self.context, self.info_count, LayerFrag._import_map["matcol.compounds.Info"])
		self.attribs = ArrayPointer(self.context, self.attrib_count, LayerFrag._import_map["matcol.compounds.Attrib"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('layer_name', Pointer, (0, ZString), (False, None), None),
		('u_0', Uint64, (0, None), (False, None), None),
		('u_1', Uint64, (0, None), (False, None), None),
		('infos', ArrayPointer, (None, None), (False, None), None),
		('info_count', Uint64, (0, None), (False, None), None),
		('u_2', Uint64, (0, None), (False, None), None),
		('u_3', Uint64, (0, None), (False, None), None),
		('attribs', ArrayPointer, (None, None), (False, None), None),
		('attrib_count', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'layer_name', Pointer, (0, ZString), (False, None)
		yield 'u_0', Uint64, (0, None), (False, None)
		yield 'u_1', Uint64, (0, None), (False, None)
		yield 'infos', ArrayPointer, (instance.info_count, LayerFrag._import_map["matcol.compounds.Info"]), (False, None)
		yield 'info_count', Uint64, (0, None), (False, None)
		yield 'u_2', Uint64, (0, None), (False, None)
		yield 'u_3', Uint64, (0, None), (False, None)
		yield 'attribs', ArrayPointer, (instance.attrib_count, LayerFrag._import_map["matcol.compounds.Attrib"]), (False, None)
		yield 'attrib_count', Uint64, (0, None), (False, None)
