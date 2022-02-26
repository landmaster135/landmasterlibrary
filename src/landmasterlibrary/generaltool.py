# generaltool.py

# Library by default
from pathlib import Path
import sys
# Library by third party
import yaml
# Library by landmasterlibrary


def get_str_repeated_to_mark(repeat_str : str, repeat_number_to_mark : int = 15) -> str:
    return str(repeat_str * repeat_number_to_mark)

def output_log(class_name : str, function_name : str, remark : str) -> None:
    print("{class_name}: {function_name}: {remark}".format(
        class_name=class_name,
        function_name=function_name,
        remark=remark
    ))

def get_str_from_list(target_list : list) -> str:
    separator = ","
    bracket_start = "["
    bracket_end   = "]"
    result_str = ""
    for i in target_list:
        if result_str == "":
            result_str = "{}{}".format(result_str, str(i))
        else:
            result_str = "{}{}{}".format(result_str, separator, str(i))
    result_str = "{} {} {}".format(bracket_start, result_str, bracket_end)
    return result_str

def get_obj_from_yaml(yaml_file):
    # className = self.__class__.__name__
    # functionName = sys._getframe().f_code.co_name
    with open(yaml_file) as file:
        obj = yaml.safe_load(file)
    return obj

def get_value_from_yaml(yaml_file, field):
    class_name = __name__
    function_name = sys._getframe().f_code.co_name
    value = ""
    obj = get_obj_from_yaml(yaml_file)
    try:
        value = obj[field]
    except KeyError:
        raise ValueError("{class_name}: {function_name}: {message}".format(
            className=class_name,
            functionName=function_name,
            message=obj["msgObj_E0102"]
        ))
    return value

def get_src_path_from_test_path(calling_file_path : str, src_file_name : str, src_folder_name : str = "src") -> str:
    degree_of_parent_directory = 2 - 1
    src_path = str(Path(calling_file_path).parents[degree_of_parent_directory] / src_folder_name / src_file_name)
    return src_path
