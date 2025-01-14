from generated.array import Array
from generated.formats.ovl_base.compounds.Pointer import Pointer
from generated.formats.ovl_base.compounds.Pointer import Pointer


class ArrayPointer(Pointer):

	"""
	a pointer to an array in an ovl memory layout
	"""

	__name__ = 'ArrayPointer'

	_import_key = 'ovl_base.compounds.ArrayPointer'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		if set_default:
			self.set_defaults()

	_attribute_list = Pointer._attribute_list + [
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)

	def read_template(self):
		if self.template:
			self.data = Array.from_stream(self.frag.struct_ptr.stream, self.context, 0, None, (self.arg,), self.template)

	@classmethod
	def _to_xml(cls, instance, elem, debug):
		"""Assigns data self to xml elem"""
		if callable(getattr(instance.template, "_to_xml_array", None)):
			instance.template._to_xml_array(instance.data, elem, debug)
			return
		Array._to_xml(instance.data, elem, debug)

	@classmethod
	def _from_xml(cls, instance, elem):
		if callable(getattr(instance.template, "_from_xml_array", None)):
			instance.data = instance.template._from_xml_array(None, elem)
			return
		arr = Array(instance.context, 0, None, (len(elem)), instance.template, set_default=False)
		instance.data = Array._from_xml(arr, elem)
		return instance

