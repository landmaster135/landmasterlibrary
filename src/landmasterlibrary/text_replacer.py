class ReplaceCharacter:
    def make_voicedsound(self, text : str) -> str:
        """
        text           : String of target text.
        """
        target  = 'がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ'
        replace = 'がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ'
        list_target  = []
        list_replace = []
        for i in range(0, len(target), 2):
            list_target.append(target[i : i+2])
        for i in range(0, len(replace), 1):
            list_replace.append(replace[i : i+1])

        for i in range(0,len(list_target)):
            text = text.replace(list_target[i], list_replace[i])

        print("ReplaceCharacter.make_voicedsound: return {}".format(text))

        return text

def main():
    replace_character = ReplaceCharacter()
    replace_character.make_voicedsound("でずど")

if __name__ == "__main__":
    main()
