# generaltool.py

# Library by default
from argparse import ArgumentError
from pathlib import Path
import os
import sys
from typing import Type
# Library by third party
import yaml
# Library by landmasterlibrary
from .config import Config
# config = Config()


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

def get_indices_by_seperators(word : str, seperators : list = Config.seperators) -> list:
    sep_indices = []
    for sep in seperators:
        start = 0
        sep_index = 0
        while sep_index != -1:
            sep_index = word.find(sep, start)
            if sep_index != -1:
                sep_indices.append(sep_index)
            start = sep_index + 1
    sep_indices.append(len(word))
    print(sep_indices)
    sep_indices.sort()
    print(sep_indices)
    return sep_indices

def get_words_by_indices(word : str, indices : list) -> list:
    start = 0
    words = []
    for i in indices:
        words.append(word[start:i])
        start = i + 1
    print(words)
    return words

def get_words_by_seperators(word : str, seperators : list = Config.seperators, spaces : list = Config.spaces) -> list:
    indices = get_indices_by_seperators(word, seperators)
    words = get_words_by_indices(word, indices)
    words_without_space = []
    for word in words:
        words_without_space.append(remove_spaces_at_head_and_tail(word, spaces))
    print(words_without_space)
    return words_without_space

def remove_spaces_at_head_and_tail(word : str, spaces : list = Config.spaces) -> str:
    word_tail_removed = remove_tail_sapces(word, spaces)
    word_both_removed = remove_head_sapces(word_tail_removed, spaces)
    return word_both_removed

def remove_tail_sapces(word : str, spaces : list = Config.spaces) -> str:
    word_removed_space = ""
    if word[len(word) - 1] in spaces:
        word_removed_space = word[0:len(word) - 1]
        print("'{}'".format(word_removed_space[0:len(word) - 1]))
        word_removed_space = remove_tail_sapces(word_removed_space, spaces)
    else:
        word_removed_space = word
    return word_removed_space

def remove_head_sapces(word : str, spaces : list = Config.spaces) -> str:
    word_removed_space = ""
    if word[0] in spaces:
        word_removed_space = word[1:len(word)+1]
        # invisible head character if head space is nothing
        print("'{}'".format(word_removed_space[1:len(word)]))
        word_removed_space = remove_head_sapces(word_removed_space, spaces)
    else:
        word_removed_space = word
    return word_removed_space

def get_functions_in_python_file(file_full_name : str, head_of_function : str = "def ", tail_of_function : str = "(") -> list:
    functions = []
    text = ""
    with open(file_full_name, "r", encoding="UTF-8") as f:
        text = f.read()

    function_name = sys._getframe().f_code.co_name
    output_log(
        __file__,
        function_name,
        "{}".format(get_str_repeated_to_mark("a"))
    )
    print(text)

    text_lines = text.split("\n")
    functions = get_words_in_lines_by_head_and_tail(text_lines, head_of_function, tail_of_function)
    return functions

def get_words_in_lines_by_head_and_tail(text_lines : list, head_of_target : str, tail_of_target : str) -> list:
    words = []
    text_line_removed_head_space = ""
    function_name = sys._getframe().f_code.co_name

    output_log(
        __file__,
        function_name,
        "{}".format(get_str_repeated_to_mark("a"))
    )
    print(text_lines)

    for text_line in text_lines:
        text_line_removed_head_space = remove_head_sapces(text_line)
        head_index = text_line_removed_head_space.find(head_of_target, 0)
        if head_index != 0:
            continue
        tail_index = text_line_removed_head_space.find(tail_of_target, 0+head_index)
        if text_line_removed_head_space.find(tail_of_target, 0) == -1:
            continue
        word = text_line_removed_head_space[len(head_of_target):tail_index]
        words.append(word)
    return words


def printfunc() -> str:
    args = sys.argv
    file_name = args[1]
    function_name = sys._getframe().f_code.co_name
    output_log(
        __file__,
        function_name,
        "{}".format(get_str_repeated_to_mark("a"))
    )
    print(f"file_name is {file_name}")
    try:
        if isinstance(file_name, str) == False:
            raise TypeError("TypeError: 1 argument is expected str only, not NoneType")
    except TypeError as e:
        raise
    file_path = Path(file_name)
    try:
        if os.path.isfile(file_path) == False:
            if os.path.isdir(file_path) == True:
                raise IsADirectoryError(f"File \"{file_path}\" is a directory")
            raise FileNotFoundError(f"File \"{file_path}\" does not exist")
    except Exception as e:
        raise
    functions = get_functions_in_python_file(file_path)
    for func in functions:
        print(func)
    return True

if __name__ == "__main__":
    printfunc()
