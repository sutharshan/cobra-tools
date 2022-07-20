from source.formats.base.basic import fmt_member
from generated.formats.dds.enum import UintEnum


class DxgiFormat(UintEnum):

	"""
	An unsigned 32-bit integer, describing the DxgiFormat.
	"""
	UNKNOWN = 0
	R_32_G_32_B_32_A_32_TYPELESS = 1
	R_32_G_32_B_32_A_32_FLOAT = 2
	R_32_G_32_B_32_A_32_UINT = 3
	R_32_G_32_B_32_A_32_SINT = 4
	R_32_G_32_B_32_TYPELESS = 5
	R_32_G_32_B_32_FLOAT = 6
	R_32_G_32_B_32_UINT = 7
	R_32_G_32_B_32_SINT = 8
	R_16_G_16_B_16_A_16_TYPELESS = 9
	R_16_G_16_B_16_A_16_FLOAT = 10
	R_16_G_16_B_16_A_16_UNORM = 11
	R_16_G_16_B_16_A_16_UINT = 12
	R_16_G_16_B_16_A_16_SNORM = 13
	R_16_G_16_B_16_A_16_SINT = 14
	R_32_G_32_TYPELESS = 15
	R_32_G_32_FLOAT = 16
	R_32_G_32_UINT = 17
	R_32_G_32_SINT = 18
	R_32_G_8_X_24_TYPELESS = 19
	D_32_FLOAT_S_8_X_24_UINT = 20
	R_32_FLOAT_X_8_X_24_TYPELESS = 21
	X_32_TYPELESS_G_8_X_24_UINT = 22
	R_10_G_10_B_10_A_2_TYPELESS = 23
	R_10_G_10_B_10_A_2_UNORM = 24
	R_10_G_10_B_10_A_2_UINT = 25
	R_11_G_11_B_10_FLOAT = 26
	R_8_G_8_B_8_A_8_TYPELESS = 27
	R_8_G_8_B_8_A_8_UNORM = 28
	R_8_G_8_B_8_A_8_UNORM_SRGB = 29
	R_8_G_8_B_8_A_8_UINT = 30
	R_8_G_8_B_8_A_8_SNORM = 31
	R_8_G_8_B_8_A_8_SINT = 32
	R_16_G_16_TYPELESS = 33
	R_16_G_16_FLOAT = 34
	R_16_G_16_UNORM = 35
	R_16_G_16_UINT = 36
	R_16_G_16_SNORM = 37
	R_16_G_16_SINT = 38
	R_32_TYPELESS = 39
	D_32_FLOAT = 40
	R_32_FLOAT = 41
	R_32_UINT = 42
	R_32_SINT = 43
	R_24_G_8_TYPELESS = 44
	D_24_UNORM_S_8_UINT = 45
	R_24_UNORM_X_8_TYPELESS = 46
	X_24_TYPELESS_G_8_UINT = 47
	R_8_G_8_TYPELESS = 48
	R_8_G_8_UNORM = 49
	R_8_G_8_UINT = 50
	R_8_G_8_SNORM = 51
	R_8_G_8_SINT = 52
	R_16_TYPELESS = 53
	R_16_FLOAT = 54
	D_16_UNORM = 55
	R_16_UNORM = 56
	R_16_UINT = 57
	R_16_SNORM = 58
	R_16_SINT = 59
	R_8_TYPELESS = 60
	R_8_UNORM = 61
	R_8_UINT = 62
	R_8_SNORM = 63
	R_8_SINT = 64
	A_8_UNORM = 65
	R_1_UNORM = 66
	R_9_G_9_B_9_E_5_SHAREDEXP = 67
	R_8_G_8_B_8_G_8_UNORM = 68
	G_8_R_8_G_8_B_8_UNORM = 69
	BC_1_TYPELESS = 70
	BC_1_UNORM = 71
	BC_1_UNORM_SRGB = 72
	BC_2_TYPELESS = 73
	BC_2_UNORM = 74
	BC_2_UNORM_SRGB = 75
	BC_3_TYPELESS = 76
	BC_3_UNORM = 77
	BC_3_UNORM_SRGB = 78
	BC_4_TYPELESS = 79
	BC_4_UNORM = 80
	BC_4_SNORM = 81
	BC_5_TYPELESS = 82
	BC_5_UNORM = 83
	BC_5_SNORM = 84
	B_5_G_6_R_5_UNORM = 85
	B_5_G_5_R_5_A_1_UNORM = 86
	B_8_G_8_R_8_A_8_UNORM = 87
	B_8_G_8_R_8_X_8_UNORM = 88
	R_10_G_10_B_10_XR_BIAS_A_2_UNORM = 89
	B_8_G_8_R_8_A_8_TYPELESS = 90
	B_8_G_8_R_8_A_8_UNORM_SRGB = 91
	B_8_G_8_R_8_X_8_TYPELESS = 92
	B_8_G_8_R_8_X_8_UNORM_SRGB = 93
	BC_6_H_TYPELESS = 94
	BC_6_H_UF_16 = 95
	BC_6_H_SF_16 = 96
	BC_7_TYPELESS = 97
	BC_7_UNORM = 98
	BC_7_UNORM_SRGB = 99
	AYUV = 100
	Y_410 = 101
	Y_416 = 102
	NV_12 = 103
	P_010 = 104
	P_016 = 105
	YUY_2 = 107
	Y_210 = 108
	Y_216 = 109
	NV_11 = 110
	AI_44 = 111
	IA_44 = 112
	P_8 = 113
	A_8_P_8 = 114
	B_4_G_4_R_4_A_4_UNORM = 115
	P_208 = 130
	V_208 = 131
	V_408 = 132
	FORCE_UINT = 0xffffffff
