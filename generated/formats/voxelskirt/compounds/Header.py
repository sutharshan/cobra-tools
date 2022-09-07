from generated.formats.ovl_base.compounds.GenericHeader import GenericHeader
from generated.formats.voxelskirt.compounds.VoxelskirtRoot import VoxelskirtRoot


class Header(GenericHeader):

	"""
	Found at the beginning of every OVL file
	"""

	__name__ = 'Header'

	_import_path = 'generated.formats.voxelskirt.compounds.Header'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.info = VoxelskirtRoot(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.info = VoxelskirtRoot(self.context, 0, None)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.info = VoxelskirtRoot.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		VoxelskirtRoot.to_stream(stream, instance.info)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'info', VoxelskirtRoot, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Header [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
