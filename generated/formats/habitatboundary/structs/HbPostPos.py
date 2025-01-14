from generated.formats.base.basic import Float
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class HbPostPos(MemStruct):

	__name__ = 'HB_PostPos'

	_import_key = 'habitatboundary.structs.HbPostPos'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Right post offset from door.
		self.right = 0.0

		# Left Post offset from door.
		self.left = 0.0
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('right', Float, (0, None), (False, None), None),
		('left', Float, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'right', Float, (0, None), (False, None)
		yield 'left', Float, (0, None), (False, None)
