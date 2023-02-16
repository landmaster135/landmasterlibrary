# generaltool.py

# Library by default
from pathlib import Path
import os
import sys
# Library by third party
import yaml
# Library by landmasterlibrary
from .config import Config


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
    txt_lines = []
    for i in range(0, len(read_files)):
        file_full_name = get_src_path_from_test_path(calling_file_path, read_files[i], dir_name)
        with open(file_full_name, "r") as fr:
            txt_lines.append(fr.readlines())
        txt_lines[i] = remove_empty_items(txt_lines[i])
        for j in range(0, len(txt_lines[i])):
            txt_lines[i][j] = txt_lines[i][j].replace("\n", "")
    return txt_lines # [][]

def read_csv_lines(calling_file_path : str, read_files : list, dir_name : str) -> list:
    if type(calling_file_path) != str:
        raise TypeError("TypeError: calling_file_path must be str type.")
    if type(read_files) != list:
        raise TypeError("TypeError: read_files must be list type.")
    if type(dir_name) != str:
        raise TypeError("TypeError: dir_name must be str type.")
    csv_lines = []
    for i in range(0, len(read_files)):
        file_full_name = get_src_path_from_test_path(calling_file_path, read_files[i], dir_name)
        with open(file_full_name, "r") as fr:
            txt_lines = fr.readlines()
        csv_line = []
        for j in range(0, len(txt_lines)):
            csv_line.append(txt_lines[j].split(","))
        csv_lines.append(csv_line)
        csv_lines[i] = remove_empty_items(csv_lines[i])
        for j in range(0, len(csv_lines[i])):
            for k in range(0, len(csv_lines[i][j])):
                csv_lines[i][j][k] = csv_lines[i][j][k].replace("\n", "")
    return csv_lines # [][][]

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
    sep_indices.sort()
    return sep_indices

def get_indcies_containing_words(target_list : list, words : list) -> list:
    if type(target_list) != list:
        raise TypeError("TypeError: target_list must be list type.")
    if type(words) != list:
        raise TypeError("TypeError: words must be list type.")
    for i in range(0, len(target_list)):
        if type(target_list[i]) != str:
            target_list[i] = str(target_list[i])
    for i in range(0, len(words)):
        if type(words[i]) != str:
            words[i] = str(words[i])
    indcies_containing_words = []
    for i in range(0, len(target_list)):
        for j in range(0, len(words)):
            indices = get_indices_by_seperators(target_list[i], [words[j]])
            indices.pop(len(indices) - 1)
            if len(indices) > 0:
                indcies_containing_words.append(i)
                break
    return indcies_containing_words

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

def replace_by_words(word : str, replacing_word : dict = {":": "：", "/": "／", "\"": "”"}) -> str:
    for k, v in replacing_word.items():
        print(k, ",,,,,", v)
        print(word)
        word = word.replace(k, v)
    return word


















def print_funcs() -> str:
    args = sys.argv
    functions = get_func(args)

    # display
    prefix = args[3]
    if prefix != "":
        functions = [f"{prefix} {f}" for f in functions]
    print("============ functions list: start ============")
    for func in functions:
        print(f"{func}")
    print("============ functions list: end ============")
    return functions



if __name__ == "__main__":
    # print_funcs()
    # print_depends()
    print_depends_on_mermaid()
