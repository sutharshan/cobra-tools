from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Vector3(MemStruct):

	"""
	16 bytes in log
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		self.ioptional = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		self.ioptional = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.x = Float.from_stream(stream, instance.context, 0, None)
		instance.y = Float.from_stream(stream, instance.context, 0, None)
		instance.z = Float.from_stream(stream, instance.context, 0, None)
		instance.ioptional = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Float.to_stream(stream, instance.x)
		Float.to_stream(stream, instance.y)
		Float.to_stream(stream, instance.z)
		Uint.to_stream(stream, instance.ioptional)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'x', Float, (0, None)
		yield 'y', Float, (0, None)
		yield 'z', Float, (0, None)
		yield 'ioptional', Uint, (0, None)

	def get_info_str(self, indent=0):
		return f'Vector3 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* x = {self.fmt_member(self.x, indent+1)}'
		s += f'\n	* y = {self.fmt_member(self.y, indent+1)}'
		s += f'\n	* z = {self.fmt_member(self.z, indent+1)}'
		s += f'\n	* ioptional = {self.fmt_member(self.ioptional, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s