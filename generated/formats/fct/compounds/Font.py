from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Font(MemStruct):

	"""
	JWE1: 16 bytes
	"""

	__name__ = 'Font'

	_import_key = 'fct.compounds.Font'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.data_size = 0
		self.zero = 0
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('data_size', Uint64, (0, None), (False, None), None),
		('zero', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'data_size', Uint64, (0, None), (False, None)
		yield 'zero', Uint64, (0, None), (False, None)
