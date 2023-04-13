# -----------------
try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Перед исключением")
    # теперь пользователь сам вводит числа для деления
    a = 4
    b = 0
    c = a / b  # здесь может возникнуть исключение деления на ноль
    print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as error:
#     print(error)
except ZeroDivisionError:  # Добавляем тип именно той ошибки которую хотим отловить.
    print("!!!Деление на ноль!!!")  # Выводим информацию об ошибке
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения)
    print("Всё ништяк")
finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Finally на месте")

print("После После исключения")
# -----------------


class MyException(Exception):  # создаём пустой класс – исключения
    pass


try:
    raise MyException  # поднимаем наше исключение
except MyException as e:  # ловим его за хвост как шкодливого котёнка
    print("ffff")  # выводим информацию об исключении

# Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.


class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException("Число меньше или равно 0")


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


def to_list(*arg):
    return list(arg)


def useless(s):
    return max(s) / len(s)


def sort_list(list2):
    list2.sort(key=lambda x: abs(x), reverse=True)
    return list2


def all_eq(lst):
    new_lst = []
    for i in lst:
        while len(i) != len(max(lst)):
            i += '_'
        new_lst.append(i)
    return new_lst


if __name__ == '__main__':
    storona = Square(3)
    lst1 = [1, 3, "f", 4, -1, 0.3, "fgrg"]
    print(lst1[::-1])
    print(change(lst1))
    print(to_list(3, 4, 1, 2))
    print(useless([3, 4, 1, 2, 6]))
    print(sort_list([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))
    list_of_strings = ['stroka', 'hype', 'traktorist']
    print(all_eq(list_of_strings))


