from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class ResearchRoot(MemStruct):

	__name__ = 'ResearchRoot'

	_import_path = 'generated.formats.animalresearch.compounds.ResearchRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count = 0
		self.levels = ArrayPointer(self.context, self.count, ResearchRoot._import_path_map["generated.formats.animalresearch.compounds.ResearchLevel"])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'levels', ArrayPointer, (instance.count, ResearchRoot._import_path_map["generated.formats.animalresearch.compounds.ResearchLevel"]), (False, None)
		yield 'count', Uint64, (0, None), (False, None)
