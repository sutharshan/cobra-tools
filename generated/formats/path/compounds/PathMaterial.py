from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class PathMaterial(MemStruct):

	__name__ = 'PathMaterial'

	_import_path = 'generated.formats.path.compounds.PathMaterial'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.path_sub_type = 0
		self.num_data = 0
		self.elevated_mat = Pointer(self.context, 0, ZString)
		self.elevated_mat_valid = Pointer(self.context, 0, ZString)
		self.elevated_mat_invalid = Pointer(self.context, 0, ZString)
		self.terrain_mat = Pointer(self.context, 0, ZString)
		self.terrain_mat_valid = Pointer(self.context, 0, ZString)
		self.terrain_mat_invalid = Pointer(self.context, 0, ZString)
		self.underside_mat_1 = Pointer(self.context, 0, ZString)
		self.underside_mat_2 = Pointer(self.context, 0, ZString)
		self.stairs_mat_1 = Pointer(self.context, 0, ZString)
		self.stairs_mat_2 = Pointer(self.context, 0, ZString)
		self.mat_data = ArrayPointer(self.context, self.num_data, PathMaterial._import_path_map["generated.formats.path.compounds.PathMaterialData"])
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.path_sub_type = 0
		self.num_data = 0
		self.elevated_mat = Pointer(self.context, 0, ZString)
		self.elevated_mat_valid = Pointer(self.context, 0, ZString)
		self.elevated_mat_invalid = Pointer(self.context, 0, ZString)
		self.terrain_mat = Pointer(self.context, 0, ZString)
		self.terrain_mat_valid = Pointer(self.context, 0, ZString)
		self.terrain_mat_invalid = Pointer(self.context, 0, ZString)
		self.underside_mat_1 = Pointer(self.context, 0, ZString)
		self.underside_mat_2 = Pointer(self.context, 0, ZString)
		self.stairs_mat_1 = Pointer(self.context, 0, ZString)
		self.stairs_mat_2 = Pointer(self.context, 0, ZString)
		self.mat_data = ArrayPointer(self.context, self.num_data, PathMaterial._import_path_map["generated.formats.path.compounds.PathMaterialData"])

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.elevated_mat = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.elevated_mat_valid = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.elevated_mat_invalid = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.terrain_mat = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.terrain_mat_valid = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.terrain_mat_invalid = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.underside_mat_1 = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.underside_mat_2 = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.stairs_mat_1 = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.stairs_mat_2 = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.path_sub_type = Uint64.from_stream(stream, instance.context, 0, None)
		instance.mat_data = ArrayPointer.from_stream(stream, instance.context, instance.num_data, PathMaterial._import_path_map["generated.formats.path.compounds.PathMaterialData"])
		instance.num_data = Uint64.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.elevated_mat, int):
			instance.elevated_mat.arg = 0
		if not isinstance(instance.elevated_mat_valid, int):
			instance.elevated_mat_valid.arg = 0
		if not isinstance(instance.elevated_mat_invalid, int):
			instance.elevated_mat_invalid.arg = 0
		if not isinstance(instance.terrain_mat, int):
			instance.terrain_mat.arg = 0
		if not isinstance(instance.terrain_mat_valid, int):
			instance.terrain_mat_valid.arg = 0
		if not isinstance(instance.terrain_mat_invalid, int):
			instance.terrain_mat_invalid.arg = 0
		if not isinstance(instance.underside_mat_1, int):
			instance.underside_mat_1.arg = 0
		if not isinstance(instance.underside_mat_2, int):
			instance.underside_mat_2.arg = 0
		if not isinstance(instance.stairs_mat_1, int):
			instance.stairs_mat_1.arg = 0
		if not isinstance(instance.stairs_mat_2, int):
			instance.stairs_mat_2.arg = 0
		if not isinstance(instance.mat_data, int):
			instance.mat_data.arg = instance.num_data

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.elevated_mat)
		Pointer.to_stream(stream, instance.elevated_mat_valid)
		Pointer.to_stream(stream, instance.elevated_mat_invalid)
		Pointer.to_stream(stream, instance.terrain_mat)
		Pointer.to_stream(stream, instance.terrain_mat_valid)
		Pointer.to_stream(stream, instance.terrain_mat_invalid)
		Pointer.to_stream(stream, instance.underside_mat_1)
		Pointer.to_stream(stream, instance.underside_mat_2)
		Pointer.to_stream(stream, instance.stairs_mat_1)
		Pointer.to_stream(stream, instance.stairs_mat_2)
		Uint64.to_stream(stream, instance.path_sub_type)
		ArrayPointer.to_stream(stream, instance.mat_data)
		Uint64.to_stream(stream, instance.num_data)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'elevated_mat', Pointer, (0, ZString), (False, None)
		yield 'elevated_mat_valid', Pointer, (0, ZString), (False, None)
		yield 'elevated_mat_invalid', Pointer, (0, ZString), (False, None)
		yield 'terrain_mat', Pointer, (0, ZString), (False, None)
		yield 'terrain_mat_valid', Pointer, (0, ZString), (False, None)
		yield 'terrain_mat_invalid', Pointer, (0, ZString), (False, None)
		yield 'underside_mat_1', Pointer, (0, ZString), (False, None)
		yield 'underside_mat_2', Pointer, (0, ZString), (False, None)
		yield 'stairs_mat_1', Pointer, (0, ZString), (False, None)
		yield 'stairs_mat_2', Pointer, (0, ZString), (False, None)
		yield 'path_sub_type', Uint64, (0, None), (False, None)
		yield 'mat_data', ArrayPointer, (instance.num_data, PathMaterial._import_path_map["generated.formats.path.compounds.PathMaterialData"]), (False, None)
		yield 'num_data', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'PathMaterial [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
