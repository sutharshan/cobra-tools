from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class MRFMember1(MemStruct):

	"""
	72 bytes, is like ThirdFrag, but different templates
	"""

	__name__ = 'MRFMember1'

	_import_path = 'generated.formats.motiongraph.compounds.MRFMember1'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count_0 = 0
		self.count_1 = 0
		self.count_2 = 0
		self.count_3 = 0
		self.count_4 = 0
		self.lua_method = Pointer(self.context, 0, ZString)
		self.ptr_1 = Pointer(self.context, 0, None)
		self.ptr_2 = Pointer(self.context, 0, None)
		self.id = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.count_0 = 0
		self.count_1 = 0
		self.count_2 = 0
		self.count_3 = 0
		self.count_4 = 0
		self.lua_method = Pointer(self.context, 0, ZString)
		self.ptr_1 = Pointer(self.context, 0, None)
		self.ptr_2 = Pointer(self.context, 0, None)
		self.id = Pointer(self.context, 0, ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.lua_method = Pointer.from_stream(stream, instance.context, 0, ZString)
		instance.count_0 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_1 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.ptr_1 = Pointer.from_stream(stream, instance.context, 0, None)
		instance.count_2 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_3 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.ptr_2 = Pointer.from_stream(stream, instance.context, 0, None)
		instance.count_4 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.id = Pointer.from_stream(stream, instance.context, 0, ZString)
		if not isinstance(instance.lua_method, int):
			instance.lua_method.arg = 0
		if not isinstance(instance.ptr_1, int):
			instance.ptr_1.arg = 0
		if not isinstance(instance.ptr_2, int):
			instance.ptr_2.arg = 0
		if not isinstance(instance.id, int):
			instance.id.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.lua_method)
		Uint64.to_stream(stream, instance.count_0)
		Uint64.to_stream(stream, instance.count_1)
		Pointer.to_stream(stream, instance.ptr_1)
		Uint64.to_stream(stream, instance.count_2)
		Uint64.to_stream(stream, instance.count_3)
		Pointer.to_stream(stream, instance.ptr_2)
		Uint64.to_stream(stream, instance.count_4)
		Pointer.to_stream(stream, instance.id)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'lua_method', Pointer, (0, ZString), (False, None)
		yield 'count_0', Uint64, (0, None), (False, None)
		yield 'count_1', Uint64, (0, None), (False, None)
		yield 'ptr_1', Pointer, (0, None), (False, None)
		yield 'count_2', Uint64, (0, None), (False, None)
		yield 'count_3', Uint64, (0, None), (False, None)
		yield 'ptr_2', Pointer, (0, None), (False, None)
		yield 'count_4', Uint64, (0, None), (False, None)
		yield 'id', Pointer, (0, ZString), (False, None)

	def get_info_str(self, indent=0):
		return f'MRFMember1 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
