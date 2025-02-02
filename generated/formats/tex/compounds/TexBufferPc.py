from generated.formats.base.basic import Ushort
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class TexBufferPc(MemStruct):

	"""
	The different tex buffers contain the smallest mip
	"""

	__name__ = 'TexBufferPc'

	_import_key = 'tex.compounds.TexBufferPc'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.width = 0
		self.height = 0

		# may be depth
		self.num_tiles = 0

		# the first ie. biggest levels are clipped off
		self.num_mips = 0
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('width', Ushort, (0, None), (False, None), None),
		('height', Ushort, (0, None), (False, None), None),
		('num_tiles', Ushort, (0, None), (False, None), True),
		('num_mips', Ushort, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'width', Ushort, (0, None), (False, None)
		yield 'height', Ushort, (0, None), (False, None)
		if instance.context.version >= 18:
			yield 'num_tiles', Ushort, (0, None), (False, None)
		yield 'num_mips', Ushort, (0, None), (False, None)
