import math
import string
import time

from my_functions import input_number

"""
-+--Ben_Stivenson_Sbornik_uprazhneniy_Python--+-
"""

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
Упражнение 39 Сколько дней в месяце?
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

