from generated.formats.base.enums import UbyteEnum


class DdsType(UbyteEnum):

	"""
	maps the OVL's dds type to name of compression format
	"""

	__name__ = 'DdsType'
	UNKNOWN = 0
	R32G32B32A32_FLOAT = 1
	R32G32B32A32_UINT = 2
	R32G32B32A32_SINT = 3
	R32G32B32A32_UNORM = 4
	R32G32B32A32_SNORM = 5
	R32G32B32_FLOAT = 6
	R32G32B32_UINT = 7
	R32G32B32_SINT = 8
	R32G32B32_UNORM = 9
	R32G32B32_SNORM = 10
	R32G32_FLOAT = 11
	R32G32_UINT = 12
	R32G32_SINT = 13
	R32G32_UNORM = 14
	R32G32_SNORM = 15
	R32_FLOAT = 16
	R32_UINT = 17
	R32_SINT = 18
	R32_UNORM = 19
	R32_SNORM = 20
	R11G11B10_FLOAT = 21
	R11G11B10_UINT = 22
	R11G11B10_SINT = 23
	R11G11B10_UNORM = 24
	R11G11B10_SNORM = 25
	R10G10B10FA2_UNORM = 26
	R10G10B10A2_UINT = 27
	R10G10B10A2_UNORM = 28
	R10G10B10X2_UINT = 29
	R10G10B10X2_SINT = 30
	R10G10B10X2_UNORM = 31
	R10G10B10X2_SNORM = 32
	R8G8B8A8_UINT = 33
	R8G8B8A8_SINT = 34
	R8G8B8A8_UNORM = 35
	R8G8B8A8_SNORM = 36
	R8G8B8A8_UNORM_SRGB = 37
	R16G16B16A16_FLOAT = 38
	R16G16B16A16_UINT = 39
	R16G16B16A16_SINT = 40
	R16G16B16A16_UNORM = 41
	R16G16B16A16_SNORM = 42
	R16G16_FLOAT = 43
	R16G16_UINT = 44
	R16G16_SINT = 45
	R16G16_UNORM = 46
	R16G16_SNORM = 47
	R16_FLOAT = 48
	R16_UINT = 49
	R16_SINT = 50
	R16_UNORM = 51
	R16_SNORM = 52
	R8G8_UINT = 53
	R8G8_SINT = 54
	R8G8_UNORM = 55
	R8G8_SNORM = 56
	R8_UINT = 57
	R8_SINT = 58
	R8_UNORM = 59
	R8_SNORM = 60
	B10G10R10A2_UNORM = 61
	B10G10R10X2_UNORM = 62
	B8G8R8A8_UNORM = 63
	B8G8R8A8_UNORM_SRGB = 64
	B8G8R8X8_UNORM = 65
	B8G8_UNORM = 66
	B8_UNORM = 67
	D32FS8_UINT = 68
	D32_UNORM = 69
	D32_FLOAT = 70
	D24UNS8_UINT = 71
	D24FS8_UINT = 72
	D24UNX8 = 73
	D24FX8 = 74
	D16_UNORM = 75
	D16_FLOAT = 76
	A8_UNORM = 77
	BC1_UNORM = 78
	BC1_UNORM_SRGB = 79
	BC2_UNORM = 80
	BC2_UNORM_SRGB = 81
	BC3_UNORM = 82
	BC3_UNORM_SRGB = 83
	BC4_UNORM = 84
	BC4_SNORM = 85
	BC5_UNORM = 86
	BC5_SNORM = 87
	BC6H_UF16 = 88
	BC6H_SF16 = 89
	BC7_UNORM = 90
	BC7_UNORM_SRGB = 91
	FMASK_R8_UINT = 92
	FMASK_R16_UINT = 93
	FMASK_R32_UINT = 94
	FMASK_R32G32_UINT = 95
	X32_TYPELESS_G8X24_UINT = 96
	X24_TYPELESS_G8_UINT = 97
