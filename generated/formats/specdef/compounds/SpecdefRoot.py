from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Ushort
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.ForEachPointer import ForEachPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class SpecdefRoot(MemStruct):

	__name__ = 'SpecdefRoot'

	_import_path = 'generated.formats.specdef.compounds.SpecdefRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.attrib_count = 0
		self.flags = 0
		self.name_count = 0
		self.childspec_count = 0
		self.manager_count = 0
		self.script_count = 0
		self.attribs = ArrayPointer(self.context, self.attrib_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.Spec"])
		self.name_foreach_attribs = ForEachPointer(self.context, self.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.NamePtr"])
		self.data_foreach_attribs = ForEachPointer(self.context, self.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.DataPtr"])
		self.names = Pointer(self.context, self.name_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		self.childspecs = Pointer(self.context, self.childspec_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		self.managers = Pointer(self.context, self.manager_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		self.scripts = Pointer(self.context, self.script_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.attrib_count = 0
		self.flags = 0
		self.name_count = 0
		self.childspec_count = 0
		self.manager_count = 0
		self.script_count = 0
		self.attribs = ArrayPointer(self.context, self.attrib_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.Spec"])
		self.name_foreach_attribs = ForEachPointer(self.context, self.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.NamePtr"])
		self.data_foreach_attribs = ForEachPointer(self.context, self.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.DataPtr"])
		self.names = Pointer(self.context, self.name_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		self.childspecs = Pointer(self.context, self.childspec_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		self.managers = Pointer(self.context, self.manager_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		self.scripts = Pointer(self.context, self.script_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.attrib_count = Ushort.from_stream(stream, instance.context, 0, None)
		instance.flags = Ushort.from_stream(stream, instance.context, 0, None)
		instance.name_count = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.childspec_count = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.manager_count = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.script_count = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.attribs = ArrayPointer.from_stream(stream, instance.context, instance.attrib_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.Spec"])
		instance.name_foreach_attribs = ForEachPointer.from_stream(stream, instance.context, instance.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.NamePtr"])
		instance.data_foreach_attribs = ForEachPointer.from_stream(stream, instance.context, instance.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.DataPtr"])
		instance.names = Pointer.from_stream(stream, instance.context, instance.name_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		instance.childspecs = Pointer.from_stream(stream, instance.context, instance.childspec_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		instance.managers = Pointer.from_stream(stream, instance.context, instance.manager_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		instance.scripts = Pointer.from_stream(stream, instance.context, instance.script_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"])
		if not isinstance(instance.attribs, int):
			instance.attribs.arg = instance.attrib_count
		if not isinstance(instance.name_foreach_attribs, int):
			instance.name_foreach_attribs.arg = instance.attribs
		if not isinstance(instance.data_foreach_attribs, int):
			instance.data_foreach_attribs.arg = instance.attribs
		if not isinstance(instance.names, int):
			instance.names.arg = instance.name_count
		if not isinstance(instance.childspecs, int):
			instance.childspecs.arg = instance.childspec_count
		if not isinstance(instance.managers, int):
			instance.managers.arg = instance.manager_count
		if not isinstance(instance.scripts, int):
			instance.scripts.arg = instance.script_count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Ushort.to_stream(stream, instance.attrib_count)
		Ushort.to_stream(stream, instance.flags)
		Ubyte.to_stream(stream, instance.name_count)
		Ubyte.to_stream(stream, instance.childspec_count)
		Ubyte.to_stream(stream, instance.manager_count)
		Ubyte.to_stream(stream, instance.script_count)
		ArrayPointer.to_stream(stream, instance.attribs)
		ForEachPointer.to_stream(stream, instance.name_foreach_attribs)
		ForEachPointer.to_stream(stream, instance.data_foreach_attribs)
		Pointer.to_stream(stream, instance.names)
		Pointer.to_stream(stream, instance.childspecs)
		Pointer.to_stream(stream, instance.managers)
		Pointer.to_stream(stream, instance.scripts)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'attrib_count', Ushort, (0, None), (False, None)
		yield 'flags', Ushort, (0, None), (False, None)
		yield 'name_count', Ubyte, (0, None), (False, None)
		yield 'childspec_count', Ubyte, (0, None), (False, None)
		yield 'manager_count', Ubyte, (0, None), (False, None)
		yield 'script_count', Ubyte, (0, None), (False, None)
		yield 'attribs', ArrayPointer, (instance.attrib_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.Spec"]), (False, None)
		yield 'name_foreach_attribs', ForEachPointer, (instance.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.NamePtr"]), (False, None)
		yield 'data_foreach_attribs', ForEachPointer, (instance.attribs, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.DataPtr"]), (False, None)
		yield 'names', Pointer, (instance.name_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"]), (False, None)
		yield 'childspecs', Pointer, (instance.childspec_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"]), (False, None)
		yield 'managers', Pointer, (instance.manager_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"]), (False, None)
		yield 'scripts', Pointer, (instance.script_count, SpecdefRoot._import_path_map["generated.formats.specdef.compounds.PtrList"]), (False, None)

	def get_info_str(self, indent=0):
		return f'SpecdefRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
