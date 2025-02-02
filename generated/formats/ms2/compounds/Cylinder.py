from generated.formats.ms2.compounds.Capsule import Capsule


class Cylinder(Capsule):

	"""
	identical data to capsule, just imported differently
	"""

	__name__ = 'Cylinder'

	_import_key = 'ms2.compounds.Cylinder'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		if set_default:
			self.set_defaults()

	_attribute_list = Capsule._attribute_list + [
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
