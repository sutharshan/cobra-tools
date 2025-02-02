from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.basic import ZStringObfuscated
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class RenderParametersRoot(MemStruct):

	"""
	32 bytes
	"""

	__name__ = 'RenderParametersRoot'

	_import_key = 'renderparameters.compounds.RenderParametersRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count = 0
		self.unk = 0
		self.param_name = Pointer(self.context, 0, ZStringObfuscated)
		self.params = Pointer(self.context, self.count, RenderParametersRoot._import_map["renderparameters.compounds.ParamList"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('param_name', Pointer, (0, ZStringObfuscated), (False, None), None),
		('params', Pointer, (None, None), (False, None), None),
		('count', Uint64, (0, None), (False, None), None),
		('unk', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'param_name', Pointer, (0, ZStringObfuscated), (False, None)
		yield 'params', Pointer, (instance.count, RenderParametersRoot._import_map["renderparameters.compounds.ParamList"]), (False, None)
		yield 'count', Uint64, (0, None), (False, None)
		yield 'unk', Uint64, (0, None), (False, None)
