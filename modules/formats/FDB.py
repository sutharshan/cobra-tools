import logging
import os
import shutil
import sqlite3
import struct
import traceback

from generated.formats.ovl_base.versions import is_pz, is_pz16
from modules.formats.BaseFormat import BaseFile
from root_path import root_dir


class FdbLoader(BaseFile):
	extension = ".fdb"

	def create(self):
		root_entry, buffer_0, buffer_1 = self._get_data(self.file_entry.path)
		self.create_root_entry()
		self.write_data_to_pool(self.root_entry.struct_ptr, 2, root_entry)
		self.create_data_entry((buffer_0, buffer_1))

	def extract(self, out_dir):
		name = self.root_entry.name
		try:
			buff = self.data_entry.buffer_datas[1]
		except:
			raise AttributeError(f"Found no buffer data for {name}")
		out_path = out_dir(name)
		with open(out_path, 'wb') as outfile:
			outfile.write(buff)
		return out_path,

	def _get_data(self, file_path):
		"""Loads and returns the data for an FDB"""
		buffer_0 = self.file_entry.basename.encode(encoding='utf8')
		buffer_1 = self.get_content(file_path)
		root_entry = struct.pack("I28s", len(buffer_1), b'')
		return root_entry, buffer_0, buffer_1

	def open_command(self, f):
		command_path = os.path.join(root_dir, "sql_commands", f+".sql")
		with open(command_path, "r") as file:
			return file.read()

	def rename_content(self, name_tuples):
		command = None
		s = None
		if is_pz(self.ovl) or is_pz16(self.ovl):
			for s in ("zoopedia", "research", "education", "animals"):
				if s in self.file_entry.name:
					command = self.open_command(f"pz_{s}")
					break
		if command:
			logging.info(f"Executing command '{s}' on {self.file_entry.name}")
			try:
				temp_dir, out_dir_func = self.get_tmp_dir()
				fdb_path = self.extract(out_dir_func)[0]
				con = sqlite3.connect(fdb_path)
				cur = con.cursor()

				for old, new in name_tuples:
					command_replaced = command.replace("ORIGINAL", old).replace("NEW", new)
					# print(command_replaced)
					cur.executescript(command_replaced)
				# Save (commit) the changes
				con.commit()
				con.close()
				self.remove()
				self.ovl.create_file(fdb_path)
				shutil.rmtree(temp_dir)
			except BaseException as err:
				traceback.print_exc()

