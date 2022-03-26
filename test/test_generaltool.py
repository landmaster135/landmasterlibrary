# Library by default
from pathlib import Path
import subprocess
import sys
# Library by third party
import pytest
# Library by landmasterlibrary
from src.landmasterlibrary.config import Config
from src.landmasterlibrary.generaltool import get_value_from_yaml, get_indices_by_seperators, get_words_by_indices, get_words_by_seperators, get_src_path_from_test_path, remove_spaces_at_head_and_tail, remove_tail_sapces, remove_head_sapces, get_functions_in_python_file, get_words_in_lines_by_head_and_tail, printfunc

class Test_Generaltool:

    # normal system
    def test_get_src_path_from_test_path_1_1(self):
        test_file_name = "pathtest.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name)
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # normal system
    def test_get_src_path_from_test_path_1_2(self):
        test_file_name = "pathtest.yml"
        actual_path = get_src_path_from_test_path(__file__, test_file_name, "src")
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # abnormal system
    def test_get_src_path_from_test_path_2_1(self):
        with pytest.raises(Exception) as e:
            actual = get_src_path_from_test_path()
            expected = 2
        print(e.value)
        assert str(e.value) == "get_src_path_from_test_path() missing 2 required positional arguments: 'calling_file_path' and 'src_file_name'"

    # abnormal system
    def test_get_src_path_from_test_path_2_2(self):
        with pytest.raises(Exception) as e:
            actual = get_src_path_from_test_path(__file__)
            expected = 2
        print(e.value)
        assert str(e.value) == "get_src_path_from_test_path() missing 1 required positional argument: 'src_file_name'"

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

    # normal system
    def test_get_indices_by_seperators_1_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        seperators = Config.seperators
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [6, 16, 26, 30]
        assert actual == expected

    # normal system
    def test_get_words_by_indices_1_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        indices = [6, 16, 26, 30]
        actual = get_words_by_indices(keyword, indices)
        expected = ["python", " node.js ", " gollila ", "web"]
        assert actual == expected

    # normal system
    def test_get_words_by_seperators_1_1(self):
        keyword = "python, node.js 、 gollila ,web"
        # spaces = [" ", "　"]
        actual = get_words_by_seperators(keyword)
        expected = ["python", "node.js", "gollila", "web"]
        assert actual == expected

    # normal system
    def test_get_indices_by_seperators_1_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        seperators = Config.seperators
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [9, 27, 46]
        assert actual == expected

    # normal system
    def test_get_words_by_indices_1_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        indices = [9, 27, 46]
        actual = get_words_by_indices(keyword, indices)
        expected = ["Internet　", "Creative Coding  ", "　Machine Learning "]
        assert actual == expected

    # normal system
    def test_get_words_by_seperators_1_2(self):
        keyword = "Internet　、Creative Coding  ,　Machine Learning "
        # spaces = [" ", "　"]
        actual = get_words_by_seperators(keyword)
        expected = ["Internet", "Creative Coding", "Machine Learning"]
        assert actual == expected

    # normal system
    def test_get_indices_by_seperators_1_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        seperators = Config.seperators
        actual = get_indices_by_seperators(keyword, seperators)
        expected = [6]
        assert actual == expected

    # normal system
    def test_get_words_by_indices_1_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        indices = [6]
        actual = get_words_by_indices(keyword, indices)
        expected = [' Flask']
        assert actual == expected

    # normal system
    def test_get_words_by_seperators_1_3(self):
        keyword = " Flask"
        # spaces = [" ", "　"]
        actual = get_words_by_seperators(keyword)
        expected = ['Flask']
        assert actual == expected

    # normal system
    def test_remove_tail_sapces_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        # spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, Config.spaces)
        expected = "   　　　　　　　      　　   node.js"
        assert actual == expected

    # normal system
    def test_remove_tail_sapces_1_2(self):
        keyword  = "# generaltool.py"
        # spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, Config.spaces)
        expected = "# generaltool.py"
        assert actual == expected

    # normal system
    def test_remove_tail_sapces_1_3(self):
        keyword  = ""
        # spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, Config.spaces)
        expected = ""
        assert actual == expected

    # normal system
    def test_remove_head_sapces_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        # spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, Config.spaces)
        expected =                             "node.js    　　　　　  　　　　  "
        assert actual == expected

    # normal system
    def test_remove_head_sapces_1_2(self):
        keyword  = "# generaltool.py"
        # spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, Config.spaces)
        expected = "# generaltool.py"
        assert actual == expected

    # normal system
    def test_remove_head_sapces_1_3(self):
        keyword  = ""
        # spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, Config.spaces)
        expected = ""
        assert actual == expected

    # normal system
    def test_remove_spaces_at_head_and_tail_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        # spaces = [" ", "　"]
        actual = remove_spaces_at_head_and_tail(keyword, Config.spaces)
        expected = "node.js"
        assert actual == expected

    # normal system for Python
    def test_get_functions_in_python_file_1_1(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        actual = get_functions_in_python_file(file_full_name)
        expected = ["make_voicedsound", "main"]
        assert actual == expected

     # normal system for Python
    def test_get_functions_in_python_file_1_2(self):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        actual = get_functions_in_python_file(file_full_name, "def ", "(")
        expected = ["make_voicedsound", "main"]
        assert actual == expected

    # normal system for JavaScript (ECMAScript)
    def test_get_functions_in_python_file_2_1(self):
        # TODO
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_javascript.js", "test_data")
        actual = get_functions_in_python_file(file_full_name, "function ", "(")
        expected = ["getFolderIdArray"]
        assert actual == expected

    # normal system
    def test_get_words_in_lines_by_head_and_tail_1_1(self):
        lines = ["class ReplaceCharacter:", "    def make_voicedsound(self, text : str) -> str:", "        pass", "def main():", "    replace_character = ReplaceCharacter()", "if __name__ == \"__main__\":", "    main()"]
        head = "def "
        tail = "("
        actual = get_words_in_lines_by_head_and_tail(lines, head, tail)
        expected = ["make_voicedsound", "main"]
        assert actual == expected

    def test_printfunc_1_1(self, mocker):
        file_full_name = get_src_path_from_test_path(__file__, "for_test_get_func_python.py", "test_data")
        mocker.patch("sys.argv", return_value=["printfunc", file_full_name, ""])
        mocker.patch.object(sys, "argv", ["printfunc", file_full_name, ""])
        actual = printfunc()
        expected = ["make_voicedsound", "main"]
        assert actual == expected
