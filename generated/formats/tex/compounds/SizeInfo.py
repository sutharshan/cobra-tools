import numpy
from generated.array import Array
from generated.formats.base.basic import Ubyte
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.tex.compounds.SizeInfoRaw import SizeInfoRaw


class SizeInfo(MemStruct):

	__name__ = 'SizeInfo'

	_import_key = 'tex.compounds.SizeInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.data = SizeInfoRaw(self.context, 0, None)
		self.padding = Array(self.context, 0, None, (0,), Ubyte)
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('data', SizeInfoRaw, (0, None), (False, None), None),
		('padding', Array, (0, None, (None,), Ubyte), (False, None), True),
		('padding', Array, (0, None, (None,), Ubyte), (False, None), True),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'data', SizeInfoRaw, (0, None), (False, None)
		if ((not instance.context.user_version.use_djb) and (instance.context.version == 20)) or (((not instance.context.user_version.use_djb) and (instance.context.version >= 19)) or (instance.context.user_version.use_djb and (instance.context.version == 20))):
			yield 'padding', Array, (0, None, (320 - instance.data.io_size,), Ubyte), (False, None)
		if instance.context.user_version.use_djb and (instance.context.version == 19):
			yield 'padding', Array, (0, None, (384 - instance.data.io_size,), Ubyte), (False, None)
