from generated.base_struct import BaseStruct


class Empty(BaseStruct):

	"""
	Grabs 00 bytes only
	"""

	__name__ = 'Empty'

	_import_path = 'generated.formats.manis.compounds.Empty'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		pass

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		pass

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		pass

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)

	def get_info_str(self, indent=0):
		return f'Empty [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
