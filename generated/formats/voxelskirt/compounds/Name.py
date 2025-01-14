from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint64


class Name(BaseStruct):

	__name__ = 'Name'

	_import_key = 'voxelskirt.compounds.Name'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# address of ZString
		self._offset = 0
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('_offset', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield '_offset', Uint64, (0, None), (False, None)
