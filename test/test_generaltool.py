# Library by default
from pathlib import Path
# Library by third party
import pytest
# Library by landmasterlibrary
from src.landmasterlibrary.generaltool import get_value_from_yaml, get_src_path_from_test_path, remove_spaces_at_head_and_tail, remove_tail_sapces, remove_head_sapces

class Test_ReplaceCharacter:

    # normal system
    def test_get_src_path_from_test_path_1_1(self):
        # TODO: configFileNameをテスト用のファイルに直す。
        actual_path = get_src_path_from_test_path(__file__, configFileName)
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # normal system
    def test_get_src_path_from_test_path_1_2(self):
        # TODO: configFileNameをテスト用のファイルに直す。
        actual_path = get_src_path_from_test_path(__file__, configFileName, "src")
        actual = actual_path.count("/")
        expected = 2
        assert actual >= expected

    # abnormal system
    def test_get_src_path_from_test_path_2_1(self):
        # TODO: pytest形式に直す
        # with self.assertRaises(TypeError):
        #     actual = get_src_path_from_test_path()
        #     expected = 2
        with pytest.raises(Exception) as e:
            actual = get_src_path_from_test_path()
            expected = 2
        assert str(e.value) == ""

    # abnormal system
    def test_get_src_path_from_test_path_2_2(self):
        # TODO: pytest形式に直す
        # with self.assertRaises(TypeError):
        #     actual = get_src_path_from_test_path(__file__)
        #     expected = 2
        with pytest.raises(Exception) as e:
            actual = get_src_path_from_test_path(__file__)
            expected = 2
        assert str(e.value) == ""

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
    def test_remove_tail_sapces_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        spaces = [" ", "　"]
        actual = remove_tail_sapces(keyword, spaces)
        expected = "   　　　　　　　      　　   node.js"
        assert actual == expected

    # normal system
    def test_remove_head_sapces_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        spaces = [" ", "　"]
        actual = remove_head_sapces(keyword, spaces)
        expected =                             "node.js    　　　　　  　　　　  "
        assert actual == expected

    # normal system
    def test_remove_spaces_at_head_and_tail_1_1(self):
        keyword  = "   　　　　　　　      　　   node.js    　　　　　  　　　　  "
        spaces = [" ", "　"]
        actual = remove_spaces_at_head_and_tail(keyword, spaces)
        expected = "node.js"
        assert actual == expected
