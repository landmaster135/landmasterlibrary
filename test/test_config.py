# Library by third party
import pytest
# Library by landmasterlibrary
import src.landmasterlibrary.config as config

class Test_Config:

    # normal system
    def test_spaces_1_1(self):
        now_config = config.Config()
        actual = now_config.spaces
        expected = [" ", "　"]
        for i in range(0, len(expected)):
            assert actual[i] == expected[i]

    # normal system
    def test_seperators_1_1(self):
        now_config = config.Config()
        actual = now_config.seperators
        expected = [",", "、"]
        for i in range(0, len(expected)):
            assert actual[i] == expected[i]
