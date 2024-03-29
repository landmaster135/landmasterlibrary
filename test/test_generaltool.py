# Library by default
from pathlib import Path
import subprocess
import sys
import datetime
# Library by third party
import pytest
# Library by landmasterlibrary
from src.landmasterlibrary.config import Config
from src.landmasterlibrary.generaltool import get_str_repeated_to_mark, get_str_by_zero_padding, output_log, get_str_from_list, get_value_from_yaml, get_indices_by_seperators, get_indcies_containing_words, get_words_by_indices, get_words_by_seperators, get_src_dir_path_from_test_path, get_src_path_from_test_path, read_txt_lines, read_csv_lines, remove_spaces_at_head_and_tail, remove_tail_sapces, remove_head_sapces, replace_by_words, get_text_in_file, get_funcs_in_text, get_functions_in_python_file, get_words_in_lines_by_head_and_tail, get_str_of_head_or_tail_by_extension, get_mark_of_not_function_statement, get_mermaid_elements, append_items, remove_empty_items, get_files_by_extensions, generate_cron_from_datetime_now, print_funcs, print_depends, count_mermaid_lines, print_depends_on_mermaid

class Test_Generaltool:

    # normal system
    def test_get_str_repeated_to_mark_1_1(self):
        repeat_str = "a"
        repeat_number_to_mark = 10
        actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)
        expected = "aaaaaaaaaa"
        assert actual == expected

    # normal system
    def test_get_str_repeated_to_mark_1_2(self):
        repeat_str = "ab"
        repeat_number_to_mark = 10
        actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)
        expected = "abababababababababab"
        assert actual == expected

    # normal system
    def test_get_str_repeated_to_mark_1_3(self):
        repeat_str = "ab"
        repeat_number_to_mark = 0
        actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)
        expected = ""
        assert actual == expected

    # normal system
    def test_get_str_repeated_to_mark_2_1(self):
        repeat_str = "a"
        repeat_number_to_mark = 10
        actual = get_str_repeated_to_mark(repeat_str)
        expected = "aaaaaaaaaaaaaaa"
        assert actual == expected

    # abnormal system
    def test_get_str_repeated_to_mark_3_1(self):
        repeat_str = 123
        repeat_number_to_mark = 10
        with pytest.raises(TypeError) as e:
            actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)

    # abnormal system
    def test_get_str_repeated_to_mark_3_2(self):
        repeat_str = "a"
        repeat_number_to_mark = "10"
        with pytest.raises(TypeError) as e:
            actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)

    # abnormal system
    def test_get_str_repeated_to_mark_3_3(self):
        repeat_str = None
        repeat_number_to_mark = 10
        with pytest.raises(TypeError) as e:
            actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)

    # abnormal system
    def test_get_str_repeated_to_mark_3_4(self):
        repeat_str = "a"
        repeat_number_to_mark = None
        with pytest.raises(TypeError) as e:
            actual = get_str_repeated_to_mark(repeat_str, repeat_number_to_mark)

    # abnormal system
    def test_get_str_repeated_to_mark_3_5(self):
        repeat_str = "a"
        repeat_number_to_mark = 10
        with pytest.raises(TypeError) as e:
            actual = get_str_repeated_to_mark()

    # normal system
    def test_get_str_by_zero_padding_1_1(self):
        number = 123
        number_of_digit = 6
        actual = get_str_by_zero_padding(number, number_of_digit)
        expected = "000123"
        assert actual == expected

    # normal system
    def test_get_str_by_zero_padding_1_2(self):
        number = 12345
        number_of_digit = 2
        actual = get_str_by_zero_padding(number, number_of_digit)
        expected = "12345"
        assert actual == expected

    # normal system
    def test_get_str_by_zero_padding_1_3(self):
        number = 321
        actual = get_str_by_zero_padding(number)
        expected = "0321"
        assert actual == expected

    # normal system
    def test_get_str_by_zero_padding_1_4(self):
        number = 12345
        actual = get_str_by_zero_padding(number)
        expected = "12345"
        assert actual == expected

    # abnormal system
    def test_get_str_by_zero_padding_2_1(self):
        number = "123"
        number_of_digit = 6
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding(number, number_of_digit)

    # abnormal system
    def test_get_str_by_zero_padding_2_2(self):
        number = 12.3
        number_of_digit = 6
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding(number, number_of_digit)

    # abnormal system
    def test_get_str_by_zero_padding_3_1(self):
        number = 123
        number_of_digit = "6"
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding(number, number_of_digit)

    # abnormal system
    def test_get_str_by_zero_padding_3_2(self):
        number = 123
        number_of_digit = 6.1
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding(number, number_of_digit)

    # abnormal system
    def test_get_str_by_zero_padding_4_1(self):
        number = 123
        number_of_digit = None
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding(number, number_of_digit)

    # abnormal system
    def test_get_str_by_zero_padding_4_2(self):
        number = None
        number_of_digit = 6
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding(number, number_of_digit)

    # abnormal system
    def test_get_str_by_zero_padding_5_1(self):
        with pytest.raises(TypeError) as e:
            actual = get_str_by_zero_padding()

    # normal system
    def test_output_log_1_1(self):
        class_name = "test_class"
        function_name = "my_function"
        remark = "test_for_output."
        actual = output_log(class_name, function_name, remark)
        expected = "test_class: my_function: test_for_output."
        assert actual == expected

    # normal system
    def test_output_log_1_2(self):
        class_name = __name__
        function_name = sys._getframe().f_code.co_name
        remark = "test_for_output."
        actual = output_log(class_name, function_name, remark)
        expected = f"{class_name}: {function_name}: {remark}"
        assert actual == expected

    # normal system
    def test_output_log_2_1(self):
        class_name = "test_class"
        function_name = "my_function"
        remark = None
        actual = output_log(class_name, function_name, remark)
        expected = f"{class_name}: {function_name}: "
        assert actual == expected

    # normal system
    def test_output_log_2_2(self):
        class_name = "test_class"
        function_name = "my_function"
        actual = output_log(class_name, function_name)
        expected = f"{class_name}: {function_name}: "
        assert actual == expected

    # abnormal system
    def test_output_log_3_1(self):
        class_name = "test_class"
        with pytest.raises(TypeError) as e:
            actual = output_log(class_name)

    # abnormal system
    def test_output_log_3_2(self):
        with pytest.raises(TypeError) as e:
            actual = output_log()

    # abnormal system
    def test_output_log_3_3(self):
        class_name = "test_class"
        function_name = None
        remark = "test_for_output"
        with pytest.raises(TypeError) as e:
            actual = output_log(class_name, function_name, remark)

    # abnormal system
    def test_output_log_3_4(self):
        class_name = None
        function_name = "my_function"
        remark = "test_for_output"
        with pytest.raises(TypeError) as e:
            actual = output_log(class_name, function_name, remark)

    # normal system
    def test_get_str_from_list_1_1(self):
        target_list = [1, 2, 3]
        actual = get_str_from_list(target_list)
        expected = "[ 1,2,3 ]"
        print(actual)
        assert actual == expected

    # normal system
    def test_get_str_from_list_1_2(self):
        target_list = ["1", "2", "3"]
        actual = get_str_from_list(target_list)
        expected = "[ 1,2,3 ]"
        print(actual)
        assert actual == expected

    # normal system
    def test_get_src_dir_path_from_test_path_1_1(self):
        actual_path = get_src_dir_path_from_test_path(__file__, "src/landmasterlibrary")
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # normal system
    def test_get_src_dir_path_from_test_path_1_2(self):
        actual_path = get_src_dir_path_from_test_path(__file__, "src/landmasterlibrary", True)
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # normal system
    def test_get_src_dir_path_from_test_path_1_3(self):
        actual_path = get_src_dir_path_from_test_path(__file__, "src/landmasterlibrary", False)
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # abnormal system
    def test_get_src_dir_path_from_test_path_2_1(self):
        with pytest.raises(TypeError) as e:
            actual = get_src_dir_path_from_test_path()
        print(e.value)
        assert str(e.value) == "get_src_dir_path_from_test_path() missing 2 required positional arguments: 'calling_file_path' and 'src_folder_name'"

    # abnormal system
    def test_get_src_dir_path_from_test_path_2_2(self):
        with pytest.raises(TypeError) as e:
            actual = get_src_dir_path_from_test_path(__file__)
        print(e.value)
        assert str(e.value) == "get_src_dir_path_from_test_path() missing 1 required positional argument: 'src_folder_name'"

    # abnormal system
    def test_get_src_dir_path_from_test_path_3_1(self):
        calling_file_path = None
        src_folder_name = ""
        with pytest.raises(TypeError) as e:
            actual = get_src_dir_path_from_test_path(calling_file_path, src_folder_name)

    # abnormal system
    def test_get_src_dir_path_from_test_path_3_2(self):
        calling_file_path = ""
        src_folder_name = None
        with pytest.raises(TypeError) as e:
            actual = get_src_dir_path_from_test_path(calling_file_path, src_folder_name)

    # abnormal system
    def test_get_src_dir_path_from_test_path_4_1(self):
        test_dir_name = "test_data/pathte"
        with pytest.raises(FileNotFoundError) as e:
            actual_path = get_src_dir_path_from_test_path(__file__, test_dir_name)

    # abnormal system
    def test_get_src_dir_path_from_test_path_4_2(self):
        test_dir_name = "test_data/pathte"
        with pytest.raises(FileNotFoundError) as e:
            actual_path = get_src_dir_path_from_test_path(__file__, test_dir_name, True)

    # abnormal system
    def test_get_src_dir_path_from_test_path_5_1(self):
        test_dir_name = "test_data/for_test_read_csv_lines.csv"
        with pytest.raises(NotADirectoryError) as e:
            actual_path = get_src_dir_path_from_test_path(__file__, test_dir_name)

    # abnormal system
    def test_get_src_dir_path_from_test_path_5_2(self):
        test_dir_name = "test_data/for_test_read_csv_lines.csv"
        with pytest.raises(NotADirectoryError) as e:
            actual_path = get_src_dir_path_from_test_path(__file__, test_dir_name, True)

    # normal system
    def test_get_src_dir_path_from_test_path_6_1(self):
        test_dir_name = "test_data/pathte"
        actual_path = get_src_dir_path_from_test_path(__file__, test_dir_name, False)
        actual = actual_path.count("/")
        expected = 3
        assert actual >= expected

    # normal system
    def test_get_src_dir_path_from_test_path_7_1(self):
        test_dir_name = "test_data/pathte"
        with pytest.raises(TypeError) as e:
            actual_path = get_src_dir_path_from_test_path(__file__, test_dir_name, None)

    # normal system
    def test_get_src_path_from_test_path_1_1(self):
        test_file_name = "pathtest.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name)
        actual = actual_path.count("/")
        expected = 3
        assert actual >= expected

    # normal system
    def test_get_src_path_from_test_path_1_2(self):
        test_file_name = "pathtest.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary")
        actual = actual_path.count("/")
        expected = 3
        assert actual >= expected

    # normal system
    def test_get_src_path_from_test_path_1_3(self):
        test_file_name = "pathtest.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary", True)
        actual = actual_path.count("/")
        expected = 3
        assert actual >= expected

    # normal system
    def test_get_src_path_from_test_path_1_4(self):
        test_file_name = "pathtest.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary", False)
        actual = actual_path.count("/")
        expected = 3
        assert actual >= expected

    # abnormal system
    def test_get_src_path_from_test_path_2_1(self):
        with pytest.raises(TypeError) as e:
            actual = get_src_path_from_test_path()
        print(e.value)
        assert str(e.value) == "get_src_path_from_test_path() missing 2 required positional arguments: 'calling_file_path' and 'src_file_name'"

    # abnormal system
    def test_get_src_path_from_test_path_2_2(self):
        with pytest.raises(TypeError) as e:
            actual = get_src_path_from_test_path(__file__)
        print(e.value)
        assert str(e.value) == "get_src_path_from_test_path() missing 1 required positional argument: 'src_file_name'"

    # abnormal system
    def test_get_src_path_from_test_path_3_1(self):
        calling_file_path = None
        src_file_name = ""
        src_folder_name = ""
        with pytest.raises(TypeError) as e:
            actual = get_src_path_from_test_path(calling_file_path, src_file_name, src_folder_name)

    # abnormal system
    def test_get_src_path_from_test_path_3_2(self):
        calling_file_path = ""
        src_file_name = None
        src_folder_name = ""
        with pytest.raises(TypeError) as e:
            actual = get_src_path_from_test_path(calling_file_path, src_file_name, src_folder_name)

    # abnormal system
    def test_get_src_path_from_test_path_3_3(self):
        calling_file_path = ""
        src_file_name = ""
        src_folder_name = None
        with pytest.raises(TypeError) as e:
            actual = get_src_path_from_test_path(calling_file_path, src_file_name, src_folder_name)

    # abnormal system
    def test_get_src_path_from_test_path_4_1(self):
        test_file_name = "pathte.yml"
        with pytest.raises(FileNotFoundError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name)

    # abnormal system
    def test_get_src_path_from_test_path_4_2(self):
        test_file_name = "pathte.yml"
        with pytest.raises(FileNotFoundError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary")

    # abnormal system
    def test_get_src_path_from_test_path_4_3(self):
        test_file_name = "pathte.yml"
        with pytest.raises(FileNotFoundError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary", True)

    # abnormal system
    def test_get_src_path_from_test_path_5_1(self):
        test_file_name = "empty_dir"
        with pytest.raises(IsADirectoryError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name)

    # abnormal system
    def test_get_src_path_from_test_path_5_2(self):
        test_file_name = "empty_dir"
        with pytest.raises(IsADirectoryError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary")

    # abnormal system
    def test_get_src_path_from_test_path_5_3(self):
        test_file_name = "empty_dir"
        with pytest.raises(IsADirectoryError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name, "test_data")

    # normal system
    def test_get_src_path_from_test_path_6_1(self):
        test_file_name = "pathte.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary", False)
        actual = actual_path.count("/")
        expected = 3
        assert actual >= expected

    # normal system
    def test_get_src_path_from_test_path_7_1(self):
        test_file_name = "pathte.yml"
        with pytest.raises(TypeError) as e:
            actual_path = get_src_path_from_test_path(__file__, test_file_name, "src/landmasterlibrary", None)

    def test_read_txt_lines_1_1(self):
        read_files = ["for_test_get_func_python.py"]
        dir_name = "test_data"
        actual = read_txt_lines(__file__, read_files, dir_name)
        expected = [["class ReplaceCharacter:"
            , "    def make_voicedsound(self, text : str) -> str:"
            , "        pass"
            , ""
            , "def main():"
            , "    replace_character = ReplaceCharacter()"
            , "    sound = replace_character.make_voicedsound(\"testtest\")"
            , ""
            , "if __name__ == \"__main__\":"
            , "    main()"
        ]]
        assert actual == expected

    def test_read_txt_lines_2_1(self):
        read_files = ["for_test_get_func_python.py"]
        dir_name = "test_data"
        with pytest.raises(TypeError) as e:
            actual = read_txt_lines(None, read_files, dir_name)

    def test_read_txt_lines_2_2(self):
        read_files = None
        dir_name = "test_data"
        with pytest.raises(TypeError) as e:
            actual = read_txt_lines(__file__, read_files, dir_name)

    def test_read_txt_lines_2_3(self):
        read_files = ["for_test_get_func_python.py"]
        dir_name = None
        with pytest.raises(TypeError) as e:
            actual = read_txt_lines(__file__, read_files, dir_name)

    def test_read_txt_lines_3_1(self):
        read_files = ["for_test_get_func_python.py"]
        with pytest.raises(TypeError) as e:
            actual = read_txt_lines(__file__, read_files)

    def test_read_txt_lines_3_2(self):
        read_files = ["for_test_get_func_python.py"]
        with pytest.raises(TypeError) as e:
            actual = read_txt_lines(__file__)

    def test_read_csv_lines_1_1(self):
        read_files = ["for_test_read_csv_lines.csv"]
        dir_name = "test_data"
        actual = read_csv_lines(__file__, read_files, dir_name)
        expected = [[["id", "title", "date"]
            , ["01", "abc","2022-12-31"]
            , ["02", "def", "2025-01-08"]
            , ["890", "ert", "2100-08-10"]
        ]]
        assert actual == expected

    def test_read_csv_lines_2_1(self):
        read_files = ["for_test_read_csv_lines.csv"]
        dir_name = "test_data"
        with pytest.raises(TypeError) as e:
            actual = read_csv_lines(None, read_files, dir_name)

    def test_read_csv_lines_2_2(self):
        read_files = None
        dir_name = "test_data"
        with pytest.raises(TypeError) as e:
            actual = read_csv_lines(__file__, read_files, dir_name)

    def test_read_csv_lines_2_3(self):
        read_files = ["for_test_read_csv_lines.csv"]
        dir_name = None
        with pytest.raises(TypeError) as e:
            actual = read_csv_lines(__file__, read_files, dir_name)

    def test_read_csv_lines_3_1(self):
        read_files = ["for_test_read_csv_lines.csv"]
        with pytest.raises(TypeError) as e:
            actual = read_csv_lines(__file__, read_files)

    def test_read_csv_lines_3_2(self):
        read_files = ["for_test_read_csv_lines.csv"]
        with pytest.raises(TypeError) as e:
            actual = read_csv_lines(__file__)

    # normal system
    # def test_get_obj_from_yaml_1_1(self):
    #     actual = get_obj_from_yaml(
    #         get_src_path_from_test_path(__file__, config_file_name)
    #     )
    #     expected = {"a": "testtest", "b": "testtest2"}
    #     self.assertEqual(type(expected), type(actual))

    # # abnormal system
    # def test_get_obj_from_yaml_2_1(self):
    #     errorMsg = get_value_from_yaml(
    #         get_src_path_from_test_path(__file__, config_file_name),
    #         "msg_obj_e0101"
    #     )
    #     # TODO: configFileNameをテスト用のファイルに直す。
    #     with self.assertRaises(FileNotFoundError, msg=errorMsg):
    #         errorMsg = get_obj_from_yaml(
    #             str(Path(__file__).parent / "src" / config_file_name)
    #         )

    # # normal system
    # def test_get_value_from_yaml_1_1(self):
    #     actual = get_value_from_yaml(
    #         get_src_path_from_test_path(__file__, config_file_name),
    #         "testField"
    #     )
    #     expected = "testtest"
    #     assert actual == expected
    #     # self.assertEqual(expected, actual)

    # # abnormal system
    # def test_get_value_from_yaml_2_1(self):
    #     errorMsg = get_value_from_yaml(
    #         get_src_path_from_test_path(__file__, config_file_name),
    #         "msgObj_E0101"
    #     )
    #     # TODO: configFileNameをテスト用のファイルに直す。
    #     with self.assertRaises(FileNotFoundError, msg=errorMsg):
    #         errorMsg = get_value_from_yaml(
    #             str(Path(__file__).parent / "src" / config_file_name),
    #             "msgObj_E0101"
    #         )
    #         # actual = get_value_from_yaml(
    #         #     get_src_path_from_test_path(__file__, config_file_name),
    #         #     "testFielddddddd"
    #         # )

    # # semi-normal system
    # def test_get_value_from_yaml_2_2(self):
    #     errorMsg = get_value_from_yaml(
    #         get_src_path_from_test_path(__file__, config_file_name),
    #         "msgObj_E0102"
    #     )
    #     # TODO: configFileNameをテスト用のファイルに直す。
    #     with self.assertRaises(ValueError, msg=errorMsg):
    #         actual = get_value_from_yaml(
    #             get_src_path_from_test_path(__file__, config_file_name),
    #             "testFielddddddd"
    #         )

    def test_get_indices_by_seperators_1_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        seperators = Config.seperators
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [6, 16, 26, 30]
        assert actual == expected

    def test_get_indices_by_seperators_1_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        seperators = Config.seperators
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [9, 27, 46]
        assert actual == expected

    def test_get_indices_by_seperators_1_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        seperators = Config.seperators
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [6]
        assert actual == expected

    def test_get_indices_by_seperators_2_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        seperators = Config.spaces
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [7, 15, 17, 25, 30]
        assert actual == expected

    def test_get_indices_by_seperators_2_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        seperators = Config.spaces
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [8, 18, 25, 26, 28, 36, 45, 46]
        assert actual == expected

    def test_get_indices_by_seperators_2_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        seperators = Config.spaces
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [0, 6]
        assert actual == expected

    def test_get_indices_by_seperators_3_1(self):
        keyword = "cdf"
        seperators = ["cde"]
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [3]
        assert actual == expected

    def test_get_indcies_containing_words_1_1(self):
        target_list = ["abcde", "cde", "cdf"]
        words = ["cde"]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0, 1]
        assert actual == expected

    def test_get_indcies_containing_words_1_2(self):
        target_list = ["abcde", "cde", "cdf", "ert"]
        words = ["cde", "ert"]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0, 1, 3]
        assert actual == expected

    def test_get_indcies_containing_words_1_3(self):
        target_list = ["abcde", "cdert", "cdf", "ert"]
        words = ["cde", "ert"]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0, 1, 3]
        assert actual == expected

    def test_get_indcies_containing_words_2_1(self):
        target_list = ["ab5de", 5, "cdf"]
        words = ["5"]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0, 1]
        assert actual == expected

    def test_get_indcies_containing_words_2_2(self):
        target_list = ["ab56de", 5, "cdf"]
        words = [56]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0]
        assert actual == expected

    def test_get_indcies_containing_words_2_3(self):
        target_list = ["ab234", 234, 2340, "c23df", 234.1]
        words = [234]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0, 1, 2, 4]
        assert actual == expected

    def test_get_indcies_containing_words_2_4(self):
        target_list = [0.234, 2.34]
        words = [234]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0]
        assert actual == expected

    def test_get_indcies_containing_words_2_5(self):
        target_list = ["False", False, "false", True]
        words = [False]
        actual = get_indcies_containing_words(target_list, words)
        expected = [0, 1]
        assert actual == expected

    def test_get_indcies_containing_words_3_1(self):
        target_list = "abcde"
        words = ["cde"]
        with pytest.raises(TypeError) as e:
            actual = get_indcies_containing_words(target_list, words)

    def test_get_indcies_containing_words_3_2(self):
        target_list = ["abcde", "cde", "cdf"]
        words = "cde"
        with pytest.raises(TypeError) as e:
            actual = get_indcies_containing_words(target_list, words)

    def test_get_indcies_containing_words_4_1(self):
        target_list = None
        words = ["cde"]
        with pytest.raises(TypeError) as e:
            actual = get_indcies_containing_words(target_list, words)

    def test_get_indcies_containing_words_4_2(self):
        target_list = ["abcde", "cde", "cdf"]
        words = None
        with pytest.raises(TypeError) as e:
            actual = get_indcies_containing_words(target_list, words)

    def test_get_indcies_containing_words_5_1(self):
        target_list = "abcde"
        words = ["cde"]
        with pytest.raises(TypeError) as e:
            actual = get_indcies_containing_words(target_list)

    def test_get_indcies_containing_words_5_2(self):
        target_list = ["abcde", "cde", "cdf"]
        words = "cde"
        with pytest.raises(TypeError) as e:
            actual = get_indcies_containing_words()

    def test_get_words_by_indices_1_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        indices = [6, 16, 26, 30]
        actual = get_words_by_indices(keyword, indices)
        expected = ["python", " node.js ", " gollila ", "web"]
        assert actual == expected

    def test_get_words_by_indices_1_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        indices = [9, 27, 46]
        actual = get_words_by_indices(keyword, indices)
        expected = ["Internet　", "Creative Coding  ", "　Machine Learning "]
        assert actual == expected

    def test_get_words_by_indices_1_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        indices = [6]
        actual = get_words_by_indices(keyword, indices)
        expected = [' Flask']
        assert actual == expected

    def test_get_words_by_seperators_1_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        actual = get_words_by_seperators(keyword)
        expected = ["python", "node.js", "gollila", "web"]
        assert actual == expected

    def test_get_words_by_seperators_1_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        actual = get_words_by_seperators(keyword)
        expected = ["Internet", "Creative Coding", "Machine Learning"]
        assert actual == expected

    def test_get_words_by_seperators_1_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        actual = get_words_by_seperators(keyword)
        expected = ['Flask']
        assert actual == expected

    def test_remove_tail_sapces_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        # spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, Config.spaces)
        expected = "   　　　　　　　      　　   node.js"
        assert actual == expected

    def test_remove_tail_sapces_1_2(self):
        keyword  = "# generaltool.py"
        # spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, Config.spaces)
        expected = "# generaltool.py"
        assert actual == expected

    def test_remove_tail_sapces_1_3(self):
        keyword  = ""
        # spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, Config.spaces)
        expected = ""
        assert actual == expected

    def test_remove_head_sapces_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        # spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, Config.spaces)
        expected =                             "node.js    　　　　　  　　　　  "
        assert actual == expected

    def test_remove_head_sapces_1_2(self):
        keyword  = "# generaltool.py"
        # spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, Config.spaces)
        expected = "# generaltool.py"
        assert actual == expected

    def test_remove_head_sapces_1_3(self):
        keyword  = ""
        # spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, Config.spaces)
        expected = ""
        assert actual == expected

    def test_get_files_by_extensions_1_1(self):
        target_dir = get_src_dir_path_from_test_path(__file__, "test_data", True)
        # target_dir = Path().cwd()
        extensions = [".csv"]
        actual = get_files_by_extensions(target_dir, extensions)
        expected = ["for_test_read_csv_lines.csv"]
        assert actual == expected

    def test_get_files_by_extensions_1_2(self):
        target_dir = get_src_dir_path_from_test_path(__file__, "test_data", True)
        extensions = [".py"]
        actual = get_files_by_extensions(target_dir, extensions)
        expected = ["for_test_get_func_python.py", "for_test_get_files_by_extensions.js.py"]
        assert len(actual) == len(expected)
        assert set(actual) == set(expected)

    def test_get_files_by_extensions_1_3(self):
        target_dir = "./"
        extensions = [".py"]
        actual = get_files_by_extensions(target_dir, extensions)
        expected = ["setup.py"]
        assert actual == expected

    def test_get_files_by_extensions_2_1(self):
        extensions = [".csv"]
        with pytest.raises(TypeError) as e:
            actual = get_files_by_extensions()

    def test_get_files_by_extensions_2_2(self):
        extensions = None
        with pytest.raises(TypeError) as e:
            actual = get_files_by_extensions(extensions)

    def test_get_files_by_extensions_2_3(self):
        extensions = [".csv",  None]
        with pytest.raises(TypeError) as e:
            actual = get_files_by_extensions(extensions)

    # normal system
    def test_remove_spaces_at_head_and_tail_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        # spaces = [" ", "　"]
        actual = remove_spaces_at_head_and_tail(keyword, Config.spaces)
        expected = "node.js"
        assert actual == expected

    # normal system
    def test_replace_by_words_1_1(self):
        keyword  = "Salesforce ソリューションキット: :クイ\"ック/ルック"
        actual = replace_by_words(keyword)
        expected = "Salesforce ソリューションキット： ：クイ”ック／ルック"
        assert actual == expected

    # normal system
    def test_replace_by_words_1_2(self):
        keyword  = "Salesforce ソリューションキット: クイックルック"
        actual = replace_by_words(keyword)
        expected = "Salesforce ソリューションキット： クイックルック"
        assert actual == expected

    # normal system
    def test_replace_by_words_2_1(self):
        keyword  = "Salesforce ソリュ$ーショ$ンキット: :クイック\"ルック"
        actual = replace_by_words(keyword, {"$": "dollar"})
        expected = "Salesforce ソリュdollarーショdollarンキット: :クイック\"ルック"
        assert actual == expected

    # abnormal system
    def test_replace_by_words_3_1(self):
        keyword  = 123
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words(keyword, {"$": "dollar"})

    # abnormal system
    def test_replace_by_words_3_2(self):
        keyword  = 123
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words(keyword)

    # abnormal system
    def test_replace_by_words_4_1(self):
        keyword  = True
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words(keyword, {"$": "dollar"})

    # abnormal system
    def test_replace_by_words_4_2(self):
        keyword  = True
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words(keyword)

    # abnormal system
    def test_replace_by_words_5_1(self):
        keyword  = None
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words(keyword, {"$": "dollar"})

    # abnormal system
    def test_replace_by_words_5_2(self):
        keyword  = None
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words(keyword)

    # abnormal system
    def test_replace_by_words_6_1(self):
        keyword  = None
        with pytest.raises(TypeError) as e:
            actual = replace_by_words()

    # abnormal system
    def test_replace_by_words_7_1(self):
        with pytest.raises(AttributeError) as e:
            actual = replace_by_words({"$": "dollar"})

    # normal system
    def test_replace_by_words_8_1(self):
        keyword  = "123"
        actual = replace_by_words(keyword, {"$": "dollar"})
        expected = "123"
        assert actual == expected

    # normal system
    def test_replace_by_words_8_2(self):
        keyword  = "123"
        actual = replace_by_words(keyword)
        expected = "123"
        assert actual == expected

    # normal system for Python
    def test_get_text_in_file_1_1(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        actual = get_text_in_file(file_full_name)
        expected = 11
        assert len(actual.split("\n")) == expected

    # normal system for Python
    def test_get_text_in_file_1_2(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_javascript.js", "test_data")
        actual = get_text_in_file(file_full_name)
        expected = 29
        assert len(actual.split("\n")) == expected

     # normal system for Python
    def test_get_text_in_file_1_3(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_files_by_extensions.js.py", "test_data")
        actual = get_text_in_file(file_full_name)
        expected = 10
        assert len(actual.split("\n")) == expected

    def test_get_funcs_in_text_1_1(self):
        funcs = ["test_replace", "test_add"]
        text = "    replace = test_replace()"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_replace"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_1_2(self):
        funcs = ["test_replace", "test_add", "test_minus"]
        text = "    replace = test_minus()"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_minus"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_1_3(self):
        funcs = ["test_replace", "test_add", "test_minus"]
        text = "    replace = test_minus() + test_add(number)"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_minus", "test_add"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_1_4(self):
        funcs = ["test_replace", "test_add", "test_minus"]
        text = "replace = test_minus() + test_add(number)"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_minus", "test_add"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_1_5(self):
        funcs = ["test_replace", "test_add"]
        text = "replace = test_minus() + test_add(number)"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_add"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_1_6(self):
        funcs = ["test_replace", "test_add"]
        text = "replace = TestClass.test_add(number)"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_add"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_1_7(self):
        funcs = ["test_replace", "test_add"]
        text = "replace = Test_replace.test_add(number)"
        actual = get_funcs_in_text(funcs, text)
        expected = ["test_add"]
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_2_1(self):
        funcs = ["test_replace", "test_add", "test_minus"]
        text = "    replace = test_multiple()"
        actual = get_funcs_in_text(funcs, text)
        expected = []
        assert set(actual) == set(expected)

    def test_get_funcs_in_text_2_2(self):
        funcs = ["test_replace", "test_add", "test_minus"]
        text = "replace = test_multiple()"
        actual = get_funcs_in_text(funcs, text)
        expected = []
        assert set(actual) == set(expected)

    # normal system for Python
    def test_get_functions_in_python_file_1_1(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        actual = get_functions_in_python_file(file_full_name)
        expected = ["make_voicedsound", "main"]
        assert set(actual) == set(expected)

     # normal system for Python
    def test_get_functions_in_python_file_1_2(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        actual = get_functions_in_python_file(file_full_name, "def ", "(")
        expected = ["make_voicedsound", "main"]
        assert set(actual) == set(expected)

    # normal system for JavaScript (ECMAScript)
    def test_get_functions_in_python_file_2_1(self):
        # TODO
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_javascript.js", "test_data")
        actual = get_functions_in_python_file(file_full_name, "function ", "(")
        expected = ["getFolderIdArray", "testtest", "main"]
        assert set(actual) == set(expected)

    # normal system
    def test_get_words_in_lines_by_head_and_tail_1_1(self):
        lines = ["class ReplaceCharacter:", "    def make_voicedsound(self, text : str) -> str:", "        pass", "def main():", "    replace_character = ReplaceCharacter()", "if __name__ == \"__main__\":", "    main()"]
        head = "def "
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = ["make_voicedsound", "main"]
        assert actual == expected

    def test_get_words_in_lines_by_head_and_tail_2_1(self):
        lines = ["    def make_voicedsound(text : str) -> str:"]
        head = "def "
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = ["make_voicedsound"]
        assert actual == expected

    def test_get_words_in_lines_by_head_and_tail_2_2(self):
        lines = ["def make_voicedsound(text : str) -> str:"]
        head = "def "
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = ["make_voicedsound"]
        assert actual == expected

    def test_get_words_in_lines_by_head_and_tail_2_3(self):
        lines = ["    def make_voicedsound(text : str) -> str:"]
        head = "function"
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = []
        assert actual == expected

    def test_get_words_in_lines_by_head_and_tail_2_4(self):
        lines = ["def make_voicedsound(text : str) -> str:"]
        head = "function"
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = []
        assert actual == expected

    def test_get_words_in_lines_by_head_and_tail_2_5(self):
        lines = ["class ReplaceCharacter:", "    def make_voicedsound(self, text : str) -> str:", "        pass", "def main():", "    replace_character = ReplaceCharacter()", "if __name__ == \"__main__\":", "    main()"]
        head = "function"
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = []
        assert actual == expected

    def test_get_words_in_lines_by_head_and_tail_2_6(self):
        lines = ["class ReplaceCharacter:", "    def make_voicedsound(self, text : str) -> str:", "        pass", "def main():", "    replace_character = ReplaceCharacter()", "if __name__ == \"__main__\":", "    main()"]
        head = "def "
        tail = "function"
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = []
        assert actual == expected

    def test_get_str_of_head_or_tail_by_extension_1_1(self):
        extension = ".py"
        head_or_tail = "head"
        actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        expected = "def "
        assert actual == expected

    def test_get_str_of_head_or_tail_by_extension_1_2(self):
        extension = ".py"
        head_or_tail = "tail"
        actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        expected = "("
        assert actual == expected

    def test_get_str_of_head_or_tail_by_extension_1_3(self):
        extension = ".js"
        head_or_tail = "head"
        actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        expected = "function "
        assert actual == expected

    def test_get_str_of_head_or_tail_by_extension_1_4(self):
        extension = ".js"
        head_or_tail = "tail"
        actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        expected = "("
        assert actual == expected

    def test_get_str_of_head_or_tail_by_extension_2_1(self):
        extension = ".py"
        head_or_tail = "body"
        with pytest.raises(AttributeError) as e:
            actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        assert str(e.value) == "head_or_tail must be 'head' or 'tail'."

    def test_get_str_of_head_or_tail_by_extension_2_2(self):
        extension = ".js"
        head_or_tail = "body"
        with pytest.raises(AttributeError) as e:
            actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        assert str(e.value) == "head_or_tail must be 'head' or 'tail'."

    def test_get_str_of_head_or_tail_by_extension_2_3(self):
        with pytest.raises(TypeError) as e:
            actual = get_str_of_head_or_tail_by_extension()
        assert str(e.value) == "get_str_of_head_or_tail_by_extension() missing 1 required positional argument: 'extension'"

    def test_get_str_of_head_or_tail_by_extension_2_4(self):
        extension = ".lua"
        head_or_tail = "head"
        with pytest.raises(AttributeError) as e:
            actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        assert str(e.value) == f"'{extension}' is not supported."

    def test_get_str_of_head_or_tail_by_extension_2_5(self):
        extension = ".lua"
        head_or_tail = "tail"
        with pytest.raises(AttributeError) as e:
            actual = get_str_of_head_or_tail_by_extension(extension, head_or_tail)
        assert str(e.value) == f"'{extension}' is not supported."

    def test_get_mark_of_not_function_statement_1_1(self):
        extension = ".py"
        actual = get_mark_of_not_function_statement(extension)
        expected = "if __name__ == \"__main__\":"
        assert actual == expected

    def test_get_mark_of_not_function_statement_1_2(self):
        extension = ".js"
        actual = get_mark_of_not_function_statement(extension)
        expected = "}"
        assert actual == expected

    def test_get_mark_of_not_function_statement_2_1(self):
        extension = ".lua"
        with pytest.raises(AttributeError) as e:
            actual = get_mark_of_not_function_statement(extension)
        assert str(e.value) == f"'{extension}' is not supported."

    def test_get_mermaid_elements_1_1(self):
        prefix_or_suffix = "prefix"
        actual = get_mermaid_elements(prefix_or_suffix)
        expected = ["```mermaid", "classDiagram"]
        assert actual == expected

    def test_get_mermaid_elements_1_2(self):
        prefix_or_suffix = "suffix"
        actual = get_mermaid_elements(prefix_or_suffix)
        expected = ["```"]
        assert actual == expected

    def test_get_mermaid_elements_2_1(self):
        prefix_or_suffix = "fix"
        with pytest.raises(AttributeError) as e:
            actual = get_mermaid_elements(prefix_or_suffix)
        assert str(e.value) == f"'prefix_or_suffix' must be 'prefix' or 'suffix'."


    def test_append_items_1_1(self):
        read_txt_lines = ["a", "b", "c"]
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        index_of_workflow_dispatch = 1
        actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)
        expected = ["a", "  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru", "b", "c"]
        assert actual == expected

    def test_append_items_1_2(self):
        read_txt_lines = ["a", "b", "c"]
        cron_lines = []
        index_of_workflow_dispatch = 1
        actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)
        expected = ["a", "b", "c"]
        assert actual == expected

    def test_append_items_1_3(self):
        read_txt_lines = []
        print(read_txt_lines)
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        index_of_workflow_dispatch = 0
        actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)
        expected = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        assert actual == expected

    def test_append_items_1_4(self):
        read_txt_lines = ["a", "b", "c"]
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        index_of_workflow_dispatch = 0
        actual = append_items(read_txt_lines, cron_lines)
        expected = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru", "a", "b", "c"]
        assert actual == expected

    def test_append_items_1_5(self):
        read_txt_lines = ["a", "b", "c"]
        cron_lines = ["d", "e"]
        index_of_workflow_dispatch = 3
        actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)
        expected = ["a", "b", "c", "d", "e"]
        assert actual == expected

    def test_append_items_2_1(self):
        read_txt_lines = ["a", "b", "c"]
        index_of_workflow_dispatch = -1
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        with pytest.raises(IndexError) as e:
            actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)
        print(e.value)
        assert str(e.value) == "IndexError: target_index must be more than or equal to 0."

    def test_append_items_2_2(self):
        read_txt_lines = None
        index_of_workflow_dispatch = 0
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        with pytest.raises(TypeError) as e:
            actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)

    def test_append_items_2_3(self):
        read_txt_lines = ["a", "b", "c"]
        index_of_workflow_dispatch = None
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        with pytest.raises(TypeError) as e:
            actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)

    def test_append_items_2_4(self):
        read_txt_lines = ["a", "b", "c"]
        index_of_workflow_dispatch = 0
        cron_lines = None
        with pytest.raises(TypeError) as e:
            actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)

    def test_append_items_2_5(self):
        read_txt_lines = ["a", "b", "c"]
        index_of_workflow_dispatch = 4
        cron_lines = ["  schedule:", "  - cron: '* 19 * * *'  # At 04:00. – https://crontab.guru"]
        with pytest.raises(IndexError) as e:
            actual = append_items(read_txt_lines, cron_lines, index_of_workflow_dispatch)

    def test_remove_empty_items_1_1(self):
        target_list = ["a", "", "b", "c", ""]
        actual = remove_empty_items(target_list)
        expected = ["a", "b", "c"]
        assert actual == expected

    def test_remove_empty_items_1_2(self):
        target_list = ["a", "b", "c"]
        actual = remove_empty_items(target_list)
        expected = ["a", "b", "c"]
        assert actual == expected

    def test_remove_empty_items_1_3(self):
        target_list = ["", "", ""]
        actual = remove_empty_items(target_list)
        expected = []
        assert actual == expected

    def test_remove_empty_items_2_1(self):
        target_list = None
        with pytest.raises(TypeError) as e:
            actual = remove_empty_items(target_list)

    def test_remove_empty_items_2_2(self):
        target_list = "abc"
        with pytest.raises(TypeError) as e:
            actual = remove_empty_items(target_list)

    def test_remove_empty_items_3_1(self):
        with pytest.raises(TypeError) as e:
            actual = remove_empty_items()

    def test_remove_empty_items_11_1(self):
        target_list = ["a", "", "b", "c", ""]
        actual = remove_empty_items(target_list, [""])
        expected = ["a", "b", "c"]
        assert actual == expected

    def test_remove_empty_items_11_2(self):
        target_list = ["a", "", "b", "c", "a"]
        actual = remove_empty_items(target_list, ["a"])
        expected = ["", "b", "c"]
        assert actual == expected

    def test_remove_empty_items_11_3(self):
        target_list = ["a", "", "b", "c", "a"]
        actual = remove_empty_items(target_list, ["", "a"])
        expected = ["b", "c"]
        assert actual == expected

    def test_remove_empty_items_11_4(self):
        target_list = [11, 12, "", 13, 14, 12, 15]
        actual = remove_empty_items(target_list, ["", 12])
        expected = [11, 13, 14, 15]
        assert actual == expected

    def test_remove_empty_items_12_1(self):
        target_list = ["a", "", "b", "c", ""]
        target_items = None
        with pytest.raises(TypeError) as e:
            actual = remove_empty_items(target_list, target_items)

    @pytest.mark.freeze_time("2022-01-12 13:23:43")
    def test_generate_cron_from_datetime_now_1_1(self):
        minutes_scheduled_later = 10
        time_difference = 0
        actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)
        expected_hours = 13
        expected_minutes = 33
        expected = f"{expected_minutes} {expected_hours} * * *"
        assert actual == expected

    @pytest.mark.freeze_time("2022-01-12 13:53:43")
    def test_generate_cron_from_datetime_now_1_2(self):
        minutes_scheduled_later = 10
        time_difference = 0
        actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)
        expected_hours = 14
        expected_minutes = 3
        expected = f"{expected_minutes} {expected_hours} * * *"
        assert actual == expected

    @pytest.mark.freeze_time("2022-01-12 23:53:43")
    def test_generate_cron_from_datetime_now_1_3(self):
        minutes_scheduled_later = 10
        time_difference = 0
        actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)
        expected_hours = 0
        expected_minutes = 3
        expected = f"{expected_minutes} {expected_hours} * * *"
        assert actual == expected

    @pytest.mark.freeze_time("2022-01-12 13:23:43")
    def test_generate_cron_from_datetime_now_2_1(self):
        minutes_scheduled_later = 10
        time_difference = 2
        actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)
        expected_hours = 15
        expected_minutes = 33
        expected = f"{expected_minutes} {expected_hours} * * *"
        assert actual == expected

    @pytest.mark.freeze_time("2022-01-12 13:23:43")
    def test_generate_cron_from_datetime_now_2_2(self):
        minutes_scheduled_later = 10
        time_difference = -2
        actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)
        expected_hours = 11
        expected_minutes = 33
        expected = f"{expected_minutes} {expected_hours} * * *"
        assert actual == expected

    @pytest.mark.freeze_time("2022-01-12 13:23:43")
    def test_generate_cron_from_datetime_now_3_1(self):
        minutes_scheduled_later = 10
        actual = generate_cron_from_datetime_now(minutes_scheduled_later)
        expected_hours = 13
        expected_minutes = 33
        expected = f"{expected_minutes} {expected_hours} * * *"
        assert actual == expected

    @pytest.mark.freeze_time("2022-01-12 23:53:43")
    def test_generate_cron_from_datetime_now_4_1(self):
        minutes_scheduled_later = "10"
        time_difference = 0
        with pytest.raises(TypeError) as e:
            actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)

    @pytest.mark.freeze_time("2022-01-12 23:53:43")
    def test_generate_cron_from_datetime_now_4_2(self):
        minutes_scheduled_later = 10
        time_difference = "0"
        with pytest.raises(TypeError) as e:
            actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)

    @pytest.mark.freeze_time("2022-01-12 23:53:43")
    def test_generate_cron_from_datetime_now_4_3(self):
        minutes_scheduled_later = None
        time_difference = 0
        with pytest.raises(TypeError) as e:
            actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)

    @pytest.mark.freeze_time("2022-01-12 23:53:43")
    def test_generate_cron_from_datetime_now_4_4(self):
        minutes_scheduled_later = 10
        time_difference = None
        with pytest.raises(TypeError) as e:
            actual = generate_cron_from_datetime_now(minutes_scheduled_later, time_difference)

    @pytest.mark.freeze_time("2022-01-12 23:53:43")
    def test_generate_cron_from_datetime_now_5_1(self):
        with pytest.raises(TypeError) as e:
            actual = generate_cron_from_datetime_now()

    def test_printfunc_1_1(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, "", ""])
        actual = print_funcs()
        expected = ["make_voicedsound", "main"]
        assert set(actual) == set(expected)

    def test_printfunc_1_2(self, mocker):
        file_full_name = "./test_data/for_test_get_func_python.py"
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, ".py", ""])
        actual = print_funcs()
        expected = ["make_voicedsound", "main"]
        assert set(actual) == set(expected)

    def test_printfunc_1_3(self, mocker):
        file_full_name = "./test_data/for_test_get_func_python.py"
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, ".py", ""])
        actual = print_funcs()
        expected = ["make_voicedsound", "main"]
        assert set(actual) == set(expected)

    def test_printfunc_1_4(self, mocker):
        file_full_name = "./test_data/for_test_get_func_python.py"
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, ".py", "*"])
        actual = print_funcs()
        expected = ["* make_voicedsound", "* main"]
        assert set(actual) == set(expected)

    def test_printfunc_2_1(self, mocker):
        file_full_name = "./test_data/for_test_get_func_javascript.js"
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, ".js", ""])
        actual = print_funcs()
        expected = ["getFolderIdArray", "testtest", "main"]
        assert set(actual) == set(expected)

    def test_printfunc_2_2(self, mocker):
        file_full_name = "./test_data/for_test_get_func_javascript.js"
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, ".js", "-"])
        actual = print_funcs()
        expected = ["- getFolderIdArray", "- testtest", "- main"]
        assert set(actual) == set(expected)

    def test_print_depends_1_1(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        mocker.patch.object(sys, "argv", ["printdepends", file_full_name, ".py", ""])
        actual = print_depends()
        expected = {"main": ["make_voicedsound"], "make_voicedsound": []}
        assert actual == expected

    def test_print_depends_1_2(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_javascript.js", "test_data")
        mocker.patch.object(sys, "argv", ["printdepends", file_full_name, ".js", ""])
        actual = print_depends()
        expected = {"getFolderIdArray": [], "testtest": [], "main": ["getFolderIdArray"]}
        assert actual == expected

    def test_count_mermaid_lines_1_1(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        mocker.patch.object(sys, "argv", ["printdepends", file_full_name, ".py", ""])
        depends = print_depends()
        prefix_elements = ["```mermaid", "classDiagram"]
        suffix_elements = ["```"]
        actual = count_mermaid_lines(depends, prefix_elements, suffix_elements)
        expected = 8
        assert actual == expected

    def test_print_depends_on_mermaid_1_1(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        mocker.patch.object(sys, "argv", ["print_depends_on_mermaid", file_full_name, ".py", ""])
        actual = print_depends_on_mermaid()
        mocker.patch.object(sys, "argv", ["printdepends", file_full_name, ".py", ""])
        depends = print_depends()
        prefix_elements = ["```mermaid", "classDiagram"]
        suffix_elements = ["```"]
        expected = count_mermaid_lines(depends, prefix_elements, suffix_elements)
        assert len(actual) == expected

    def test_print_depends_on_mermaid_1_2(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        mocker.patch.object(sys, "argv", ["print_depends_on_mermaid", file_full_name, ".py", ""])
        actual = print_depends_on_mermaid()
        prefix_elements = ["```mermaid", "classDiagram"]
        suffix_elements = ["```"]
        expected = [* prefix_elements, '  make_voicedsound <|-- main', '  class make_voicedsound{', '  }', '  class main{', '  }', * suffix_elements]
        assert list(actual) == list(expected)

    def test_print_depends_on_mermaid_1_3(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_javascript.js", "test_data")
        mocker.patch.object(sys, "argv", ["print_depends_on_mermaid", file_full_name, ".js", ""])
        actual = print_depends_on_mermaid()
        mocker.patch.object(sys, "argv", ["printdepends", file_full_name, ".js", ""])
        depends = print_depends()
        prefix_elements = ["```mermaid", "classDiagram"]
        suffix_elements = ["```"]
        expected = count_mermaid_lines(depends, prefix_elements, suffix_elements)
        assert len(actual) == expected

    def test_print_depends_on_mermaid_1_4(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_javascript.js", "test_data")
        mocker.patch.object(sys, "argv", ["print_depends_on_mermaid", file_full_name, ".js", ""])
        actual = print_depends_on_mermaid()
        prefix_elements = ["```mermaid", "classDiagram"]
        suffix_elements = ["```"]
        expected = [* prefix_elements, '  getFolderIdArray <|-- main', '  class getFolderIdArray{', '  }', '  class testtest{', '  }',  '  class main{', '  }', * suffix_elements]
        assert list(actual) == list(expected)
