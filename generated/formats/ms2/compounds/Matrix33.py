import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Float


class Matrix33(BaseStruct):

	"""
	A 3x3 rotation matrix; M^T M=identity, det(M)=1.
	"""

	__name__ = 'Matrix33'

	_import_key = 'ms2.compounds.Matrix33'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Stored in OpenGL column-major format.
		self.data = Array(self.context, 0, None, (0,), Float)
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('data', Array, (0, None, (3, 3,), Float), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'data', Array, (0, None, (3, 3,), Float), (False, None)
