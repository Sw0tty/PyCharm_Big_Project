import matplotlib.pyplot as plt
import numpy as np


# simple generator
# list_ = [i**2 for i in range(10)]
#
# print([2, 1, 1, 2, 4].index(2, 1, 4))
#
# print([(x, y) for x in range(3) for y in range(3)])

"""
Глава 2
"""

# ------------
# employees = {'Alice': 100000,
#              'Bob': 99817,
#              'Carol': 122908,
#              'Frank': 88123,
#              'Eve': 93121}
#
# print([(key, value) for key, value in employees.items() if value >= 100000])
# ------------

# ------------
# text = '''
# Call me Ishmael. Some years ago - never mind how long precisely - having
# little or no money in my purse, and nothing particular to interest me
# on shore, I thought I would sail about a little and see the watery part
# of the world. It is a way I have of driving off the spleen, and regulating
# the circulation. - Moby Dick'''
# # Однострочник
# w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]
# print(w)
# ------------

# ------------
# print([line.strip() for line in open('one_liners.py')])
# ------------

# ------------
# txt = ['lambda functions are anonymous functions.',
#        'anonymous functions dont have a name.',
#        'functions are objects in Python.']
#
# print(mark := [('anonymous' in line, line) for line in txt])
# # OR
# mark2 = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
# print(list(mark2))
# ------------

# ------------
# letters_amazon = '''
# We spent several years building our own database engine,
# Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
# service with the same or better durability and availability as
# the commercial engines, but at one-tenth of the cost. We were
# not surprised when this worked.
# '''
#
# self_find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
# print(self_find(letters_amazon, 'SQL'))
# ------------

# ------------
# price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
#          [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
#          [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
#          [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
#
# print([i[::2] for i in price])

# УПРАЖНЕНИЕ 2.2
# Вернитесь к этому однострочнику после изучения главы 3 и попробуйте
# написать его более лаконичный вариант с помощью возможностей библиотеки NumPy.
# Подсказка: воспользуйтесь расширенными возможностями срезов NumPy.
# ------------

# ------------
# visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
#             'Safari', 'corrupted', 'Safari', 'corrupted',
#             'Chrome', 'corrupted', 'Firefox', 'corrupted']
#
# visitors[1::2] = visitors[::2]
# print(visitors)
# ------------

# ------------
# cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
# expected_cycles = cardiac_cycle[1:-2] * 10
# plt.plot(expected_cycles)
# plt.show()
# ------------

# ------------
# companies = {
#         'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
#         'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
#         'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
# }
#
# illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
# print(illegal)
# ------------

# ------------
# column_names = ['name', 'salary', 'job']
# db_rows = [('Alice', 180000, 'data scientist'),
#            ('Bob', 99000, 'mid-level manager'),
#            ('Frank', 87000, 'CEO')]
#
# db = [dict(zip(column_names, i)) for i in db_rows]
# print(db)
# ------------

"""
Глава 3
"""

# ------------
# # Создание одномерного массива
# a = np.array([1, 2, 3])
# print(a)
#
# # Создание двумерного массива
# b = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(b)
#
# # Создание трехмерного массива
# c = np.array([[[1, 2, 3], [4, 5, 6]],
#               [[7, 8, 9], [7, 8, 9]]])
# print(c)
# ------------

# ------------
# simple operations
# a = np.array([[1, 0, 0],
#               [1, 1, 1],
#               [2, 0, 0]])
#
# b = np.array([[1, 1, 1],
#               [1, 1, 2],
#               [1, 1, 2]])
#
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# max_element = np.max(a)
# min_element = np.min(a)
# average_element = np.average(a)
# print(c)
# print(d)
# print(e)
# print(f)
# print(max_element)
# print(min_element)
# print(average_element)
# ------------

# ------------
# # Данные: годовые зарплаты в тысячах долларов (за 2017, 2018 и 2019 гг.)
# alice = [99, 101, 103]
# bob = [110, 108, 105]
# tim = [90, 88, 85]
# salaries = np.array([alice, bob, tim])
# taxation = np.array([[0.2, 0.25, 0.22],
#                      [0.4, 0.5, 0.5],
#                      [0.1, 0.2, 0.1]])
#
# max_income = np.max(salaries - salaries * taxation)
# print(max_income)
# ------------

# ------------
# a = np.array([[0, 1, 2, 3],
#               [4, 5, 6, 7],
#               [8, 9, 10, 11],
#               [12, 13, 14, 15]])
#
# print(a[:, 2])  # [2 6 10 14] Третий столбец
# print(a[3, :])  # [12 13 14 15] Четвертая строка
# print(a[1, ::2])  # [4 6] Каждый второй элемент второй строки
# print(a[::2, 2])  # [2 10] Каждый второй элемент третьего столбца
# print(a[:, :-1])  # все столбцы, кроме последнего
# print(a[:-2])  # все, кроме двух последних строк. Аналог: a[:-2, :]
# ------------

# ------------
# Транслирование (broadcasting)
# a = np.array([1, 2, 3, 4])
# b = np.array([[2, 1, 2],
#               [3, 2, 3],
#               [4, 3, 4]])
# c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
#               [[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
#
# print(a.shape)
# print(b.shape)
# print(c.shape)
# ------------

# ------------
# dataScientist = [130, 132, 137]
# productManager = [127, 140, 145]
# designer = [118, 118, 127]
# softwareEngineer = [129, 131, 137]
# employees = np.array([dataScientist,
#                       productManager,
#                       designer,
#                       softwareEngineer])
# employees[0, ::2] = employees[0, ::2] * 1.1
# print(employees)
# ------------

# ------------
x = np.array([[1, 0, 0],
              [0, 2, 2],
              [3, 0, 0]])
print(np.nonzero(x))
print(x == 2)
# ------------

# ------------
X = np.array(
             [[42, 40, 41, 43, 44, 43],  # Гонконг
              [30, 31, 29, 29, 29, 30],  # Нью-Йорк
              [8, 13, 31, 11, 11, 9],  # Берлин
              [11, 11, 12, 13, 11, 12]])  # Монреаль
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])
# Однострочник
polluted = set(cities[np.nonzero(X > np.average(X))[0]])
# 1) X > np.average(X)  Сравнение каждого элемента со средним значением всего массива = ~24
# 2) np.nonzero(X > np.average(X)) Получение кортежей с индексами, которые больше среднего
# 3) np.nonzero(X > np.average(X))[0] Берем первый кортеж, который указывает в кокой строке нужные элементы
# 3) cities[np.nonzero(X > np.average(X))[0]] Отбираем все города по индексу подходязих элементов
# 4) set(cities[np.nonzero(X > np.average(X))[0]]) Убираем повторные элементы и получаем города
# Результат
print(polluted)
# ------------






