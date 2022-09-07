from generated.base_struct import BaseStruct
from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Uint
from generated.formats.bnk.compounds.AkMediaInformation import AkMediaInformation


class AkBankSourceData(BaseStruct):

	__name__ = 'AkBankSourceData'

	_import_path = 'generated.formats.bnk.compounds.AkBankSourceData'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.ul_plugin_i_d = 0
		self.stream_type = 0
		self.ak_media_information = AkMediaInformation(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.ul_plugin_i_d = 0
		self.stream_type = 0
		self.ak_media_information = AkMediaInformation(self.context, 0, None)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.ul_plugin_i_d = Uint.from_stream(stream, instance.context, 0, None)
		instance.stream_type = Ubyte.from_stream(stream, instance.context, 0, None)
		instance.ak_media_information = AkMediaInformation.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.ul_plugin_i_d)
		Ubyte.to_stream(stream, instance.stream_type)
		AkMediaInformation.to_stream(stream, instance.ak_media_information)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'ul_plugin_i_d', Uint, (0, None), (False, None)
		yield 'stream_type', Ubyte, (0, None), (False, None)
		yield 'ak_media_information', AkMediaInformation, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'AkBankSourceData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
