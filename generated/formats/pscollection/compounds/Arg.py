from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Arg(MemStruct):

	__name__ = 'Arg'

	_import_path = 'generated.formats.pscollection.compounds.Arg'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.u_0 = 0
		self.arg_type = 0

		# one-based index
		self.arg_index = 0
		self.u_1 = 0
		self.u_2 = 0
		self.u_3 = 0
		self.u_4 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.u_0 = 0
		self.arg_type = 0
		self.arg_index = 0
		self.u_1 = 0
		self.u_2 = 0
		self.u_3 = 0
		self.u_4 = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.u_0 = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.arg_type = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.arg_index = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.u_1 = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.u_2 = Uint.from_stream(stream, instance.context, 0, None)
		instance.u_3 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.u_4 = Uint64.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Ubyte.to_stream(stream, instance.u_0)
		Ubyte.to_stream(stream, instance.arg_type)
		Ubyte.to_stream(stream, instance.arg_index)
		Ubyte.to_stream(stream, instance.u_1)
		Uint.to_stream(stream, instance.u_2)
		Uint64.to_stream(stream, instance.u_3)
		Uint64.to_stream(stream, instance.u_4)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'u_0', Ubyte, (0, None), (False, None)
		yield 'arg_type', Ubyte, (0, None), (False, None)
		yield 'arg_index', Ubyte, (0, None), (False, None)
		yield 'u_1', Ubyte, (0, None), (False, None)
		yield 'u_2', Uint, (0, None), (False, None)
		yield 'u_3', Uint64, (0, None), (False, None)
		yield 'u_4', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Arg [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
