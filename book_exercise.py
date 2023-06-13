"""
-+--Ben_Stivenson_Sbornik_uprazhneniy_Python--+-
"""
import math
import random
import string
import time
from decimal import Decimal
from my_functions import input_number


"""
--Упражнение 1 Почтовый адрес--
"""
# name = "Кирилл"
# post_address = "1470"
# print(f"Приверт {name}. Ваш почтовый адрес {post_address}")


"""
--Упражнение 2 Приветствие--
"""
# name = input("Как вас зовут? ")
# print(f"{name}, приятно познакомиться!")


"""
--Упражнение 3 Площадь комнаты--
"""
# HEIGHT = float(input("Введите длину комнаты "))
# WIDTH = float(input("Введите ширину комнаты "))
#
# print(f"Площадь вашей комнаты {HEIGHT * WIDTH} квадратных метров")


"""
--Упражнение 4 Площадь садового участка--
"""
# akr = 43560
# HEIGHT = float(input("Введите длину участка "))
# WIDTH = float(input("Введите ширину участка "))
#
# print(f"Площадь вашего участка {akr / (HEIGHT * WIDTH)} акров")


"""
--Упражнение 5 Сдаем бутылки--
"""
# tara1 = ""
# tara2 = ""
# while not tara1.isdigit():
#     tara1 = input("Сколько у вас бутылок 1 и меньше литров? ")
# while not tara2.isdigit():
#     tara2 = input("Сколько у вас бутылок больше 1 литра? ")
#
# tara1, tara2 = int(tara1), int(tara2)
# print(f"Продав все бутылки, вы сможите выручить ${round(tara1 * 0.1 + tara2 * 0.25, 2)}")


"""
--Упражнение 6 Налоги и чаевые--
"""
# number = ""
#
# while not number.isdigit():
#     number = input("Введите целое, положительное число ")
# sum_ = 0
# number = int(number)
#
# for i in range(1, number + 1):
#     sum_ = sum_ + i
#
# print(f"Сумма чисел последовательности равна {sum_}")


"""
--Упражнение 7 Сумма первых n положительных чисел--
"""
# a = ""
# while True:
#     a = input()
#     sum_ = 0
#     sum_2 = 0
#     if a.isdigit():
#         for i in range(1, int(a) + 1):
#             sum_ += i
#         print(sum_)
#         break
#     else:
#         continue


"""
--Упражнение 8 Сувениры и безделушки--
"""
# toys_1 = ""
# toys_2 = ""
# while not toys_1.isdigit():
#     toys_1 = input("Сколько сувениров? ")
# while not toys_2.isdigit():
#     toys_2 = input("Сколько безделушек? ")
#
# toys_1, toys_2 = int(toys_1), int(toys_2)
# print(f"Общий вес всех безделушек {(toys_2 * 75 + toys_2 * 112)//1000} кг,"
#       f" {(toys_2 * 75 + toys_2 * 112)%1000} грамм")


"""
--Упражнение 9 Сложные проценты--
"""
# money = ""
# while not money.isdigit():
#     money = input("Сколько денег положить в банк? ")
#
# money = int(money)
# print("--Сберегательный счет под 4% годовых успешно открыт--")
# for i in range(1, 4):
#     print(f"После года вложения на вашем счете будет: {round(money + ((4 * money) / 100) * i, 2)}")


"""
--Упражнение 10 Арифметика--
"""
# a = input_number(input("Введите первое число: "))
# b = input_number(input("Введите второе число: "))
#
# print(f"Сумма A и B: {a + b}")
# print(f"Разница между A и B: {round(a - b, 3)}")
# print(f"Произведение A и B: {a * b}")
# print(f"Частное от деления A и B: {a / b}")
# print(f"Остаток от деления A и B: {a % b}")
# print(f"Десятичный логарифм числа A: {math.log(a)}")
# print(f"Результат возведения числа A и B: {a ** b}")

"""
--Упражнение 12 Расстояние между точками на Земле--
"""
# EARTH_AVR = 6371.01
#
# def distance_of_dots(t1, t2, g1, g2):
#     distance = round(EARTH_AVR*math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1 - g2)), 6)
#     return f"Дистанция между точками: {distance}"
#
#
# while True:
#     try:
#         t1, t2 = map(int, (input("Введите координаты первой точки через пробел ")).split())
#         g1, g2 = map(int, (input("Введите координаты второй точки через пробел ")).split())
#         print(distance_of_dots(t1, t2, g1, g2))
#         break
#     except ValueError:
#         print("Неверное значение!")


"""
--Упражнение 13 Размен--
"""

# class BelowZero(Exception):
#     pass
#
#
# class IsZero(Exception):
#     pass
#
#
# def give_change(cash: int):
#     change_money = [200, 100, 25, 10, 5]
#     change = {'2D': 0, '1D': 0, '25C': 0, '10C': 0, '5C': 0, '1C': 0}
#     for i, j in enumerate(change.keys()):
#         if not cash:
#             break
#         if j == '1C':
#             change[j] = cash
#             break
#         count = cash // change_money[i]
#         change[j] = count
#         cash -= count * change_money[i]
#     return "Количество двухдолларовых купюр: {}\n" \
#            "Количество однодолларовых купюр: {}\n" \
#            "Количество монет в 25 центов: {}\n" \
#            "Количество монет в 10 центов: {}\n" \
#            "Количество монет в 5 центов: {}\n" \
#            "Количество монет в 1 цент: {}".format(*change.values())
#
#
# while True:
#     try:
#         cash = int(input("Сколько центов на сдачу? "))
#         if cash < 0:
#             raise BelowZero
#         print(give_change(cash))
#         break
#     except ValueError:
#         print("Принимаются только целые числа!")
#     except BelowZero:
#         print("Значение меньше нуля!")
#     except IsZero:
#         print("Без сдачи")


"""
--Упражнение 14 Рост--
"""
# height = 0
# while True:
#     a = input("Сколько в вашем росте футов: ")
#     if a.isdigit():
#         while True:
#             b = input("А дюймов: ")
#             if b.isdigit():
#                 height = ((int(a) * 12) + int(b)) * 2.54
#                 print(f"Ваш рост составляет: {int(height // 100)}м и {round(height % 100, 3)}мм")
#                 break
#         break

"""
--Упражнение 15 Расстояние--
"""
# while True:
#     a = input("Сколько футов до цели: ")
#     if a.isdigit():
#         distance = [(int(a) * 12, "дюймов"), (round(int(a) / 3, 4), "ярдов"), (round(int(a) / 5280, 4), "миль")]
#         for i, j in distance:
#             print(f"До цели: {i}{j}")
#         break

"""
--Упражнение 16 Площадь и объем--
"""
# Обычное решение
# def radius(r):
#     return f"Площадь круга: {round(math.pi * pow(r, 2), 4)}. Объем шара: {round(4/3 * math.pi * pow(r, 3), 4)}."
#
#
# while True:
#     r = input()
#     if r.isdigit():
#         print(radius(int(r)))
#         break
#     elif "." in r:
#         print(radius(float(r)))
#         break

# Решение через класс
# class Radius:
#     def __init__(self, r):
#         self.r = r
#
#     def get_radius(self):
#         return f"Площадь круга: {round(math.pi * pow(self.r, 2), 4)}"
#
#     def get_volume(self):
#         return f"Объем шара: {round(4/3 * math.pi * pow(self.r, 3), 4)}"
#
#
# radius = Radius(5.4)
# print(radius.get_radius())
# print(radius.get_volume())

"""
--Упражнение 18 Объем цилиндра--
"""
# class Cylinder:
#     def __init__(self, r, height):
#         self.r = r
#         self.height = height
#
#     def __enter__(self):
#         return self.r, self.height
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"Площадь вашего целиндра: {round(result, 1)}")
#
#
# with Cylinder(int(input()), int(input())) as (r, height):
#     result = math.pi * pow(r, 2) * height


"""
--Упражнение 24 Единицы времени--
"""
# question_dict = {"1": "дней", "2": "часов", "3": "минут", "4": "секунд"}
# i = 1
# n = []
# while True:
#     a = input(f"Введите количество {question_dict[str(i)]} или N, для пропуска: ")
#     if a.isdigit():
#         n.append(int(a))
#     elif a.upper().strip() == "N":
#         n.append(0)
#     else:
#         continue
#     if i != 4:
#         i += 1
#         continue
#     break
#
# result = ((n[0] * 24) * 60) * 60 + (n[1] * 60) * 60 + n[2] * 60 + n[3]
# print(f"В заданном временном отрезке {result} секунд")


"""
--Упражнение 25 Единицы времени (снова)--
"""
# while True:
#     seconds = input("Введите количество секунд: ")
#     if seconds.isdigit():
#         seconds = int(seconds)
#         while True:
#             days = seconds // (24 * 60 * 60)
#             if days > 0:
#                 seconds = seconds - (24 * 60 * 60) * days
#             hours = seconds // (60 * 60)
#             if hours > 0:
#                 seconds = seconds - ((60 * 60) * hours)
#             minutes = seconds // 60
#             if minutes > 0:
#                 seconds = seconds - 60 * minutes
#             break
#         print("%d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
#         break


"""
--Упражнение 26 Текущее время--
"""
# print(time.asctime())


"""
--Упражнение 30 Цельсий в Фаренгейт и Кельвин--
"""
# class Temperature:
#     def __init__(self, celsia):
#         self.celsia = celsia
#
#     def conversion(self):
#         return f"Ваши цельсия в Фаренгейт: {(self.celsia * 9 / 5) + 32}. И Кельвин: {self.celsia + 273.15}"
#
#
# while True:
#     try:
#         temperature = Temperature(float(input("Введите температуру в цельсия: ").strip()))
#         print(temperature.conversion())
#         break
#     except ValueError:
#         print("Try again!")


"""
--Упражнение 31 Единицы давления--
В данном задании вам предстоит написать программу, которая будет пе-
реводить введенное пользователем значение давления в  килопаскалях
(кПа) в фунты на квадратный дюйм (PSI), миллиметры ртутного столба
и  атмосферы. Коэффициенты и  формулы для перевода найдите само-
стоятельно.
"""

"""
--Упражнение 32 Сумма цифр в числе--
"""
# while True:
#     number = input("Введите 4-значное, целое число: ")
#     if number.isdigit() and len(number) == 4:
#         print(sum(map(int, list(number))))
#         break


"""
--Упражнение 33 Сортировка трех чисел--
"""
# while True:
#     number1 = input("Введите первое, целое число: ")
#     number2 = input("Введите второе, целое число: ")
#     number3 = input("Введите третье, целое число: ")
#     if number1.isdigit() and number2.isdigit() and number3.isdigit():
#         list_of_numbers = list(map(int, (number1, number2, number3)))
#         print(min(list_of_numbers), abs(max(list_of_numbers) + min(list_of_numbers) - sum(list_of_numbers)),
#               max(list_of_numbers))
#         break
#     print("Не все введенные значения, являются целыми числами!")
#
#
# class Numbers:
#     def __init__(self, first, second, third):
#         self.first = first
#         self.second = second
#         self.third = third
#
#     def sorted(self):
#         list_of_numbers = list(map(int, (self.first, self.second, self.third)))
#         return f"{min(list_of_numbers)} {abs(max(list_of_numbers) + min(list_of_numbers) - sum(list_of_numbers))} " \
#                f"{max(list_of_numbers)}"
#
#
# sorted_numbers = Numbers(number1, number2, number3)
#
# print(sorted_numbers.sorted())

"""
--Упражнение 34 Вчерашний хлеб--
"""
# class Bakery:
#     def __init__(self, quantity):
#         self.quantity = quantity
#         self.bread_price = 3.49
#
#     def price(self):
#         return f"Буханка хлеба стоит ${self.bread_price}\nСкидка на вчерашний хлеб составляет 60%"
#
#     def buy(self):
#         with_discount = self.bread_price - (self.bread_price * 60 / 100)
#         return f"Стоимость с учетом скидки, за одну буханку будет составлять: ${round(with_discount, 2)}.\n" \
#                f"Итого с вас: ${round((self.bread_price - with_discount) * self.quantity, 2)}"
#
#
# while True:
#     try:
#         customer = Bakery(int(input("Сколько будете брать? ").strip()))
#         print(customer.price())
#         print(customer.buy())
#         break
#     except ValueError:
#         print("Хлеб продаем целыми буханками.")
#         time.sleep(1)


"""
--Упражнение 35 Чет или нечет?--
"""
# a = ""
# while type(a) != int:
#     a = input_number(input("Введите целое число: "))
#
# if a % 2 == 0:
#     print("Число четное")
# else:
#     print("Число не четное")


"""
--Упражнение 36 Собачий возраст--
"""
# a = ""
# result = 0
# while type(a) != int:
#     a = input_number(input("Введите НЕ отрицательное целое число "))
#     if "-" in str(a):
#         a = ""
#         print("Сказал же, НЕ отрицательное!")
#     elif a == 0:
#         a = ""
#         print("Вашей собаке должно быть хотя бы год для перевода")
#
# if a <= 2:
#     result = a * 10.5
# elif a > 2:
#     result = (a - 2) * 4 + 2 * 10.5
# print(result)


"""
--Упражнение 37 Гласные и согласные--
"""
# letter = (input("Введите английскую букву ")).strip()
# glasn_letters = "aeiouAEIOUYy"
# alphabet = "".join(sorted(set(glasn_letters).symmetric_difference(set(string.ascii_letters))))
# if letter in alphabet:
#     print("Ввведена согласная буква")
# elif letter == "y" or letter == "Y":
#     print("Буква может быть и согласной, и гласной")
# else:
#     print("Буква гласная")


"""
--Упражнение 38 Угадайте фигуру--
"""
# class ThisFigure:
#     def __init__(self, quantity_sides):
#         self.quantity_sides = quantity_sides
#
#     def i_think(self):
#         figure_dict = {"3": "треугольник", "4": "прямоугольник", "5": "пятиугольник", "6": "шестиугольник",
#                        "7": "шестиугольник", "8": "шестиугольник", "9": "девятиугольник", "10": "десятиугольник"}
#         self.quantity_sides = str(self.quantity_sides)
#         return f"Я думаю, что ваша фигуру: {figure_dict[self.quantity_sides]}"
#
#
# while True:
#     try:
#         figure = ThisFigure(int(input("Сколько сторон в вашей фигуре? ").strip()))
#         if figure.quantity_sides not in range(3, 11):
#             raise ValueError
#     except ValueError:
#         print("Принимаем лишь целые значения от 3 до 10")
#         time.sleep(1)
#     else:
#         print(figure.i_think())
#         break


"""
--Упражнение 39 Сколько дней в месяце?--
"""
# class DaysMonth:
#     def __init__(self, month):
#         self.month = month
#         self.month_dict = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
#                            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
#
#     def in_month(self):
#         user_month.month = user_month.month.lower().title()
#         if user_month.month_dict.index(user_month.month) % 2 == 0:
#             return f"В месяце {user_month.month} 31 день"
#         elif user_month.month_dict.index(user_month.month) % 2 != 0 and user_month.month == "Февраль":
#             return f"В месяце {user_month.month} 28(29) дней, в зависимости от года"
#         else:
#             return f"В месяце {user_month.month} 30 дней"
#
#
# while True:
#     try:
#         user_month = DaysMonth(input("Введите месяц: ").strip())
#         if not user_month.month.isalpha():
#             raise ValueError
#         elif user_month.month.lower().title() not in user_month.month_dict:
#             print("Такого месяца не существует")
#             continue
#     except ValueError:
#         print("Месяца состоят только из букв")
#     else:
#         print(user_month.in_month())
#         break

"""
--Упражнение 40 Громкость звука--
"""

# class BelowZero(Exception):
#     pass
#
#
# sounds_dict = {130: 'Отбойный молоток', 106: 'Газовая газонокосилка', 70: 'Будильник', 40: 'Тихая комната'}
#
# def sound_like(sound: int, sounds: dict):
#     if sound in sounds.keys():
#         return f"Такая громкость у: {sounds[sound]}"
#     elif sound > 130:
#         return f"Такая громкость больше, чем у: {sounds[130]}"
#     elif sound < 40:
#         return f"Такая громкость тише, чем у: {sounds[40]}"
#     for i, j in enumerate(sounds.keys()):
#         check = j
#         if j > sound < list(sounds)[i + 1]:
#             continue
#         return f"Такая громкость тише, чем у: {sounds[check]}, " \
#                f"но громче, чем у: {sounds[list(sounds)[i + 1]]}"
#
#
# while True:
#     try:
#         sound = int(input("Введите громкость звука: "))
#         if sound < 0:
#             raise BelowZero
#         sound_like(sound, sounds_dict)
#     except ValueError:
#         print("Недопустимое значение!")
#     except BelowZero:
#         print("Значение ниже нуля!")
#     else:
#         sound_like(sound, sounds_dict)
#         break


"""
--Упражнение 41 Классификация треугольников--
"""
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def this_triangle(self):
#         if self.a == self.b and self.a == self.c and self.c == self.b:
#             return "Данный треугольник равносторонний"
#         elif self.a == self.c or self.a == self.b or self.b == self.c:
#             return "Данный треуголник равнобедренный"
#         else:
#             return "Данный треугольник разносторонний"
#
#
# while True:
#     try:
#         a = float(input("Введите первую сторону треугольника: "))
#         b = float(input("Введите вторую сторону треугольника: "))
#         c = float(input("Введите третью сторону треугольника: "))
#         triangle = Triangle(a, b, c)
#     except ValueError:
#         print("Введено неверное значение, начинаем с начала")
#     else:
#         print(triangle.this_triangle())
#         break

"""
Упражнение 44 Портреты на банкнотах
"""

"""
Упражнение 46 Какого цвета клетка?
"""

"""
--Упражнение 63 Среднее значение--
"""

# def list_avg():
#     numbers_list = []
#     while (number := input("Введите число: ")) != '0':
#         try:
#             numbers_list.append(float(number))
#         except ValueError:
#             print("Только числа")
#     return sum(numbers_list) / len(numbers_list)
#
# print(list_avg())

"""
--Упражнение 64 Таблица со скидками--
"""

# initial_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
# changes = [(i, i * 60 / 100, i - i * 60 / 100) for i in initial_prices]
# print("Начальная цена|Скидка|Цена по скидке")
# for i in changes:
#     print("{:14.2f}|{:6.2f}|{:14.2f}".format(*i))

"""
--Упражнение 65 Таблица соотношения температур--
"""

# CONSTANT = float(Decimal('9') / Decimal('5'))
# print("|Цельсия | Фаренгейт|")
# degrees = [(i, (i*CONSTANT) + 32) for i in range(0, 101, 10)]
# for i in degrees:
#     print("|{:<8}|{:>10}|".format(*i))

"""
--Упражнение 69 Билеты в зоопарк--
"""

# class BelowZero(Exception):
#     pass
#
#
# class NotBirth(Exception):
#     pass
#
#
# def ticket_price() -> str:
#     visitors = []
#     while age := input("Сколько вам лет? "):
#         try:
#             age = int(age)
#             if age == 0:
#                 raise NotBirth
#             elif age < 0:
#                 raise BelowZero
#             if 3 <= age <= 12:
#                 visitors.append(14)
#             elif age > 65:
#                 visitors.append(18)
#             elif 12 < age <= 65:
#                 visitors.append(23)
#         except ValueError:
#             print()
#         except NotBirth:
#             print("Вы еще не родились")
#         except BelowZero:
#             print("Вам не может быть меньше нуля")
#     return f"Общая сумма всех билетов: ${sum(visitors)}"
#
#
# print(ticket_price())


"""
Упражнение 86 Плата за такси
"""
# PRICE = 4.00
# DRIVE_FOR_M = 0.25
#
#
# def total_taxi_price(distance):
#     return f"С вас ${PRICE + ((distance / 140) * DRIVE_FOR_M)}"
#
#
# print(total_taxi_price(140))


"""
Упражнение 87 Расчет стоимости доставки
"""

# FOR_FIRST = 10.95
# ANOTHER = 2.95
#
#
# def delivery(value):
#     return f"Стоимость доставки ${round(FOR_FIRST + (ANOTHER * (value - 1)), 2)}"
#
#
# while True:
#     value = input("Сколько в вашем заказе предметов: ")
#     if value.isdigit() and value != '0':
#         value = int(value)
#         print(delivery(value))
#         break
#     print("Принимаются только целые числа большие 0")
#     continue

"""
Упражнение 88 Медиана трех значений
"""

# def mediana(n1, n2, n3):
#     return sorted([n1, n2, n3])[1]
#
#
# while True:
#     user_numbers = input("Введите три числа через пробел ")
#     try:
#         n1, n2, n3 = map(int, user_numbers.split())
#     except Exception:
#         continue
#     else:
#         print(mediana(n1, n2, n3))
#         break

"""
Упражнение 93 Центрируем строку
"""

# def center_str(s, spaces):
#     return f"|{s:^{spaces}s}|"
#
# print(center_str("Меж пробелами", 25))

"""
Упражнение 94 Треугольник ли?
"""

# def is_triangle(n1, n2, n3):
#     sort_num = sorted([n1, n2, n3])
#     return True if sort_num[0] + sort_num[1] > sort_num[2] else False
#
#
# while True:
#     user_numbers = input("Введите три числа через пробел ")
#     try:
#         n1, n2, n3 = map(int, user_numbers.split())
#     except Exception:
#         continue
#     else:
#         print(is_triangle(n1, n2, n3))
#         break

"""
Упражнение 95 Озаглавим буквы
"""

# def upper_first_letter(str_: str) -> str:
#     counter = -1
#     str_list = str_.split()
#     for i in str_list:
#         counter += 1
#         if counter == 0 or '!' in str_.split()[counter - 1] or '?' in str_.split()[counter - 1]\
#                 or '.' in str_.split()[counter - 1]:
#             str_list[counter] = i.capitalize()
#     return " ".join(str_list)
#
#
# print(upper_first_letter("""what time do i have to be there?
# what’s the address? this time i’ll try to be on time!"""))

"""
Упражнение 96 Является ли строка целым числом?
"""
# def is_integer(str_: str) -> bool:
#     try:
#         if float(str_.replace(" ", "")) == int(float(str_.replace(" ", ""))):
#             return True
#         else:
#             return False
#     except ValueError:
#         return False
#
#
# if __name__ == '__main__':
#     print(is_integer(' -3 .0 '))

"""
Упражнение 98 Простое число?
"""

# def is_simple(digit: int) -> bool:
#     counter = 2
#     for i in range(2, int(math.sqrt(digit))):
#         if digit % i == 0:
#             counter += 1
#         if counter > 2:
#             return False
#     return True
#
# if __name__ == '__main__':
#     print(is_simple(809))

"""
Упражнение 99 Следующее простое число
"""
# def next_simple(digit: int):
#     digit += 1
#     while not is_simple(digit):
#         print()
#         digit += 1
#     return digit
#
# if __name__ == '__main__':
#     print(next_simple(983))

"""
Упражнение 100 Случайный пароль
"""

# def random_password():
#     password = ''
#     for i in range(1, random.randint(8, 11)):
#         password += chr(random.randint(33, 126))
#     return password
#
#
# if __name__ == '__main__':
#     print(random_password())

"""
Упражнение 101 Случайный номерной знак
"""

# def random_plate_number():
#     plate_number = ''
#     for i in range(5):
#         if len(plate_number) >= 4:
#             plate_number += f"{str(random.randint(0, 999)):>03s}"
#         else:
#             plate_number += chr(random.randint(1040, 1071))
#     return plate_number
#
# print(random_plate_number())

"""
Упражнение 110 Порядок сортировки
"""

# numbers_list = []
# while True:
#     try:
#         number = int(input("Введите целое число (0 - закончить): "))
#         if number == 0:
#             break
#         numbers_list.append(number)
#     except ValueError:
#         print("Принимаются только целые числа!")
#
# print(*sorted(numbers_list), sep='\n')

"""
Упражнение 111 Обратный порядок
"""

# numbers_list = []
# while True:
#     try:
#         number = int(input("Введите целое число (0 - закончить): "))
#         if number == 0:
#             break
#         numbers_list.append(number)
#     except ValueError:
#         print("Принимаются только целые числа!")
#
# print(*sorted(numbers_list, reverse=True), sep='\n')

"""
Упражнение 112 Удаляем выбросы
"""

# class ShortList(Exception):
#     pass
#
#
# def cut_list(list_: list):
#     cutting_list = list_.copy()
#     cutting_list.remove(max(cutting_list))
#     cutting_list.remove(min(cutting_list))
#     return f"Original: {list_}\nCutting: {cutting_list}"
#
#
# numbers_list = []
# while True:
#     try:
#         number = int(input("Введите целое число (0 - закончить): "))
#         if number == 0:
#             break
#         numbers_list.append(number)
#     except ValueError:
#         print("Принимаются только целые числа!")
# if len(numbers_list) < 4:
#     raise ShortList("Список слишком короткий!")
# else:
#     print(cut_list(numbers_list))

"""
Упражнение 113 Избавляемся от дубликатов
"""
# list_of_strings = []
# def del_repeats(list_: list):
#     list_ = list_[::-1]
#     for i in list_:
#         while list_.count(i) > 1:
#             list_.remove(i)
#     return list_[::-1]
#
# while True:
#     user_str = input("Введите строку: ")
#     if not user_str:
#         break
#     list_of_strings.append(user_str)
#
# print(del_repeats(list_of_strings))

"""
Упражнение 114 Отрицательные, положительные и нули
"""

# numbers_list = []
# while True:
#     try:
#         number = input("Введите целое число (0 - закончить): ")
#         if not number:
#             break
#         numbers_list.append(int(number))
#     except ValueError:
#         print("Принимаются только целые числа!")
#
# print(*sorted(numbers_list), sep='\n')

"""
Упражнение 115 Список собственных делителей
"""
# def all_divisions(num):
#     divisions_list = [1]
#     for i in range(2, num):
#         if num % i == 0:
#             divisions_list.append(i)
#     return divisions_list
#
# while True:
#     try:
#         print(all_divisions(int(input("Делители какого числа узнать? "))))
#         break
#     except ValueError:
#         print("Принимается только целое число!")

"""
Упражнение 116 Совершенные числа
"""
# def all_perfect_numbers():
#     perfect_numbers = []
#     for i in range(1, 1001):
#         number = perfect_number(i)
#         if number:
#             perfect_numbers.append(i)
#     return perfect_numbers
#
# def perfect_number(num):
#     divisions_list = [1]
#     for i in range(2, num):
#         if num % i == 0:
#             divisions_list.append(i)
#     if sum(divisions_list) == num:
#         return True
#     return False
#
# print(all_perfect_numbers())
# while True:
#     try:
#         print(perfect_number(int(input("Какое число проверить на совершенство? "))))
#         break
#     except ValueError:
#         print("Принимается только целое число!")

"""
Упражнение 117 Только слова
"""

# def clear_words(str_):
#     for i in [',', '.', '!', '?', ';', ':', '-']:
#         str_ = str_.replace(i, '')
#     return str_.split()
#
# if __name__ == '__main__':
#     print(clear_words(input("Str ")))

"""
Упражнение 118 Словесные палиндромы
"""

# def is_palindrom(str_: str) -> bool:
#     for i in ['\n', ',', '.', '!', '?', ';', ':', '-']:
#         str_ = str_.replace(i, '')
#     if str_.lower() == " ".join([i for i in str_.lower().split()[::-1]]):
#         return True
#     return False
#
#
# print(is_palindrom("""Information graduate seeks graduate school information"""))

"""
Упражнение 119 Ниже и выше среднего
"""

# def print_lists(list_: list):
#     avg = round(sum(list_)/len(list_), 2)
#     under_avg = []
#     over_avg = []
#     for i in list_:
#         if i <= avg:
#             under_avg.append(i)
#         else:
#             over_avg.append(i)
#     return f"Avg: {avg}\nUnder Avg: {under_avg}\nOver Avg: {over_avg}"
#
# numbers_list = []
# while True:
#     try:
#         number = input("Input number: ")
#         if not number:
#             print(print_lists(numbers_list))
#             break
#         numbers_list.append(int(number))
#     except ValueError:
#         print("Принимаются только целые числа!")

"""
Упражнение 120 Форматирование списка
"""

# def print_format_str(list_: list):
#     format_str = ", ".join(list_)
#     format_str = format_str[::-1].replace(',', 'и ', 1)
#     return format_str[::-1]
#
#
# def input_list():
#     strs_list = []
#     while True:
#         str_ = input("Str ")
#         if not str_:
#             break
#         strs_list.append(str_)
#     return print_format_str(strs_list)
#
# print(input_list())

"""
Упражнение 121. Случайные лотерейные номера
"""

# def random_list():
#     win_ticket = random.sample(range(1, 50), 6)
#     my_ticket = random.sample(range(1, 50), 6)
#     return f"Win ticket: {win_ticket}\nYour ticket: {my_ticket}\n" \
#            f"Matched: {len(set(win_ticket).intersection(my_ticket))} numbers"
#
#
# print(random_list())

"""
Упражнение 122. "Поросячья латынь"
"""

# def to_pig_text():
#     str_ = input("Input str: ")
#     str_list = str_.split()
#     check_str = ''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     consonants = list(sorted({chr(i) for i in range(97, 123)}.difference(vowels)))
#     for i, j in enumerate(str_list):
#         for k in j:
#             if k in vowels and k == j[0]:
#                 str_list[i] = j + 'way'
#                 break
#             elif k in consonants:
#                 check_str += k
#             elif k in vowels:
#                 str_list[i] = j[len(check_str):] + check_str + 'ay'
#                 check_str = ''
#                 break
#     return " ".join(str_list)
#
# print(to_pig_text())

"""
Упражнение 123. "Поросячья латынь" (продолжение)
"""

# def to_pig_text():
#     str_ = input("Input str: ")
#     str_list = str_.lower().split()
#     p = [',', '.', '!', '?', ';', ':', '-']
#     for i, j in enumerate(str_list):
#         for k in p:
#             if k in j and len(j) > 2:
#                 str_list[i] = j[:-1]
#                 str_list.insert(i+1, f"{k} ")
#                 break
#     check_str = ''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     consonants = list(sorted({chr(i) for i in range(97, 123)}.difference(vowels)))
#     for i, j in enumerate(str_list):
#         for k in j:
#             if k in vowels and k == j[0]:
#                 str_list[i] = j + 'way'
#                 break
#             elif k in consonants:
#                 check_str += k
#             elif k in vowels:
#                 str_list[i] = j[len(check_str):] + check_str + 'ay'
#                 check_str = ''
#                 break
#     return "".join(str_list).capitalize()
#
# print(to_pig_text())

"""
Упражнение 125. Тасуем колоду карт
"""

# def snuffle(deck: list):
#     for key in range(2):
#         for i in range(random.randint(5, 10)):
#             first = random.randint(0, len(deck) - 1)
#             deleted = deck[first:random.randint(first, len(deck) - 1)]
#             deck = list(set(deck).difference(deleted))
#             deck.insert(random.randint(0, len(deck) - 1), deleted)
#             count = 0
#             del_index = deck.index(deleted)
#             deck.pop(del_index)
#             for j in deleted:
#                 deck.insert(del_index + count, j)
#                 count += 1
#         for i in range(random.randint(10, 60)):
#             deck.insert(random.randint(0, len(deck) - 1), deck.pop(random.randint(0, len(deck) - 1)))
#     return deck
#
#
# def create_deck():
#     deck = []
#     for i in [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']:
#         for j in ['s', 'h', 'd', 'c']:
#             deck.append(f"{i}{j}")
#     return snuffle(deck)

# print(create_deck())

"""
Упражнение 126. Раздача карманных карт
"""

# class Player:
#
#     def __init__(self):
#         self.__player_cards = []
#
#     def add_card(self, value):
#         self.__player_cards.append(value)
#
#     @property
#     def get_cards(self):
#         return self.__player_cards
#
#
# def deal(players: int, card_value: int, deck: list):
#     new_deck = deck.copy()
#     players_list = []
#     for i in range(players):
#         player = Player()
#         players_list.append(player)
#     for i in range(card_value):
#         for j in players_list:
#             j.add_card(new_deck.pop(0))
#     for i, j in enumerate(players_list):
#         print(f"№{i + 1} player's cards: {j.get_cards}")
#
#
# deal(3, 6, create_deck())  # create_deck из 125 задачи

"""
Упражнение 127. Список уже отсортирован?
"""

# def is_sorted(list_: list) -> bool:
#     if list_ == sorted(list_):
#         return True
#     return False
#
# print(is_sorted([1, 2, -1, 4]))

"""
Упражнение 128. Подсчитать элементы в списке
"""

# def count_range(list_: list, min_: int, max_: int) -> int:
#     count = 0
#     for i in list_:
#         if max_ > i >= min_:
#             count += 1
#     return count
#
#
# print(count_range([1, 2, 3, 4, 0.3, 123, 4345, 435, -34, 342, 0.12], 1, 200))

"""
Упражнение 129. Разбиение строки на лексемы
"""



"""
Упражнение 138. Текстовые сообщения
"""

# phone_symbols = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}
#
# def need_press_buttons(text: str, dictionary: dict) -> str:
#     text = text.upper()
#     message_str = ''
#     for i in text:
#         for j in phone_symbols.keys():
#             if i in phone_symbols[j]:
#                 message_str = message_str + str(j)*(phone_symbols[j].index(i) + 1)
#     return message_str
#
#
# print(need_press_buttons('Hello, world!', phone_symbols))

"""
Упражнение 142. Уникальные символы
"""

# def unique_symbols(str_: str) -> str:
#     return f"В строке '{str_}', {len(set(str_))} уникальных символов"
#
# print(unique_symbols('Hello world!'))

"""
Упражнение 146. Карточка лото
"""

# def lotto_ticket():
#     win_word = ['B', 'I', 'N', 'G', 'O']
#     ran_numbers = [random.randint(1, 90) for number in range(5)]
#     return print_ticket(dict(zip(win_word, ran_numbers)))
#
#
# def print_ticket(ticket: dict):
#     for i in ticket.keys():
#         print(f'|{i:>2s}', end='')
#     print('|')
#     for i in ticket.values():
#         print(f'|{str(i):>2s}', end='')
#     print('|')
#
# lotto_ticket()

"""
Упражнение 173. Сумма значений
"""

# def rec_sum_numbers():
#     if not (number := input()):
#         return 0
#     else:
#         return rec_sum_numbers() + int(number)
#
# print(rec_sum_numbers())


"""
*****
"""
# def moving_rings(rings: int):
#     A = [i for i in range(1, rings + 1)][::-1]
#     B = []
#     C = []
#     count = 0
#     while True:
#         if not A and not B:
#             break
#         print(A, B, C)
#         time.sleep(1)
#         count += 1
#         if A:
#             if not C:
#                 C.append(A.pop(-1))
#             elif not B and len(A) != 1:
#                 B.append(A.pop(-1))
#             elif not B and len(A) == 1 and A[-1] < C[-1]:
#                 C.append(A.pop(-1))
#             elif not B:
#                 B.append(C.pop(-1))
#             elif B[-1] > C[-1]:
#                 B.append(C.pop(-1))
#             elif B[-1] < C[-1]:
#                 C.append(B.pop(-1))
#         else:
#             if len(B) > 1:
#                 A.append(B.pop(-1))
#             else:
#                 C.append(B.pop(-1))
#     return A, B, C, count
#
#
# print(moving_rings(3))

