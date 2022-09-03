from generated.base_enum import BaseEnum
from generated.formats.base.basic import Uint


class Compression(BaseEnum):

	__name__ = 'Compression'
	_storage = Uint

	NONE = 0
	ZLIB = 1
	OODLE = 4
