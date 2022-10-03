from generated.base_struct import BaseStruct


class StreamDebugger(BaseStruct):

	"""
	logs stream address to debug log
	"""

	__name__ = 'StreamDebugger'

	_import_key = 'ms2.compounds.StreamDebugger'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
