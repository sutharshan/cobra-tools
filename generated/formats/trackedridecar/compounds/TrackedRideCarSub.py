from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class TrackedRideCarSub(MemStruct):

	"""
	32 bytes
	"""

	__name__ = 'TrackedRideCarSub'

	_import_key = 'trackedridecar.compounds.TrackedRideCarSub'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.float = 0.0
		self.u_0 = 0
		self.vecs_count = 0
		self.zero_1 = 0
		self.vectors = ArrayPointer(self.context, self.vecs_count, TrackedRideCarSub._import_map["trackedridecar.compounds.Vector3"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('float', Float, (0, None), (False, None), None),
		('u_0', Uint, (0, None), (False, None), None),
		('vectors', ArrayPointer, (None, None), (False, None), None),
		('vecs_count', Uint64, (0, None), (False, None), None),
		('zero_1', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'float', Float, (0, None), (False, None)
		yield 'u_0', Uint, (0, None), (False, None)
		yield 'vectors', ArrayPointer, (instance.vecs_count, TrackedRideCarSub._import_map["trackedridecar.compounds.Vector3"]), (False, None)
		yield 'vecs_count', Uint64, (0, None), (False, None)
		yield 'zero_1', Uint64, (0, None), (False, None)
