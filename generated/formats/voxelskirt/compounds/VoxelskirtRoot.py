from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.voxelskirt.compounds.DataSlot import DataSlot


class VoxelskirtRoot(MemStruct):

	"""
	# size varies according to game
	JWE2 - 120 bytes
	"""

	__name__ = 'VoxelskirtRoot'

	_import_path = 'generated.formats.voxelskirt.compounds.VoxelskirtRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.zero = 0

		# total size of buffer data
		self.data_size = 0
		self.x = 0
		self.y = 0
		self.scale = 0.0
		self.padding = 0.0

		# zero, for PC only
		self.zero_pc = 0

		# x*y*4, for PC only
		self.height_array_size_pc = 0
		self.layers = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Layer"])

		# entries of 40 bytes
		self.sizes = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Size"])

		# counts the -1 structs; entries of 32 bytes
		self.positions = DataSlot(self.context, 0, None)
		self.materials = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Material"])
		self.names = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Name"])
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.zero = 0
		self.data_size = 0
		self.x = 0
		self.y = 0
		self.scale = 0.0
		self.padding = 0.0
		if self.context.version == 18:
			self.zero_pc = 0
			self.height_array_size_pc = 0
		if not (self.context.version == 18):
			self.layers = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Layer"])
			self.sizes = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Size"])
		self.positions = DataSlot(self.context, 0, None)
		self.materials = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Material"])
		self.names = DataSlot(self.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Name"])

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.zero = Uint64.from_stream(stream, instance.context, 0, None)
		instance.data_size = Uint64.from_stream(stream, instance.context, 0, None)
		instance.x = Uint64.from_stream(stream, instance.context, 0, None)
		instance.y = Uint64.from_stream(stream, instance.context, 0, None)
		instance.scale = Float.from_stream(stream, instance.context, 0, None)
		instance.padding = Float.from_stream(stream, instance.context, 0, None)
		if instance.context.version == 18:
			instance.zero_pc = Uint64.from_stream(stream, instance.context, 0, None)
			instance.height_array_size_pc = Uint64.from_stream(stream, instance.context, 0, None)
		if not (instance.context.version == 18):
			instance.layers = DataSlot.from_stream(stream, instance.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Layer"])
			instance.sizes = DataSlot.from_stream(stream, instance.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Size"])
		instance.positions = DataSlot.from_stream(stream, instance.context, 0, None)
		instance.materials = DataSlot.from_stream(stream, instance.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Material"])
		instance.names = DataSlot.from_stream(stream, instance.context, 0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Name"])

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint64.to_stream(stream, instance.zero)
		Uint64.to_stream(stream, instance.data_size)
		Uint64.to_stream(stream, instance.x)
		Uint64.to_stream(stream, instance.y)
		Float.to_stream(stream, instance.scale)
		Float.to_stream(stream, instance.padding)
		if instance.context.version == 18:
			Uint64.to_stream(stream, instance.zero_pc)
			Uint64.to_stream(stream, instance.height_array_size_pc)
		if not (instance.context.version == 18):
			DataSlot.to_stream(stream, instance.layers)
			DataSlot.to_stream(stream, instance.sizes)
		DataSlot.to_stream(stream, instance.positions)
		DataSlot.to_stream(stream, instance.materials)
		DataSlot.to_stream(stream, instance.names)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'zero', Uint64, (0, None), (False, None)
		yield 'data_size', Uint64, (0, None), (False, None)
		yield 'x', Uint64, (0, None), (False, None)
		yield 'y', Uint64, (0, None), (False, None)
		yield 'scale', Float, (0, None), (False, None)
		yield 'padding', Float, (0, None), (False, None)
		if instance.context.version == 18:
			yield 'zero_pc', Uint64, (0, None), (False, None)
			yield 'height_array_size_pc', Uint64, (0, None), (False, None)
		if not (instance.context.version == 18):
			yield 'layers', DataSlot, (0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Layer"]), (False, None)
			yield 'sizes', DataSlot, (0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Size"]), (False, None)
		yield 'positions', DataSlot, (0, None), (False, None)
		yield 'materials', DataSlot, (0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Material"]), (False, None)
		yield 'names', DataSlot, (0, VoxelskirtRoot._import_path_map["generated.formats.voxelskirt.compounds.Name"]), (False, None)

	def get_info_str(self, indent=0):
		return f'VoxelskirtRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* zero = {self.fmt_member(self.zero, indent+1)}'
		s += f'\n	* data_size = {self.fmt_member(self.data_size, indent+1)}'
		s += f'\n	* x = {self.fmt_member(self.x, indent+1)}'
		s += f'\n	* y = {self.fmt_member(self.y, indent+1)}'
		s += f'\n	* scale = {self.fmt_member(self.scale, indent+1)}'
		s += f'\n	* padding = {self.fmt_member(self.padding, indent+1)}'
		s += f'\n	* zero_pc = {self.fmt_member(self.zero_pc, indent+1)}'
		s += f'\n	* height_array_size_pc = {self.fmt_member(self.height_array_size_pc, indent+1)}'
		s += f'\n	* layers = {self.fmt_member(self.layers, indent+1)}'
		s += f'\n	* sizes = {self.fmt_member(self.sizes, indent+1)}'
		s += f'\n	* positions = {self.fmt_member(self.positions, indent+1)}'
		s += f'\n	* materials = {self.fmt_member(self.materials, indent+1)}'
		s += f'\n	* names = {self.fmt_member(self.names, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
