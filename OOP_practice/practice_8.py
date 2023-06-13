import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def alphabet_print(self):
        return self.letters

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def_letters = string.ascii_uppercase

    def __init__(self, lang='En', letters=def_letters):
        super().__init__(lang, letters)

    @staticmethod
    def __letters_num():
        return len(EngAlphabet.def_letters)

    def is_en_letter(self, letter):
        return True if letter in self.letters else False

    def letters_num(self):
        return EngAlphabet.__letters_num()


if __name__ == '__main__':
    en_al = EngAlphabet()
    print(en_al.letters)
    print(en_al.letters_num())
    print(en_al.is_en_letter('F'))
    print(en_al.is_en_letter('Щ'))
