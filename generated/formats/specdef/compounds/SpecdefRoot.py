from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Ushort
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.ForEachPointer import ForEachPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class SpecdefRoot(MemStruct):

	__name__ = 'SpecdefRoot'

	_import_key = 'specdef.compounds.SpecdefRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.attrib_count = 0
		self.flags = 0
		self.name_count = 0
		self.childspec_count = 0
		self.manager_count = 0
		self.script_count = 0
		self.attribs = ArrayPointer(self.context, self.attrib_count, SpecdefRoot._import_map["specdef.compounds.Spec"])
		self.name_foreach_attribs = ForEachPointer(self.context, self.attribs, SpecdefRoot._import_map["specdef.compounds.NamePtr"])
		self.data_foreach_attribs = ForEachPointer(self.context, self.attribs, SpecdefRoot._import_map["specdef.compounds.DataPtr"])
		self.names = Pointer(self.context, self.name_count, SpecdefRoot._import_map["specdef.compounds.PtrList"])
		self.childspecs = Pointer(self.context, self.childspec_count, SpecdefRoot._import_map["specdef.compounds.PtrList"])
		self.managers = Pointer(self.context, self.manager_count, SpecdefRoot._import_map["specdef.compounds.PtrList"])
		self.scripts = Pointer(self.context, self.script_count, SpecdefRoot._import_map["specdef.compounds.PtrList"])
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('attrib_count', Ushort, (0, None), (False, None), None),
		('flags', Ushort, (0, None), (False, None), None),
		('name_count', Ubyte, (0, None), (False, None), None),
		('childspec_count', Ubyte, (0, None), (False, None), None),
		('manager_count', Ubyte, (0, None), (False, None), None),
		('script_count', Ubyte, (0, None), (False, None), None),
		('attribs', ArrayPointer, (None, None), (False, None), None),
		('name_foreach_attribs', ForEachPointer, (None, None), (False, None), None),
		('data_foreach_attribs', ForEachPointer, (None, None), (False, None), None),
		('names', Pointer, (None, None), (False, None), None),
		('childspecs', Pointer, (None, None), (False, None), None),
		('managers', Pointer, (None, None), (False, None), None),
		('scripts', Pointer, (None, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'attrib_count', Ushort, (0, None), (False, None)
		yield 'flags', Ushort, (0, None), (False, None)
		yield 'name_count', Ubyte, (0, None), (False, None)
		yield 'childspec_count', Ubyte, (0, None), (False, None)
		yield 'manager_count', Ubyte, (0, None), (False, None)
		yield 'script_count', Ubyte, (0, None), (False, None)
		yield 'attribs', ArrayPointer, (instance.attrib_count, SpecdefRoot._import_map["specdef.compounds.Spec"]), (False, None)
		yield 'name_foreach_attribs', ForEachPointer, (instance.attribs, SpecdefRoot._import_map["specdef.compounds.NamePtr"]), (False, None)
		yield 'data_foreach_attribs', ForEachPointer, (instance.attribs, SpecdefRoot._import_map["specdef.compounds.DataPtr"]), (False, None)
		yield 'names', Pointer, (instance.name_count, SpecdefRoot._import_map["specdef.compounds.PtrList"]), (False, None)
		yield 'childspecs', Pointer, (instance.childspec_count, SpecdefRoot._import_map["specdef.compounds.PtrList"]), (False, None)
		yield 'managers', Pointer, (instance.manager_count, SpecdefRoot._import_map["specdef.compounds.PtrList"]), (False, None)
		yield 'scripts', Pointer, (instance.script_count, SpecdefRoot._import_map["specdef.compounds.PtrList"]), (False, None)
