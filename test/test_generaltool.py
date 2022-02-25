from src.landmasterlibrary.generaltool import ReplaceCharacter

class Test_ReplaceCharacter:
    # normal system
    def test_get_src_path_from_test_path_1_1(self):
        # TODO: configFileNameをテスト用のファイルに直す。
        actual_path = get_src_path_from_test_path(__file__, configFileName)
        actual = actual_path.count("/")
        expected = 2
        assert actual == expected

    # normal system
    def test_get_src_path_from_test_path_1_2(self):
        # TODO: configFileNameをテスト用のファイルに直す。
        actual_path = get_src_path_from_test_path(__file__, configFileName, "src")
        actual = actual_path.count("/")
        expected = 2
        assert actual == expected

    # abnormal system
    def test_get_src_path_from_test_path_2_1(self):
        # TODO: pytest形式に直す
        with self.assertRaises(TypeError):
            actual = get_src_path_from_test_path()
            expected = 2

    # abnormal system
    def test_get_src_path_from_test_path_2_2(self):
        # TODO: pytest形式に直す
        with self.assertRaises(TypeError):
            actual = get_src_path_from_test_path(__file__)
            expected = 2
