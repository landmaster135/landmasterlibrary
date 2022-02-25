from src.landmasterlibrary.text_replacer import ReplaceCharacter

class Test_ReplaceCharacter:
    # Unicode : \u3099
    def test_make_voicedsound_1_1(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('がぎぐげござじずぜぞ') == 'がぎぐげござじずぜぞ'

    def test_make_voicedsound_1_2(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('だぢづでどばびぶべぼ') == 'だぢづてどばびぶべぼ'

    # Unicode : \u309A
    def test_make_voicedsound_1_3(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('ぱぴぷぺぽ') == 'ぱぴぷぺぽ'

    # Unicode : \u3099
    def test_make_voicedsound_1_4(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('ガギグゲゴザジズゼゾ') == 'ガギグゲゴザジズゼゾ'

    def test_make_voicedsound_1_5(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('ダヂヅデドバビブベボ') == 'ダヂヅデドバビブベボ'

    # Unicode : \u309A
    def test_make_voicedsound_1_6(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('パピプペポ') == 'パピプペポ'

    # dakuon
    def test_make_voicedsound_2_1(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('がぎぐげござじずぜぞ') == 'がぎぐげござじずぜぞ'

    def test_make_voicedsound_2_2(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('だぢづてどばびぶべぼ') == 'だぢづてどばびぶべぼ'

    #handakuon
    def test_make_voicedsound_2_3(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('ぱぴぷぺぽ') == 'ぱぴぷぺぽ'

    # dakuon
    def test_make_voicedsound_2_4(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('ガギグゲゴザジズゼゾ') == 'ガギグゲゴザジズゼゾ'

    def test_make_voicedsound_2_5(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('ダヂヅデドバビブベボ') == 'ダヂヅデドバビブベボ'

    # handakuon
    def test_make_voicedsound_2_6(self):
        replaceCharacter = ReplaceCharacter()
        assert replaceCharacter.make_voicedsound('パピプペポ') == 'パピプペポ'
