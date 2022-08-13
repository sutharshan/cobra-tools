from generated.formats.curve.compounds.CurveRoot import CurveRoot
from modules.formats.BaseFormat import MemStructLoader


class CurveLoader(MemStructLoader):
	extension = ".curve"
	target_class = CurveRoot
