"""
Модуль перевода строк в числа
"""


class NumberStr:
    @staticmethod
    def transform_string_to_integer(s):
        s = s.lower().split()
        basic_dict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
                      'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'двенадцать': 12, 'сорок': 40,
                      'девяносто': 90, 'сто': 100, 'двести': 200, 'тысяча': 1000, 'миллион': 1000000}
        num_from_str = []
        for num in s:
            if num in basic_dict and len(s) == 1:
                return basic_dict[num]
            elif num in basic_dict:
                num_from_str.append(basic_dict[num])
            else:
                for i in basic_dict.keys():
                    if i in num or i[:-1] in num:
                        if i + 'адцать' == num:
                            num_from_str.append(int('1' + str(basic_dict[i])))
                        elif i + 'надцать' == num or i[:-1] + 'надцать' == num:
                            num_from_str.append(int('1' + str(basic_dict[i])))
                        elif i + 'дцать' == num:
                            num_from_str.append(int(str(basic_dict[i]) + '0'))
                        elif i + 'десят' == num:
                            num_from_str.append(int(str(basic_dict[i]) + '0'))
                        elif i + 'ста' == num or i + 'сот' == num or i[:-1] + 'сти' == num:
                            num_from_str.append(int(str(basic_dict[i]) + '00'))
                        elif i.lower().startswith('тысяч'):
                            num_from_str.append(int(str(basic_dict['тысяча'])))

        if not num_from_str:
            return "Неизвестное число"
        elif len(num_from_str) <= 3:
            return sum(num_from_str)
        elif 1000 in num_from_str:
            return sum(i * 1000 for i in num_from_str[:num_from_str.index(1000)]) + \
                sum(i for i in num_from_str[num_from_str.index(1000) + 1:])
