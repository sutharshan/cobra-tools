from generated.array import Array
from generated.formats.motiongraph.compounds.SinglePtr import SinglePtr
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class PtrList(MemStruct):

	"""
	8 * arg bytes
	"""

	__name__ = 'PtrList'

	_import_key = 'motiongraph.compounds.PtrList'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.ptrs = Array(self.context, 0, self.template, (0,), SinglePtr)
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('ptrs', Array, (0, None, (None,), SinglePtr), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'ptrs', Array, (0, instance.template, (instance.arg,), SinglePtr), (False, None)
