from generated.formats.wmeta.compounds.WmetasbRoot import WmetasbRoot
from modules.formats.BaseFormat import MemStructLoader


class WmetaLoader(MemStructLoader):
	target_class = WmetasbRoot
	extension = ".wmetasb"

