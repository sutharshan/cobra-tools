from generated.formats.base.basic import Uint
from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class LuaRoot(MemStruct):

	"""
	ZTUAC: 32 bytes
	newer: 48 bytes
	all meta data except lua size seems to just be meta data, can be zeroed
	"""

	__name__ = 'LuaRoot'

	_import_key = 'lua.compounds.LuaRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.lua_size = 0
		self.sixteenk = 0
		self.hash = 0
		self.zero_0 = 0
		self.zero_1 = 0
		self.zero_2 = 0
		self.source_path = Pointer(self.context, 0, ZString)
		self.likely_alignment = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('lua_size', Uint, (0, None), (False, None), None),
		('sixteenk', Uint, (0, None), (False, None), None),
		('hash', Uint, (0, None), (False, None), None),
		('zero_0', Uint, (0, None), (False, None), None),
		('source_path', Pointer, (0, ZString), (False, None), True),
		('likely_alignment', Pointer, (0, ZString), (False, None), True),
		('zero_1', Uint64, (0, None), (False, None), None),
		('zero_2', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'lua_size', Uint, (0, None), (False, None)
		yield 'sixteenk', Uint, (0, None), (False, None)
		yield 'hash', Uint, (0, None), (False, None)
		yield 'zero_0', Uint, (0, None), (False, None)
		if instance.context.version >= 18:
			yield 'source_path', Pointer, (0, ZString), (False, None)
			yield 'likely_alignment', Pointer, (0, ZString), (False, None)
		yield 'zero_1', Uint64, (0, None), (False, None)
		yield 'zero_2', Uint64, (0, None), (False, None)
