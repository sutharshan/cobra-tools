from generated.formats.base.basic import fmt_member
from generated.formats.base.basic import Ushort
from generated.struct import StructBase


class Object(StructBase):

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default)

		# index into material name array
		self.material_index = 0

		# index into mesh array
		self.mesh_index = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.material_index = 0
		self.mesh_index = 0

	def read(self, stream):
		self.io_start = stream.tell()
		self.read_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		self.write_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.material_index = stream.read_ushort()
		instance.mesh_index = stream.read_ushort()

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_ushort(instance.material_index)
		stream.write_ushort(instance.mesh_index)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('material_index', Ushort, (0, None))
		yield ('mesh_index', Ushort, (0, None))

	def get_info_str(self, indent=0):
		return f'Object [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* material_index = {fmt_member(self.material_index, indent+1)}'
		s += f'\n	* mesh_index = {fmt_member(self.mesh_index, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
