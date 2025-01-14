from generated.formats.bnk.compounds.AuxFileContainer import AuxFileContainer
from generated.formats.bnk.compounds.BnkFileContainer import BnkFileContainer
from generated.formats.ovl_base import OvlContext
from generated.io import IoFile
import os


class BnkFile(BnkFileContainer, IoFile):

	def __init__(self):
		super().__init__(OvlContext())

	def load(self, filepath):
		with open(filepath, "rb") as stream:
			self.read_fields(stream, self)

	def save(self, filepath):
		self.old_size = os.path.getsize(filepath)
		with open(filepath, "wb") as stream:
			self.write_fields(stream, self)


class AuxFile(AuxFileContainer, IoFile):

	def __init__(self):
		super().__init__(OvlContext())

	def load(self, filepath):
		with open(filepath, "rb") as stream:
			self.read_fields(stream, self)

	def save(self, filepath):
		self.old_size = os.path.getsize(filepath)
		with open(filepath, "wb") as stream:
			self.write_fields(stream, self)


if __name__ == "__main__":
	# bnk = BnkFile()
	# bnk.load("C:/Users/arnfi/Desktop/Coding/ovl/aux files/dlc_dingo_dlc_dingo_media_bnk_B.aux")
	# print(bnk)
	bnk = BnkFile()
	bnk.load("C:/Users/arnfi/Desktop/Coding/ovl/aux files/music_vehicleradio_events.bnk")
	print(bnk)
