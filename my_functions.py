"""
-----Функция проверки вводимого числа в функции input()-----
Функция переведет любую строку в int, float формат.
При переводе отбрасывает все символы с учетом:
    1. Минус будет один в начале строки и не встретится между цифр
    2. Первая "." будет указывать начало float, остальные будут отброшены
"""


def input_number(number: str):  # для проверки переменной <переменная> = input_number(input())
    str_ = ""
    minus_count = 0
    number.strip()  # Для возможного сокращения перебора
    for i in number:
        if not str_ and i == "-":
            minus_count += 1
        elif str_ and i == "-":
            return "Минус не может быть после числа!"
        elif i == "." not in str_:
            str_ = str_ + i
        elif i == "." in str_:
            pass
        elif i.isdigit():
            str_ = str_ + i
    # Возможный print(number) Для провеки введеного числа
    if not str_:
        return "В строке не было чисел"
    if minus_count == 1 and "." in str_:
        str_ = "-" + str_
        return float(str_)
    elif minus_count == 1:
        str_ = "-" + str_
        return int(str_)
    elif minus_count == 0 and "." not in str_:
        return int(str_)
    elif minus_count == 0 and "." in str_:
        return float(str_)
    else:
        return "Для задания отрицательного числа введите лишь 1 минус в начале числа!"


if __name__ == "__main__":
    a = input_number(input("Введите ваше число: "))

    print(a)
    print(type(a))
