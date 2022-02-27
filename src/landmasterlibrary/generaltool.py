# generaltool.py

# Library by default
from pathlib import Path
import sys
# Library by third party
import yaml
# Library by landmasterlibrary
from .config import Config
config = Config()


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

def get_indices_by_seperators(word : str, seperators : list = config.seperators) -> list:
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

def get_words_by_seperators(word : str, seperators : list = config.seperators, spaces : list = config.spaces) -> list:
    indices = get_indices_by_seperators(word, seperators)
    words = get_words_by_indices(word, indices)
    words_without_space = []
    for word in words:
        words_without_space.append(remove_spaces_at_head_and_tail(word, spaces))
    print(words_without_space)
    return words_without_space

def remove_spaces_at_head_and_tail(word : str, spaces : list = config.spaces) -> str:
    word_tail_removed = remove_tail_sapces(word, spaces)
    word_both_removed = remove_head_sapces(word_tail_removed, spaces)
    return word_both_removed

def remove_tail_sapces(word : str, spaces : list = config.spaces) -> str:
    word_removed_space = ""
    if word[len(word) - 1] in spaces:
        word_removed_space = word[0:len(word) - 1]
        print("'{}'".format(word_removed_space[0:len(word) - 1]))
        word_removed_space = remove_tail_sapces(word_removed_space, spaces)
    else:
        word_removed_space = word
    return word_removed_space

def remove_head_sapces(word : str, spaces : list = config.spaces) -> str:
    word_removed_space = ""
    if word[0] in spaces:
        word_removed_space = word[1:len(word)+1]
        # invisible head character if head space is nothing
        print("'{}'".format(word_removed_space[1:len(word)]))
        word_removed_space = remove_head_sapces(word_removed_space, spaces)
    else:
        word_removed_space = word
    return word_removed_space
