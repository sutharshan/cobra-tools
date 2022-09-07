from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class AxisValue(MemStruct):

	__name__ = 'AxisValue'

	_import_path = 'generated.formats.logicalcontrols.compounds.AxisValue'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.u_0 = 0
		self.u_1 = 0
		self.u_2 = 0
		self.u_3 = 0
		self.u_4 = 0
		self.axis_name = Pointer(self.context, 0, ZString)
		self.value_name = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.u_0 = 0
		self.u_1 = 0
		self.u_2 = 0
		self.u_3 = 0
		self.u_4 = 0
		self.axis_name = Pointer(self.context, 0, ZString)
		self.value_name = Pointer(self.context, 0, ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.axis_name = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.u_0 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.u_1 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.u_2 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.value_name = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.u_3 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.u_4 = Uint64.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.axis_name, int):
			instance.axis_name.arg = 0
		if not isinstance(instance.value_name, int):
			instance.value_name.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.axis_name)
		Uint64.to_stream(stream, instance.u_0)
		Uint64.to_stream(stream, instance.u_1)
		Uint64.to_stream(stream, instance.u_2)
		Pointer.to_stream(stream, instance.value_name)
		Uint64.to_stream(stream, instance.u_3)
		Uint64.to_stream(stream, instance.u_4)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'axis_name', Pointer, (0, ZString), (False, None)
		yield 'u_0', Uint64, (0, None), (False, None)
		yield 'u_1', Uint64, (0, None), (False, None)
		yield 'u_2', Uint64, (0, None), (False, None)
		yield 'value_name', Pointer, (0, ZString), (False, None)
		yield 'u_3', Uint64, (0, None), (False, None)
		yield 'u_4', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'AxisValue [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
