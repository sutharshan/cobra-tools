from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class Uint64Data(MemStruct):

	"""
	48 bytes in log
	"""

	__name__ = 'Uint64Data'

	_import_key = 'specdef.compounds.Uint64Data'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.imin = 0
		self.imax = 0
		self.ivalue = 0
		self.ioptional = 0
		self.enum = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('imin', Uint64, (0, None), (False, None), None),
		('imax', Uint64, (0, None), (False, None), None),
		('ivalue', Uint64, (0, None), (False, None), None),
		('ioptional', Uint64, (0, None), (False, None), None),
		('enum', Pointer, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'imin', Uint64, (0, None), (False, None)
		yield 'imax', Uint64, (0, None), (False, None)
		yield 'ivalue', Uint64, (0, None), (False, None)
		yield 'ioptional', Uint64, (0, None), (False, None)
		yield 'enum', Pointer, (0, None), (False, None)
