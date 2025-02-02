import logging

import generated.formats.base.basic
import generated.formats.motiongraph.compounds.AnimationActivityData
import generated.formats.motiongraph.compounds.FootPlantActivityData
import generated.formats.motiongraph.compounds.DataStreamProducerActivityData
import generated.formats.motiongraph.compounds.SelectActivityActivityData
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer

from generated.formats.base.basic import Int64
from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class Activity(MemStruct):

	"""
	48 bytes
	"""

	__name__ = 'Activity'

	_import_key = 'motiongraph.compounds.Activity'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count_2 = 0
		self.count_3 = 0
		self.minus_one = 0
		self.data_type = Pointer(self.context, 0, ZString)

		# template has to be defined according to data type ie 'AnimationActivity' + 'Data'
		self.ptr = Pointer(self.context, 0, None)
		self.name_b = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('data_type', Pointer, (0, ZString), (False, None), None),
		('ptr', Pointer, (0, None), (False, None), None),
		('count_2', Uint64, (0, None), (False, None), None),
		('count_3', Uint64, (0, None), (False, None), None),
		('minus_one', Int64, (0, None), (False, None), None),
		('name_b', Pointer, (0, ZString), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'data_type', Pointer, (0, ZString), (False, None)
		yield 'ptr', Pointer, (0, None), (False, None)
		yield 'count_2', Uint64, (0, None), (False, None)
		yield 'count_3', Uint64, (0, None), (False, None)
		yield 'minus_one', Int64, (0, None), (False, None)
		yield 'name_b', Pointer, (0, ZString), (False, None)

	def get_ptr_template(self, prop):
		"""Returns the appropriate template for a pointer named 'prop', if exists.
		Must be overwritten in subclass"""
		if prop == "ptr":
			activity = self.data_type.data
			key = f"motiongraph.compounds.{activity}Data"
			try:
				return Activity._import_map[key]
			except:
				logging.warning(f"Unsupported activity '{activity}'")

