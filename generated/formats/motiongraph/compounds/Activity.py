
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

	_import_path = 'generated.formats.motiongraph.compounds.Activity'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count_2 = 0
		self.count_3 = 0
		self.minus_one = 0
		self.data_type = Pointer(self.context, 0, ZString)
		self.ptr = Pointer(self.context, 0, None)
		self.name_b = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.count_2 = 0
		self.count_3 = 0
		self.minus_one = 0
		self.data_type = Pointer(self.context, 0, ZString)
		self.ptr = Pointer(self.context, 0, None)
		self.name_b = Pointer(self.context, 0, ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.data_type = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.ptr = Pointer.from_stream(stream, instance.context, 0, None)
		instance.count_2 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_3 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.minus_one = Int64.from_stream(stream, instance.context, 0, None)
		instance.name_b = Pointer.from_stream(stream, instance.context, 0, ZString)
		if not isinstance(instance.data_type, int):
			instance.data_type.arg = 0
		if not isinstance(instance.ptr, int):
			instance.ptr.arg = 0
		if not isinstance(instance.name_b, int):
			instance.name_b.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.data_type)
		Pointer.to_stream(stream, instance.ptr)
		Uint64.to_stream(stream, instance.count_2)
		Uint64.to_stream(stream, instance.count_3)
		Int64.to_stream(stream, instance.minus_one)
		Pointer.to_stream(stream, instance.name_b)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'data_type', Pointer, (0, ZString), (False, None)
		yield 'ptr', Pointer, (0, None), (False, None)
		yield 'count_2', Uint64, (0, None), (False, None)
		yield 'count_3', Uint64, (0, None), (False, None)
		yield 'minus_one', Int64, (0, None), (False, None)
		yield 'name_b', Pointer, (0, ZString), (False, None)

	def get_info_str(self, indent=0):
		return f'Activity [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_ptr_template(self, prop):
		"""Returns the appropriate template for a pointer named 'prop', if exists.
		Must be overwritten in subclass"""
		# print(f"get_ptr_template Activity")
		if prop == "ptr":
			activity = self.data_type.data
			# print(f"data_type {self.data_type.data}")
			if activity == "AnimationActivity":
				# print(f"data_type {self.data_type.data}")
				return generated.formats.motiongraph.compounds.AnimationActivityData.AnimationActivityData
			elif activity == "FootPlantActivity":
				# print(f"data_type {self.data_type.data}")
				return generated.formats.motiongraph.compounds.FootPlantActivityData.FootPlantActivityData
			elif activity == "DataStreamProducerActivity":
				# print(f"data_type {self.data_type.data}")
				return generated.formats.motiongraph.compounds.DataStreamProducerActivityData.DataStreamProducerActivityData
			elif activity == "SelectActivityActivity":
				# print(f"data_type {self.data_type.data}")
				return generated.formats.motiongraph.compounds.SelectActivityActivityData.SelectActivityActivityData
			else:
				logging.warning(f"Unsupported activity '{activity}'")

