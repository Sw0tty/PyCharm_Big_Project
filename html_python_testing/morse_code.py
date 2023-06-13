morse_dict = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И',
              '.---': 'Й', '-.-': 'К', '.--..': 'Л', '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П', '.-.': 'Р',
              '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
              '--.-': 'Щ', '.--.-.': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '..--..': 'Э', '..--': 'Ю', '.-.-': 'Я'}


class Morse:
    @staticmethod
    def word_in_morse(word):
        word_morse = ''
        count = 0
        if '.' in word or '-' in word:
            translate_word = word.split()
            for i in translate_word:
                word_morse += f"{morse_dict[i]}"
            return word_morse
        else:
            while count < len(word):
                for i, j in morse_dict.items():
                    if j == word[count].upper():
                        word_morse += f"{i} "
                    elif not word[count].upper():
                        pass
                count += 1
            return word_morse


if __name__ == '__main__':
    word = Morse
    print(word.word_in_morse(input('Что перевести на азбуку морзе? ')))
