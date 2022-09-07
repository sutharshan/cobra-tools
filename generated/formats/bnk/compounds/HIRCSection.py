from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.bnk.compounds.HircPointer import HircPointer


class HIRCSection(BaseStruct):

	"""
	The HIRC section contains all the Wwise objects, including the events, the containers to group sounds, and the references to the sound files.
	"""

	__name__ = 'HIRCSection'

	_import_path = 'generated.formats.bnk.compounds.HIRCSection'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# length of following data
		self.length = 0
		self.count = 0
		self.hirc_pointers = Array(self.context, 0, None, (0,), HircPointer)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.length = 0
		self.count = 0
		self.hirc_pointers = Array(self.context, 0, None, (self.count,), HircPointer)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.length = Uint.from_stream(stream, instance.context, 0, None)
		instance.count = Uint.from_stream(stream, instance.context, 0, None)
		instance.hirc_pointers = Array.from_stream(stream, instance.context, 0, None, (instance.count,), HircPointer)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.length)
		Uint.to_stream(stream, instance.count)
		Array.to_stream(stream, instance.hirc_pointers, HircPointer)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'length', Uint, (0, None), (False, None)
		yield 'count', Uint, (0, None), (False, None)
		yield 'hirc_pointers', Array, (0, None, (instance.count,), HircPointer), (False, None)

	def get_info_str(self, indent=0):
		return f'HIRCSection [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
