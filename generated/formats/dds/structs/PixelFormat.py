from generated.base_struct import BaseStruct
from generated.formats.dds.basic import Uint
from generated.formats.dds.bitstructs.PixelFormatFlags import PixelFormatFlags
from generated.formats.dds.enums.FourCC import FourCC


class PixelFormat(BaseStruct):

	__name__ = 'PixelFormat'

	_import_key = 'dds.structs.PixelFormat'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Always 32.
		self.size = 32

		# Non-zero for DX9, zero for DX10.
		self.flags = PixelFormatFlags(self.context, 0, None)

		# Determines compression type. Zero means no compression.
		self.four_c_c = FourCC(self.context, 0, None)

		# For non-compressed types, this is either 24 or 32 depending on whether there is an alpha channel. For compressed types, this describes the number of bits per block, which can be either 256 or 512.
		self.bit_count = 0

		# For non-compressed types, this determines the red mask. Usually 0x00FF0000. Is zero for compressed textures.
		self.r_mask = 0

		# For non-compressed types, this determines
		# the green mask. Usually 0x0000FF00. Is zero for compressed textures.
		self.g_mask = 0

		# For non-compressed types, this determines
		# the blue mask. Usually 0x00FF0000. Is zero for compressed textures.
		self.b_mask = 0

		# For non-compressed types, this determines
		# the alpha mask. Usually 0x00000000 if there is no alpha channel and 0xFF000000 if there is an alpha channel. Is zero for compressed textures.
		self.a_mask = 0
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('size', Uint, (0, None), (False, 32), None),
		('flags', PixelFormatFlags, (0, None), (False, None), None),
		('four_c_c', FourCC, (0, None), (False, None), None),
		('bit_count', Uint, (0, None), (False, None), None),
		('r_mask', Uint, (0, None), (False, None), None),
		('g_mask', Uint, (0, None), (False, None), None),
		('b_mask', Uint, (0, None), (False, None), None),
		('a_mask', Uint, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'size', Uint, (0, None), (False, 32)
		yield 'flags', PixelFormatFlags, (0, None), (False, None)
		yield 'four_c_c', FourCC, (0, None), (False, None)
		yield 'bit_count', Uint, (0, None), (False, None)
		yield 'r_mask', Uint, (0, None), (False, None)
		yield 'g_mask', Uint, (0, None), (False, None)
		yield 'b_mask', Uint, (0, None), (False, None)
		yield 'a_mask', Uint, (0, None), (False, None)
