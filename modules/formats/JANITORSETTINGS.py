from generated.formats.janitorsettings.compounds.JanitorSettingsRoot import JanitorSettingsRoot
from modules.formats.BaseFormat import MemStructLoader


class Janitorsettings(MemStructLoader):
	target_class = JanitorSettingsRoot
	extension = ".janitorsettings"
