from generated.base_struct import BaseStruct
from generated.formats.base.basic import Double
from generated.formats.base.basic import Uint


class AkTrackSrcInfo(BaseStruct):

	__name__ = 'AkTrackSrcInfo'

	_import_path = 'generated.formats.bnk.compounds.AkTrackSrcInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.track_i_d = 0
		self.source_i_d = 0
		self.event_i_d = 0
		self.f_play_at = 0.0
		self.f_begin_trim_offset = 0.0
		self.f_end_trim_offset = 0.0
		self.f_src_duration = 0.0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.track_i_d = 0
		self.source_i_d = 0
		self.event_i_d = 0
		self.f_play_at = 0.0
		self.f_begin_trim_offset = 0.0
		self.f_end_trim_offset = 0.0
		self.f_src_duration = 0.0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.track_i_d = Uint.from_stream(stream, instance.context, 0, None)
		instance.source_i_d = Uint.from_stream(stream, instance.context, 0, None)
		instance.event_i_d = Uint.from_stream(stream, instance.context, 0, None)
		instance.f_play_at = Double.from_stream(stream, instance.context, 0, None)
		instance.f_begin_trim_offset = Double.from_stream(stream, instance.context, 0, None)
		instance.f_end_trim_offset = Double.from_stream(stream, instance.context, 0, None)
		instance.f_src_duration = Double.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.track_i_d)
		Uint.to_stream(stream, instance.source_i_d)
		Uint.to_stream(stream, instance.event_i_d)
		Double.to_stream(stream, instance.f_play_at)
		Double.to_stream(stream, instance.f_begin_trim_offset)
		Double.to_stream(stream, instance.f_end_trim_offset)
		Double.to_stream(stream, instance.f_src_duration)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'track_i_d', Uint, (0, None), (False, None)
		yield 'source_i_d', Uint, (0, None), (False, None)
		yield 'event_i_d', Uint, (0, None), (False, None)
		yield 'f_play_at', Double, (0, None), (False, None)
		yield 'f_begin_trim_offset', Double, (0, None), (False, None)
		yield 'f_end_trim_offset', Double, (0, None), (False, None)
		yield 'f_src_duration', Double, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'AkTrackSrcInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
