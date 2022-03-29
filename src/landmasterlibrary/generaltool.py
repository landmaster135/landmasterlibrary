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
    if type(repeat_str) != str:
        raise TypeError("TypeError: repeat_str must be str type.")
    if type(repeat_number_to_mark) != int:
        raise TypeError("TypeError: repeat_number_to_mark must be int type.")
    return str(repeat_str * repeat_number_to_mark)

def get_str_by_zero_padding(number : int, number_of_digit : int = 4) -> str:
    if type(number) != int:
        raise TypeError("TypeError: number must be str type.")
    if type(number_of_digit) != int:
        raise TypeError("TypeError: number_of_digit must be int type.")
    targetNumberOfDigit = number_of_digit
    if len(str(number)) >= number_of_digit:
        targetNumberOfDigit = 0
    else:
        targetNumberOfDigit = number_of_digit - len(str(number))
    return "{}{}".format(get_str_repeated_to_mark("0", targetNumberOfDigit), str(number))
    # return get_str_repeated_to_mark("0", targetNumberOfDigit + number).slice(-(targetNumberOfDigit))

def output_log(class_name : str, function_name : str, remark : str = "") -> str:
    remark = remark
    if type(class_name) != str:
        raise TypeError("TypeError: class_name must be str type.")
    if type(function_name) != str:
        raise TypeError("TypeError: function_name must be str type.")
    if remark is None:
        print("a")
        remark = ""
    if type(remark) != str:
        raise TypeError("TypeError: remark must be str type.")
    print_str = "{class_name}: {function_name}: {remark}".format(
        class_name=class_name,
        function_name=function_name,
        remark=remark
    )
    print(print_str)
    return print_str

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

def get_src_dir_path_from_test_path(calling_file_path : str, src_folder_name : str, isChecking : bool = True) -> str:
    if type(calling_file_path) != str:
        raise TypeError("TypeError: calling_file_path must be str type.")
    if type(src_folder_name) != str:
        raise TypeError("TypeError: src_folder_name must be str type.")
    if type(isChecking) != bool:
        raise TypeError("TypeError: isChecking must be bool type.")
    degree_of_parent_directory = 2 - 1
    src_dir_path = str(Path(calling_file_path).resolve().parents[degree_of_parent_directory] / src_folder_name)
    if isChecking == True:
        if os.path.isdir(src_dir_path) == False:
            if os.path.isfile(src_dir_path) == True:
                raise NotADirectoryError(f"NotADirectoryError: Directory \"{src_dir_path}\" is a file")
            raise FileNotFoundError(f"FileNotFoundError: Directory \"{src_dir_path}\" does not exist")
    return src_dir_path

def get_src_path_from_test_path(calling_file_path : str, src_file_name : str, src_folder_name : str = "src/landmasterlibrary", isChecking : bool = True) -> str:
    if type(calling_file_path) != str:
        raise TypeError("TypeError: calling_file_path must be str type.")
    if type(src_file_name) != str:
        raise TypeError("TypeError: src_file_name must be str type.")
    if type(src_folder_name) != str:
        raise TypeError("TypeError: src_folder_name must be str type.")
    if type(isChecking) != bool:
        raise TypeError("TypeError: isChecking must be bool type.")
    degree_of_parent_directory = 2 - 1
    src_path = str(Path(calling_file_path).resolve().parents[degree_of_parent_directory] / src_folder_name / src_file_name)
    if isChecking == True:
        if os.path.isfile(src_path) == False:
            if os.path.isdir(src_path) == True:
                raise IsADirectoryError(f"IsADirectoryError: File \"{src_path}\" is a directory")
            raise FileNotFoundError(f"FileNotFoundError: File \"{src_path}\" does not exist")
    return src_path

def read_txt_lines(calling_file_path : str, read_files : list, dir_name : str) -> list:
    if type(calling_file_path) != str:
        raise TypeError("TypeError: calling_file_path must be str type.")
    if type(read_files) != list:
        raise TypeError("TypeError: read_files must be list type.")
    if type(dir_name) != str:
        raise TypeError("TypeError: dir_name must be str type.")
    read_txt_lines = []
    for i in range(0, len(read_files)):
        file_full_name = get_src_path_from_test_path(calling_file_path, read_files[i], dir_name)
        with open(file_full_name, "r") as fr:
            # read_books_lines = fr.readlines()
            read_txt_lines.append(fr.readlines())
        read_txt_lines[i] = remove_empty_items(read_txt_lines[i])
        for j in range(0, len(read_txt_lines[i])):
            read_txt_lines[i][j] = read_txt_lines[i][j].replace("\n", "")
    return read_txt_lines # [][]

def read_csv_lines(calling_file_path : str, read_files : list, dir_name : str) -> list:
    if type(calling_file_path) != str:
        raise TypeError("TypeError: calling_file_path must be str type.")
    if type(read_files) != list:
        raise TypeError("TypeError: read_files must be list type.")
    if type(dir_name) != str:
        raise TypeError("TypeError: dir_name must be str type.")
    read_csv_lines = []
    for i in range(0, len(read_files)):
        file_full_name = get_src_path_from_test_path(calling_file_path, read_files[i], dir_name)
        with open(file_full_name, "r") as fr:
            # read_books_lines = fr.readlines()
            read_txt_lines = fr.readlines()
        read_csv_line = []
        for j in range(0, len(read_txt_lines)):
            read_csv_line.append(read_txt_lines[j].split(","))
        read_csv_lines.append(read_csv_line)
        read_csv_lines[i] = remove_empty_items(read_csv_lines[i])
        for j in range(0, len(read_csv_lines[i])):
            for k in range(0, len(read_csv_lines[i][j])):
                read_csv_lines[i][j][k] = read_csv_lines[i][j][k].replace("\n", "")
    return read_csv_lines # [][][]

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
    if len(word) == 0:
        word_removed_space = word
    elif word[len(word) - 1] in spaces:
        word_removed_space = word[0:len(word) - 1]
        print("'{}'".format(word_removed_space[0:len(word) - 1]))
        word_removed_space = remove_tail_sapces(word_removed_space, spaces)
    else:
        word_removed_space = word
    return word_removed_space

def remove_head_sapces(word : str, spaces : list = Config.spaces) -> str:
    word_removed_space = ""
    if len(word) == 0:
        word_removed_space = word
    elif word[0] in spaces:
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
    output_log(
        __file__,
        function_name,
        "{}".format(get_str_repeated_to_mark("b"))
    )
    return words

def append_items(appended_list : list, appending_list : list, target_index : int = 0) -> list:
    if type(appended_list) != list:
        raise TypeError("TypeError: appended_list must be list type.")
    if type(appending_list) != list:
        raise TypeError("TypeError: appending_list must be list type.")
    if type(target_index) != int:
        raise TypeError("TypeError: target_index must be int type.")
    if target_index < 0:
        raise IndexError("IndexError: target_index must be more than or equal to 0.")
    if target_index > len(appended_list):
        raise IndexError("IndexError: target_index must be less than length of appended_list.")
    for i in range(0, len(appending_list)):
        appended_list.insert(target_index + i, appending_list[i])
    return appended_list

def remove_empty_items(removed_list : list, target_items : list = [""]) -> list:
    if type(removed_list) != list:
        raise TypeError("TypeError: removed_list must be list type.")
    if type(target_items) != list:
        raise TypeError("TypeError: target_item must be list type.")
    removed_count = 0
    for i in range(0, len(removed_list)):
        j = i - removed_count
        if removed_list[j] in target_items:
        # if removed_list[j] == target_item:
            removed_list.pop(j)
            removed_count += 1
    return removed_list

def get_files_by_extensions(target_dir : str, extensions : list) -> list:
    if type(extensions) != list:
        raise TypeError("TypeError: extensions must be list type.")
    for i in range(0, len(extensions)):
        if type(extensions[i]) != str:
            raise TypeError("TypeError: extensions' items must be str type.")
    all_files = os.listdir(target_dir)
    files = []
    for i in range(0, len(all_files)):
        for j in range(0, len(extensions)):
            if all_files[i][-len(extensions[j]):] == extensions[j]:
                files.append(all_files[i])
    return files

def printfunc() -> str:
    args = sys.argv
    print(args)
    # file_name = args[1]
    file_path = args[1]
    function_name = sys._getframe().f_code.co_name
    output_log(
        __file__,
        function_name,
        "{}".format(get_str_repeated_to_mark("a"))
    )
    print(f"file_name is {file_path}")
    print(type(file_path))
    try:
        if type(file_path) != str:
            raise TypeError("TypeError: 1 argument is expected str only, not NoneType")
    except TypeError as e:
        raise
    functions = get_functions_in_python_file(file_path)
    output_log(
        __file__,
        function_name,
        "{}".format(get_str_repeated_to_mark("b"))
    )

    # display
    prefix = args[2]
    print("============ functions list: start ============")
    for func in functions:
        print("{} {}".format(prefix, func))
    print("============ functions list: end ============")
    return functions

if __name__ == "__main__":
    printfunc()
