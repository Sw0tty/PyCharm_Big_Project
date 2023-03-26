import math
import string
from my_functions import input_number

# Напишите несколько строк кода, выводящих на экран ваше имя и почто-
# вый адрес. Адрес напишите в формате, принятом в вашей стране. Ника-
# кого ввода от пользователя ваша первая программа принимать не будет,
# только вывод на экран и больше ничего.

# name = "Кирилл"
# post_address = "1470"
# print(f"Приверт {name}. Ваш почтовый адрес {post_address}")

# Напишите программу, запрашивающую у пользователя его имя. В ответ
# на ввод на экране должно появиться приветствие с обращением по имени,
# введенному с клавиатуры ранее.

# name = input("Как вас зовут? ")
# print(f"{name}, приятно познакомиться!")

# Напишите программу, запрашивающую у  пользователя длину и  ширину
# комнаты. После ввода значений должен быть произведен расчет площади
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами
# измерения, принятыми в вашей стране. Это могут быть футы или метры.

# HEIGHT = float(input("Введите длину комнаты "))
# WIDTH = float(input("Введите ширину комнаты "))
#
# print(f"Площадь вашей комнаты {HEIGHT * WIDTH} квадратных метров")

# Создайте программу, запрашивающую у пользователя длину и  ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.
# Подсказка. В одном акре содержится 43 560 квадратных футов.

# akr = 43560
# HEIGHT = float(input("Введите длину участка "))
# WIDTH = float(input("Введите ширину участка "))
#
# print(f"Площадь вашего участка {akr / (HEIGHT * WIDTH)} акров")

# Во многих странах в стоимость стеклотары закладывается определенный
# депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
# тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
# ки большего объема – $0,25.
# Напишите программу, запрашивающую у пользователя количество бу-
# тылок каждого размера. На экране должна отобразиться сумма, которую
# можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
# вывод так, чтобы сумма включала два знака после запятой и дополнялась
# слева символом доллара.

# tara1 = ""
# tara2 = ""
# while not tara1.isdigit():
#     tara1 = input("Сколько у вас бутылок 1 и меньше литров? ")
# while not tara2.isdigit():
#     tara2 = input("Сколько у вас бутылок больше 1 литра? ")
#
# tara1, tara2 = int(tara1), int(tara2)
# print(f"Продав все бутылки, вы сможите выручить ${round(tara1 * 0.1 + tara2 * 0.25, 2)}")

# Программа, которую вы напишете, должна начинаться с запроса у поль-
# зователя суммы заказа в ресторане. После этого должен быть произведен
# расчет налога и  чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
# де программа должна отобразить отдельно налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.

# Напишите программу, запрашивающую у пользователя число и подсчи-
# тывающую сумму натуральных положительных чисел от 1 до введенного
# пользователем значения.

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

# Интернет-магазин занимается продажей различных сувениров и безде-
# лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите про-
# грамму, запрашивающую у пользователя количество тех и других покупок,
# после чего выведите на экран общий вес посылки.

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

# Представьте, что вы открыли в банке сберегательный счет под 4 % годо-
# вых. Проценты банк рассчитывает в конце года и добавляет к сумме счета.
# Напишите программу, которая запрашивает у пользователя сумму перво-
# начального депозита, после чего рассчитывает и выводит на экран сумму
# на счету в конце первого, второго и третьего годов. Все суммы должны
# быть округлены до двух знаков после запятой.

# money = ""
# while not money.isdigit():
#     money = input("Сколько денег положить в банк? ")
#
# money = int(money)
# print("--Сберегательный счет под 4% годовых успешно открыт--")
# for i in range(1, 4):
#     print(f"После года вложения на вашем счете будет: {round(money + ((4 * money) / 100) * i, 2)}")

# Создайте программу, которая запрашивает у пользователя два целых чис-
# ла a и b, после чего выводит на экран результаты следующих математи-
# ческих операций:
# * сумма a и b;
# * разница между a и b;
# * произведение a и b;
# * частное от деления a на b;
# * остаток от деления a на b;
# * десятичный логарифм числа a;
# * результат возведения числа a в степень b.

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

# Напишите программу, запрашивающую у пользователя целое число и вы-
# водящую на экран информацию о том, является введенное число четным
# или нечетным.

# a = ""
# while type(a) != int:
#     a = input_number(input("Введите целое число: "))
#
# if a % 2 == 0:
#     print("Число четное")
# else:
#     print("Число не четное")

# Считается, что один год, прожитый собакой, эквивалентен семи челове-
# ческим годам. При этом зачастую не учитывается, что собаки становятся
# абсолютно взрослыми уже к двум годам. Таким образом, многие предпо-
# читают каждый из первых двух лет жизни собаки приравнивать к 10,5 года
# человеческой жизни, а все последующие – к 4.
# Напишите программу, которая будет переводить человеческий возраст
# в  собачий с  учетом указанной выше логики. Убедитесь, что программа
# корректно работает при пересчете возраста собаки меньше и больше двух
# лет. Также программа должна выводить сообщение об ошибке, если поль-
# зователь ввел отрицательное число.

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

# Разработайте программу, запрашивающую у пользователя букву латин-
# ского алфавита. Если введенная буква входит в следующий список (a, e, i,
# o или u), необходимо вывести сообщение о том, что эта буква гласная. Если
# была введена буква y, программа должна написать, что эта буква может
# быть как гласной, так и согласной. Во всех других случаях должно выво-
# диться сообщение о том, что введена согласная буква.

letter = (input("Введите английскую букву ")).strip()
glasn_letters = "aeiouAEIOUYy"
alphabet = "".join(sorted(set(glasn_letters).symmetric_difference(set(string.ascii_letters))))
if letter in alphabet:
    print("Ввведена согласная буква")
elif letter == "y" or letter == "Y":
    print("Буква может быть и согласной, и гласной")
else:
    print("Буква гласная")


