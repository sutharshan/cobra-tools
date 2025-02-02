from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class ScaleformlanguagedataRoot(MemStruct):

	"""
	# PC - is maybe organized differently here
	PZ: 48 bytes
	"""

	__name__ = 'ScaleformlanguagedataRoot'

	_import_key = 'scaleformlanguagedata.compounds.ScaleformlanguagedataRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.zero_0 = 0
		self.zero_1 = 0
		self.count = 0
		self.zero_2 = 0
		self.zero_3 = 0
		self.fonts = ArrayPointer(self.context, self.count, ScaleformlanguagedataRoot._import_map["scaleformlanguagedata.compounds.FontInfo"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('zero_0', Uint64, (0, None), (False, None), None),
		('zero_1', Uint64, (0, None), (False, None), None),
		('fonts', ArrayPointer, (None, None), (False, None), None),
		('count', Uint64, (0, None), (False, None), None),
		('zero_2', Uint64, (0, None), (False, None), None),
		('zero_3', Uint64, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'zero_0', Uint64, (0, None), (False, None)
		yield 'zero_1', Uint64, (0, None), (False, None)
		yield 'fonts', ArrayPointer, (instance.count, ScaleformlanguagedataRoot._import_map["scaleformlanguagedata.compounds.FontInfo"]), (False, None)
		yield 'count', Uint64, (0, None), (False, None)
		yield 'zero_2', Uint64, (0, None), (False, None)
		yield 'zero_3', Uint64, (0, None), (False, None)
