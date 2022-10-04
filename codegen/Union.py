from codegen.expression import Expression, Version, interpret_literal
from codegen.Imports import Imports
from codegen.Versions import Versions
import codegen.naming_conventions as convention

CONTEXT_SUFFIX = "context"


def get_attr_with_backups(field, attribute_keys):
    # return the value of the first attribute in the list that is not empty or
    # missing
    for key in attribute_keys:
        attr_value = field.attrib.get(key)
        if attr_value:
            return attr_value
    else:
        return None


def condition_indent(base_indent, conditionals, condition=""):
    # determine the python condition and indentation level based on whether the
    # last used condition was the same.
    if conditionals:
        new_condition = f"if {' and '.join(conditionals)}:"
        # condition is there but has not changed, so we can keep it in the same if clause
        if condition == new_condition:
            new_condition = ""
        # there are conditionals (same or different) so we must indent
        indent = base_indent + "\t"
    else:
        indent = base_indent
        new_condition = ""

    return indent, new_condition


class Union:
    def __init__(self, compound, union_name):
        self.compounds = compound
        self.name = union_name
        self.members = []

    def is_ovl_ptr(self):
        """Check if this union is used as an ovl memory pointer"""
        for field in self.members:
            arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, _ = self.get_params(field)
            if field_type in ("Pointer", "ArrayPointer", "ForEachPointer"):
                return True

    def append(self, member):
        self.members.append(member)

    def indirect_class_access(self, field_type):
        if self.compounds.parser.tag_dict[field_type.lower()] in self.compounds.parser.struct_types:
            class_access = f'{self.compounds.class_name}._import_map["{Imports.import_map_key(self.compounds.parser.path_dict[field_type])}"]'
        else:
            class_access = field_type
        return class_access

    def get_conditions(self, field, expression_prefix="self.", use_abstract=False):
        CONTEXT = f'{expression_prefix}{CONTEXT_SUFFIX}'
        VER = f"{CONTEXT}.version"
        conditionals = []
        ver1 = get_attr_with_backups(field, ["ver1", "since"])
        if ver1:
            ver1 = Version(ver1)
        ver2 = get_attr_with_backups(field, ["ver2", "until"])

        if ver2:
            ver2 = Version(ver2)
        vercond = field.attrib.get("vercond")
        valid_versions = field.attrib.get("versions")
        if valid_versions:
            valid_versions = [Versions.format_id(version) for version in valid_versions.split(" ")]
        cond = field.attrib.get("cond")
        onlyT = field.attrib.get("onlyT")
        excludeT = field.attrib.get("excludeT")
        if ver1 and ver2:
            conditionals.append(f"{ver1} <= {VER} <= {ver2}")
        elif ver1:
            conditionals.append(f"{VER} >= {ver1}")
        elif ver2:
            conditionals.append(f"{VER} <= {ver2}")
        if vercond:
            vercond = Expression(vercond, f'{expression_prefix}context.')
            conditionals.append(f"{vercond}")
        if valid_versions:
            conditionals.append(f"({' or '.join([f'versions.is_{version}({CONTEXT})' for version in valid_versions])})")
        if cond:
            cond = Expression(cond, f'{expression_prefix}')
            conditionals.append(f"{cond}")
        if onlyT:
            onlyT = self.indirect_class_access(onlyT)
            conditionals.append(f"isinstance({expression_prefix[:-1]}, {onlyT})")
        if excludeT:
            excludeT = self.indirect_class_access(excludeT)
            conditionals.append(f"not isinstance({expression_prefix[:-1]}, {excludeT})")
        if use_abstract:
            if field.attrib.get("abstract", "False") == "True":
                conditionals.append("include_abstract")
        return conditionals

    def get_params(self, field, expression_prefix="self.", use_abstract=False):
        # parse all attributes and return the python-evaluatable string

        field_name = field.attrib["name"]
        field_type = field.attrib["type"]
        if field_type == "template":
            field_type = f'{expression_prefix}{field_type}'
        pad_mode = field.attrib.get("padding")
        template = field.attrib.get("template")
        optional = (field.attrib.get("optional", "False"), field.attrib.get("default"))

        conditionals = self.get_conditions(field, expression_prefix, use_abstract)

        arg = field.attrib.get("arg", "0")
        arr1 = get_attr_with_backups(field, ["arr1", "length"])
        arr2 = get_attr_with_backups(field, ["arr2", "width"])
        if template:
            # template can be either a type or a reference to a local field
            template_class = convention.name_class(template)
            if template_class not in self.compounds.parser.path_dict:
                template = Expression(template, expression_prefix)
            else:
                template = self.indirect_class_access(template_class)
        if arg:
            arg = Expression(arg, expression_prefix)
        if arr1:
            arr1 = Expression(arr1, expression_prefix)
        if arr2:
            arr2 = Expression(arr2, expression_prefix)
        return arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, optional

    def default_to_value(self, default_string, field_type):
        if default_string:
            if field_type in self.compounds.parser.path_dict and self.compounds.parser.tag_dict[field_type.lower()] == "enum":
                default_string = convention.name_enum_key_if_necessary(default_string)
                return f'{field_type}.{default_string}'
            else:
                if ", " in default_string:
                    # already formatted by format_potential_tuple
                    pass
                else:
                    # check for boolean
                    if field_type in self.compounds.parser.path_dict and \
                    self.compounds.parser.tag_dict[field_type.lower()] == "basic" and \
                        field_type in self.compounds.parser.basics.booleans:
                        # boolean basics *can* be used as booleans, but don't have to be
                        if default_string.capitalize() in ("True", "False"):
                            default_string = default_string.capitalize()
                            return default_string
                    value = interpret_literal(default_string)
                    if value is not None:
                        default_string = str(value)
                    else:
                        # not interpretable, must be a string
                        default_string = repr(default_string)
        return default_string

    def get_default_string(self, default_string, context, arg, template, arr1, arr2, field_name, field_type):
        # get the default (or the best guess of it)
        field_type_lower = field_type.lower()
        tag_of_field_type = self.compounds.parser.tag_dict.get(field_type_lower)
        _, return_type = self.compounds.parser.map_type(field_type, arr1)
        default_string = self.default_to_value(default_string, field_type)

        if arr1:
            arr_str = self.compounds.parser.arrs_to_tuple(arr1, arr2)
            if default_string:
                if return_type[0] == 'numpy':
                    return f'numpy.full({arr_str}, dtype={return_type[1]}, fill_value={default_string})'
                else:
                    return f'Array.from_value({arr_str}, {field_type}, {default_string})'
            else:
                if return_type[0] == 'numpy':
                    return f'numpy.zeros({arr_str}, dtype={return_type[1]})'
                else:
                    return f'Array({context}, {arg}, {template}, {arr_str}, {field_type})'
        else:
            if default_string:
                if return_type in self.compounds.parser.builtin_literals or tag_of_field_type == "enum":
                    # the default string, when evaluated, gives the correct type
                    return default_string
                else:
                    # the default sring needs to be converted to an object of the proper type
                    return f'{field_type}.from_value({default_string})'
            else:
                # we don't have a specified default, guess one
                if return_type in self.compounds.parser.builtin_literals:
                    # this type can be returned from a literal
                    return repr(self.compounds.parser.builtin_literals[return_type])
                else:
                    # instantiate like a generic type: dtype(context, arg, template)
                    return f'{field_type}({context}, {arg}, {template})'

    # def default_assigns(self, field, context, arg, template, arr1, arr2, field_name, field_type, base_indent):
    #     field_default = self.get_default_string(field.attrib.get('default'), context, arg, template, arr1, arr2, field_name,
    #                                             field_type)
    #     default_children = field.findall("default")
    #     if default_children:
    #         defaults = [(f'{base_indent}else:', f'{base_indent}\tself.{field_name} = {field_default}')]
    #         last_default = len(default_children) - 1
    #         condition = ""
    #         for i, default_element in enumerate(default_children):
    #
    #             # get the condition
    #             conditionals = self.get_conditions(default_element)
    #             indent, condition = condition_indent(base_indent, conditionals, condition)
    #             if not condition:
    #                 raise AttributeError(
    #                     f"Default tag without or with overlapping conditionals on {field.attrib['name']} {condition} {default_element.get('value')}")
    #             if i != last_default:
    #                 condition = f'{base_indent}el{condition}'
    #             else:
    #                 condition = f'{base_indent}{condition}'
    #
    #             default = self.get_default_string(default_element.attrib.get("value"), context, arg, template, arr1, arr2,
    #                                               field_name, field_type)
    #             defaults.append((condition, f'{indent}self.{field_name} = {default}'))
    #
    #         defaults = defaults[::-1]
    #     else:
    #         defaults = [("", f'{base_indent}self.{field_name} = {field_default}')]
    #     return defaults

    def write_init(self, f):
        base_indent = "\n\t\t"
        debug_strs = []
        for field in self.members:
            field_debug_str = convention.clean_comment_str(field.text, indent="\t\t")
            arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, _ = self.get_params(field)
            if field_debug_str.strip() and field_debug_str not in debug_strs:
                debug_strs.append(field_debug_str)

        # add every (unique) debug string:
        for field_debug_str in debug_strs:
            f.write(field_debug_str)
        # nice idea, but causes too much trouble
        if arr1:
            # init with empty shape to work regardless of condition
            field_default = f'Array(self.{CONTEXT_SUFFIX}, {arg}, {template}, (0,), {field_type})'
        else:
            # we init each field with 0 to prevent overhead, but still allow the field to be used in conditionals
            # field_default = 0
            # we init each field with its basic default string so that the field exists regardless of any condition
            field_default = self.get_default_string(field.attrib.get('default'), f'self.{CONTEXT_SUFFIX}', arg, template,
                                                    arr1, arr2, field_name,
                                                    field_type)
        f.write(f'{base_indent}self.{field_name} = {field_default}')

    # def write_defaults(self, f, condition=""):
    #     base_indent = "\n\t\t"
    #     for field in self.members:
    #         arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, _ = self.get_params(field)
    #
    #         indent, new_condition = condition_indent(base_indent, conditionals, condition)
    #
    #         defaults = self.default_assigns(field, f'self.{CONTEXT_SUFFIX}', arg, template, arr1, arr2, field_name, field_type, indent)
    #
    #         if field_name == "dtype":
    #             f.write(f"{base_indent}# leaving self.dtype alone")
    #         else:
    #             # if defaults:
    #             if new_condition:
    #                 f.write(f"{base_indent}{new_condition}")
    #             if new_condition or indent == base_indent:
    #                 condition = new_condition
    #             for default_condition, default in defaults:
    #                 if default_condition:
    #                     f.write(default_condition)
    #                 f.write(default)
    #     return condition

    # def write_io(self, f, method_type, condition="", target_variable="self"):
    #     CONTEXT = f'{target_variable}.{CONTEXT_SUFFIX}'
    #     base_indent = "\n\t\t"
    #     for field in self.members:
    #         if field.attrib.get("abstract", "False") == "True":
    #             continue
    #         arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, _ = self.get_params(field, f'{target_variable}.')
    #         indent, new_condition = condition_indent(base_indent, conditionals, condition)
    #         if new_condition:
    #             f.write(f"{base_indent}{new_condition}")
    #         if new_condition or indent == base_indent:
    #             condition = new_condition
    #         if method_type == 'read':
    #             f.write(f"{indent}{target_variable}.{field_name} = {self.compounds.parser.read_for_type(field_type, CONTEXT, arg, template, arr1, arr2)}")
    #             # store version related fields on the context on read
    #             for k, (access, dtype) in self.compounds.parser.verattrs.items():
    #                 # check all version-related global variables registered with the verattr tag
    #                 attr_path = access.split('.')
    #                 if field_name == attr_path[0]:
    #                     if dtype is None or len(attr_path) > 1 or field_type == dtype:
    #                         # the verattr type isn't known, we can't check it or it matches
    #                         f.write(f"{indent}{CONTEXT}.{field_name} = {target_variable}.{field_name}")
    #                         break
    #         else:
    #             # if arr1 and pad_mode: resize array to the specified size
    #             if arr1 and pad_mode and self.compounds.parser.tag_dict[field_type.lower()] == "basic":
    #                 f.write(f"{indent}{target_variable}.{field_name}.resize({self.compounds.parser.arrs_to_tuple(arr1, arr2)})")
    #             f.write(f"{indent}{self.compounds.parser.write_for_type(field_type, f'{target_variable}.{field_name}', CONTEXT, arg, template, arr1, arr2)}")
    #     return condition

    def write_attributes(self, f):
        for field in self.members:
            arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, (optional, default) = self.get_params(field, f'x.')
            # replace all non-static values with None for now
            try:
                arg = int(str(arg), 0)
            except ValueError:
                arg = None
            if template not in self.compounds.parser.path_dict:
                template = None
            if field_type not in self.compounds.parser.path_dict:
                field_type = None
            default = self.default_to_value(default, field_type)
            if arr1 is None:
                arguments = f"({arg}, {template})"
            else:
                shape = self.compounds.parser.arrs_to_tuple(arr1, arr2)
                shape_parts = shape[1:-1].split(",")
                resolved_shape_parts = []
                for dim in shape_parts:
                    dim = dim.strip()
                    if dim:
                        try:
                            dim = int(dim, 0)
                        except ValueError:
                            dim = None
                        resolved_shape_parts.append(str(dim))
                shape = f"({', '.join(resolved_shape_parts)},)"
                arguments = f"({arg}, {template}, {shape}, {field_type})"
                field_type = "Array"
            f.write(f"({repr(field_name)}, {field_type}, {arguments}, ({optional}, {default}), {True if conditionals else None}),\n\t\t")

    def write_filtered_attributes(self, f, condition, target_variable="self"):
        base_indent = "\n\t\t"
        for field in self.members:
            arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, (optional, default) = self.get_params(field, f'{target_variable}.', use_abstract=True)
            default = self.default_to_value(default, field_type)
            if arr1 is None:
                arguments = f"({arg}, {template})"
            else:
                arguments = f"({arg}, {template}, {self.compounds.parser.arrs_to_tuple(arr1, arr2)}, {field_type})"
                field_type = "Array"

            indent, new_condition = condition_indent(base_indent, conditionals, condition)
            if new_condition:
                f.write(f"{base_indent}{new_condition}")
            if new_condition or indent == base_indent:
                condition = new_condition

            default_children = field.findall("default")
            if default_children:

                condition_defaults = [(f'{indent}else:', default)]
                last_default = len(default_children) - 1
                def_condition = ""
                for i, default_element in enumerate(default_children):
    
                    # get the condition
                    conditionals = self.get_conditions(default_element, expression_prefix=f'{target_variable}.')
                    def_indent, def_condition = condition_indent(indent, conditionals, def_condition)
                    if not def_condition:
                        raise AttributeError(
                            f"Default tag without or with overlapping conditionals on {field.attrib['name']} {def_condition} {default_element.get('value')}")
                    if i != last_default:
                        def_condition = f'{indent}el{def_condition}'
                    else:
                        def_condition = f'{indent}{def_condition}'
                    condition_defaults.append((def_condition, self.default_to_value(default_element.attrib.get("value"), field_type)))
                condition_defaults = condition_defaults[::-1]
            else:
                condition_defaults = [("", default)]

            for def_condition, default in condition_defaults:
                if def_condition:
                    f.write(def_condition)
                    def_indent = f'{indent}\t'
                else:
                    def_indent = indent
                f.write(f"{def_indent}yield {repr(field_name)}, {field_type}, {arguments}, ({optional}, {default})")
        return condition

    # def write_arg_update(self, f, method_type):
    #     base_indent = "\n\t\t"
    #     for field in self.members:
    #         arg, template, arr1, arr2, conditionals, field_name, field_type, pad_mode, _ = self.get_params(field, f'instance.')
    #         if method_type == 'read':
    #             f.write(f"{base_indent}if not isinstance(instance.{field_name}, int):")
    #             f.write(f"{base_indent}\tinstance.{field_name}.arg = {arg}")
