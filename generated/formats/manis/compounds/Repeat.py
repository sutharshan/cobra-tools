import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint64


class Repeat(BaseStruct):

	__name__ = 'Repeat'

	_import_key = 'manis.compounds.Repeat'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.zeros_0 = Array(self.context, 0, None, (0,), Uint64)

		# to be read sequentially starting after this array
		self.byte_size = 0
		self.zeros_1 = Array(self.context, 0, None, (0,), Uint64)
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('zeros_0', Array, (0, None, (7,), Uint64), (False, None), None),
		('byte_size', Uint64, (0, None), (False, None), None),
		('zeros_1', Array, (0, None, (2,), Uint64), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'zeros_0', Array, (0, None, (7,), Uint64), (False, None)
		yield 'byte_size', Uint64, (0, None), (False, None)
		yield 'zeros_1', Array, (0, None, (2,), Uint64), (False, None)
