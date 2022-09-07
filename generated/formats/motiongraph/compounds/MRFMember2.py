from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class MRFMember2(MemStruct):

	"""
	72 bytes
	only used if transition is in 'id'
	"""

	__name__ = 'MRFMember2'

	_import_path = 'generated.formats.motiongraph.compounds.MRFMember2'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count_0 = 0
		self.count_1 = 0
		self.count_2 = 0
		self.count_3 = 0
		self.count_4 = 0
		self.count_5 = 0
		self.count_6 = 0
		self.transition = Pointer(self.context, 0, MRFMember2._import_path_map["generated.formats.motiongraph.compounds.Transition"])
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
		self.count_5 = 0
		self.count_6 = 0
		self.transition = Pointer(self.context, 0, MRFMember2._import_path_map["generated.formats.motiongraph.compounds.Transition"])
		self.id = Pointer(self.context, 0, ZString)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.transition = Pointer.from_stream(stream, instance.context, 0, MRFMember2._import_path_map["generated.formats.motiongraph.compounds.Transition"])
		instance.count_0 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_1 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_2 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_3 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_4 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_5 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.count_6 = Uint64.from_stream(stream, instance.context, 0, None)
		instance.id = Pointer.from_stream(stream, instance.context, 0, ZString)
		if not isinstance(instance.transition, int):
			instance.transition.arg = 0
		if not isinstance(instance.id, int):
			instance.id.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.transition)
		Uint64.to_stream(stream, instance.count_0)
		Uint64.to_stream(stream, instance.count_1)
		Uint64.to_stream(stream, instance.count_2)
		Uint64.to_stream(stream, instance.count_3)
		Uint64.to_stream(stream, instance.count_4)
		Uint64.to_stream(stream, instance.count_5)
		Uint64.to_stream(stream, instance.count_6)
		Pointer.to_stream(stream, instance.id)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'transition', Pointer, (0, MRFMember2._import_path_map["generated.formats.motiongraph.compounds.Transition"]), (False, None)
		yield 'count_0', Uint64, (0, None), (False, None)
		yield 'count_1', Uint64, (0, None), (False, None)
		yield 'count_2', Uint64, (0, None), (False, None)
		yield 'count_3', Uint64, (0, None), (False, None)
		yield 'count_4', Uint64, (0, None), (False, None)
		yield 'count_5', Uint64, (0, None), (False, None)
		yield 'count_6', Uint64, (0, None), (False, None)
		yield 'id', Pointer, (0, ZString), (False, None)

	def get_info_str(self, indent=0):
		return f'MRFMember2 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
