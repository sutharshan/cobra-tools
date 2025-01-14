from generated.formats.base.basic import Float
from generated.formats.ms2.compounds.Descriptor import Descriptor
from generated.formats.ms2.compounds.Vector3 import Vector3


class ListShort(Descriptor):

	"""
	used in JWE dinos
	"""

	__name__ = 'ListShort'

	_import_key = 'ms2.compounds.ListShort'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# location of the joint
		self.loc = Vector3(self.context, 0, None)

		# normalized
		self.direction = Vector3(self.context, 0, None)

		# min, le 0
		self.min = 0.0

		# max, ge 0
		self.max = 0.0
		if set_default:
			self.set_defaults()

	_attribute_list = Descriptor._attribute_list + [
		('loc', Vector3, (0, None), (False, None), None),
		('direction', Vector3, (0, None), (False, None), None),
		('min', Float, (0, None), (False, None), None),
		('max', Float, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'loc', Vector3, (0, None), (False, None)
		yield 'direction', Vector3, (0, None), (False, None)
		yield 'min', Float, (0, None), (False, None)
		yield 'max', Float, (0, None), (False, None)
