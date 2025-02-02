from generated.base_struct import BaseStruct
from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ms2.compounds.Vector3 import Vector3


class Sphere(BaseStruct):

	__name__ = 'Sphere'

	_import_key = 'ms2.compounds.Sphere'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# center of the sphere
		self.center = Vector3(self.context, 0, None)

		# radius around the center
		self.radius = 0.0

		# apparently unused
		self.zero = 0
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('center', Vector3, (0, None), (False, None), None),
		('radius', Float, (0, None), (False, None), None),
		('zero', Uint, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'center', Vector3, (0, None), (False, None)
		yield 'radius', Float, (0, None), (False, None)
		yield 'zero', Uint, (0, None), (False, None)
