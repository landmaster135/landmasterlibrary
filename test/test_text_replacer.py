from src.landmasterlibrary.text_replacer import ReplaceCharacter

class Test_ReplaceCharacter:
    # Unicode : \u3099: normal system
    def test_make_voicedsound_1_1(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("がぎぐげござじずぜぞ") == "がぎぐげござじずぜぞ"

    def test_make_voicedsound_1_2(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("だぢづでどばびぶべぼ") == "だぢづでどばびぶべぼ"

    # Unicode : \u309A: normal system
    def test_make_voicedsound_1_3(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("ぱぴぷぺぽ") == "ぱぴぷぺぽ"

    # Unicode : \u3099: normal system
    def test_make_voicedsound_1_4(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("ガギグゲゴザジズゼゾ") == "ガギグゲゴザジズゼゾ"

    def test_make_voicedsound_1_5(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("ダヂヅデドバビブベボ") == "ダヂヅデドバビブベボ"

    # Unicode : \u309A: normal system
    def test_make_voicedsound_1_6(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("パピプペポ") == "パピプペポ"

    # dakuon: normal system
    def test_make_voicedsound_2_1(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("がぎぐげござじずぜぞ") == "がぎぐげござじずぜぞ"

    def test_make_voicedsound_2_2(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("だぢづでどばびぶべぼ") == "だぢづでどばびぶべぼ"

    #handakuon: normal system
    def test_make_voicedsound_2_3(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("ぱぴぷぺぽ") == "ぱぴぷぺぽ"

    # dakuon: normal system
    def test_make_voicedsound_2_4(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("ガギグゲゴザジズゼゾ") == "ガギグゲゴザジズゼゾ"

    def test_make_voicedsound_2_5(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("ダヂヅデドバビブベボ") == "ダヂヅデドバビブベボ"

    # handakuon: normal system
    def test_make_voicedsound_2_6(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound("パピプペポ") == "パピプペポ"

    # dakuon: semi-normal system
    def test_make_voicedsound_3_1(self):
        replaceCharacter = ReplaceCharacter()
        expectedCharacters = "かきくけこさしすせそ"
        actualCharacters = replaceCharacter.make_voicedsound("がぎぐげござじずぜぞ")
        for i in range(0, len(expectedCharacters), 1):
            assert expectedCharacters[i] != actualCharacters[i]

    def test_make_voicedsound_3_2(self):
        replaceCharacter = ReplaceCharacter()
        actualCharacters = replaceCharacter.make_voicedsound("だぢづでどばびぶべぼ")
        expectedCharacters = "たちつてとはひふへほ"
        for i in range(0, len(expectedCharacters), 1):
            assert expectedCharacters[i] != actualCharacters[i]

    #handakuon: semi-normal system
    def test_make_voicedsound_3_3(self):
        replaceCharacter = ReplaceCharacter()
        actualCharacters = replaceCharacter.make_voicedsound("ぱぴぷぺぽ")
        expectedCharacters = "はひふへほ"
        for i in range(0, len(expectedCharacters), 1):
            assert expectedCharacters[i] != actualCharacters[i]

    # dakuon: semi-normal system
    def test_make_voicedsound_3_4(self):
        replaceCharacter = ReplaceCharacter()
        actualCharacters = replaceCharacter.make_voicedsound("ガギグゲゴザジズゼゾ")
        expectedCharacters = "カキクケコサシスセソ"
        for i in range(0, len(expectedCharacters), 1):
            assert expectedCharacters[i] != actualCharacters[i]

    def test_make_voicedsound_3_5(self):
        replaceCharacter = ReplaceCharacter()
        actualCharacters = replaceCharacter.make_voicedsound("ダヂヅデドバビブベボ")
        expectedCharacters = "タチツテトハヒフヘホ"
        for i in range(0, len(expectedCharacters), 1):
            assert expectedCharacters[i] != actualCharacters[i]

    # handakuon: semi-normal system
    def test_make_voicedsound_3_6(self):
        replaceCharacter = ReplaceCharacter()
        actualCharacters = replaceCharacter.make_voicedsound("パピプペポ")
        expectedCharacters = "ハヒフヘホ"
        for i in range(0, len(expectedCharacters), 1):
            assert expectedCharacters[i] != actualCharacters[i]
