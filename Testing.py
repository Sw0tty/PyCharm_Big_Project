import random
import time

print(isinstance(13, str))


def create_phone_number(n):
    return f"""({"".join(n[0:3])}) {n[3:6]}-{n[6:]}"""

def create_phone_number2(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

a = [1,3,41,56 ,74, 23]
print(*a)


def new_func(inside_func):
    inside_func()


def hello():
    print("Hello")


new_func(hello)

def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458
print()
# def my_decorator(a_function_to_decorate):
#     def wrapper():
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
#
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return "конец my_function"


# decorated_function = my_decorator(my_function)
# print(decorated_function())



def make_adder(x):
   def adder(n):
       return x + n # захват переменной "x" из nonlocal области
   return adder

add_5 = make_adder(5)
print(type(add_5))
print(add_5(100))


#-----------Вебинар по функция----------------
# yield
def cube_numbers(nums):
    cube_list = []
    for i in nums:
        cube_list.append(i**3)
    return cube_list

print(cube_numbers([1, 2, 3, 4, 5]))

def cube_numbers(nums):
    for i in nums:
        yield (i**3)

print(list(cube_numbers([1, 2, 3, 4, 5])))

generator = (i ** 2 for i in range(10))  # в генераторе можно использовать функцию next()
# генератор - итератор элементы которого можно итерировать только один раз
# итератор - это объект, который поддерживает функцию next(). Помнит о том, какой элемент будет браться следующим
# итерируемы объект - это объект, который предоставляет возможность обойти поочередно свои элементы
print("First")
for i in generator:
    print(i)
print("Second")
for i in generator:
    print(i)

a = [i ** 2 for i in range(10)]
print(a)

#iter()
s = [1, 2, 3]
d = iter(s)
print(next(d))

a = ['2', '5', '5']

a_mod = [int(i) for i in a]
print(a_mod)
def check(n):
    if n < 2:
        return (n % 2 == 0)
    return check(n - 2)

n = int(input("число "))
if check(n) == True:
    print("Число четное")
else:
    print("нечетное")

def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)
rec(1)
#------------111---------------

a = ["asd", "bbd", "ddfa", "mcsa"]
print(list(map(str.upper, a)))
print(list(x.upper() for x in a))
print(list(map(lambda x: x.upper(), a)))

# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]
print(sorted(data, key=lambda x: x[0]/x[1]**2))
print(min(data, key=lambda x: x[0]/x[1]**2))

d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# Чтобы отсортировать его по ключам, нужно сделать так
print(dict(sorted(d.items())))

print(dict(sorted(d.items(), key=lambda x: x[1])))

print(list(map(lambda x: x**2, range(1, 11))))

def positive(x):
    return x % 2 == 0


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))


L_str = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L_str)))

L = [1, 3, 5, -3, 4, -4, 0]

def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(min_list(L))

def D(a, b, c):
    if pow(b, 2) - 4 * a * c < 0:
        return "Нет вещественных корней"
    elif pow(b, 2) - 4 * a * c == 0:
        return -b / (2 * a)
    else:
        return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

print(D(3, 4, 2))



text = "aaabbccccdaa"  # получаем строку

last = text[0]  # сохраняем первый символ
count = 0  # заводим счётчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохранённым,
        count += 1  # то увеличиваем счётчик
    else:
        result += last + str(count)  # иначе записываем в результат
        last = c  # и обновляем сохранённый символ с его счётчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)

# —------Генераторы--------—
L = [i for i in range(0, 10)]
M = [i for i in range(10, 0, -1)]
N = [a*b for a, b in zip(L, M)]
print(N)

L = [i for i in range(0, 10)]
print(any(L))

L = [int(input()) % 2 == 0 for i in range(5)]
print(L)

L = [input() for i in range(3)]
print(L)

multiplication_table = [[i * j for i in range(1, 11)] for j in range(1, 11)]
print(multiplication_table)
for i in multiplication_table:
    for j in i:
        print("%2d" % j, end=" ")
    print()

squares = [i**2 for i in range(1, 11)]
print(squares)

squares = [i**2 for i in range(1, 11) if i % 2 == 1]
print(squares)

list_tuples = [(i, i**2) for i in range(1, 11)]
print(list_tuples)

M = [[i+j for j in range(5)] for i in range(5)]
print(M)
# —--------------—

cook_book = {
'first_el': 'картофель',
'second_el': 'морковь'
}

for i, j in cook_book.items():
    print(f"{i} —- {j}")

a = [1, 3, 5, -3, 4, -4, 0]
b = a[0]

for i in a:
    if i < b:
        b = i
print(b)

print(random.randint(0, 100))
print()

a = [1, 'Hello', 3, [2, 6, 9, "True"]]
for i in a:
    if type(i) == list:
        for j in i:
            print(j)
    print(i)

lllist = ['ffff', 'dsffhgf', 'n555nhg']
print(list(map(len, lllist)))
print(list(len(x) for x in lllist))
print(list(x.upper() for x in lllist))



str_numbers = list(map(int, input().split()))
print(str_numbers)
print(not any(str_numbers))

a = int(input())

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")


if type(a) == int:
    print("Число целое")
if a in range(100, 1000):
    print("Входит в промежуто от 100 до 999")
if a % 3 == 0:
    print("Делится на 3")
if a % 2 == 0:
    print("Делится на 2")

some_var = (2,)
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

L = input()
c = set(L)
print(len(c))

a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1
print(a)




def my_decorator(fn):
   def wrapper():
       fn()
   return wrapper  # возвращается задекорированная функция, которая заменяет исходную

# выведем незадекорированную функцию
def my_function():
   pass
print(my_function)  # <function my_function at 0x7f938401ba60>

# выведем задекорированную функцию
@my_decorator
def my_function():
   pass
print(my_function)


def twice_func(inside_func):
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    inside_func()


def hello():
    print("Hello")


test = twice_func(hello)

# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#
#     while True:
#         a, b = b, a + b
#         yield b
#
#
# for i in fib():
#     print(next(i))


def fibanachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibanachi(n - 1) + fibanachi(n - 2)


for i in range(1, 11):
    print(fibanachi(i))
print()


def range_sum(my_list_numbers, start, end):
    if start > end:
        return 0
    else:
        return range_sum(my_list_numbers, start + 1, end) + my_list_numbers[start]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_sum(numbers, 2, 4))


def factr(x):
    if x > 0:
        return factr(x - 1) * x
    return 1


print(factr(4))


def f(k):
    if k > 0:
        return f(k-1) + k
    return 0

print(f(k=int(input())))


def s(k):
    sum_ = 0
    for s in range(1, k-1):
        sum_ += k

print(f(5))
print(s(5))


def rec_str_(str__):
    new_str__ = ""
    return 0

print(rec_str_("abc"))


def wrwr(n):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += i
    return  sum_

print(wrwr(3))

def rec_sum(n):
   if n == 1:  # терминальный случай
       return 1
   return n + rec_sum(n - 1)

print(rec_sum(3))

def rec_fibb(n):
   if n == 1:
       return 1
   if n == 2:
      return 1
   return rec_fibb(n - 1) + rec_fibb(n - 2)

print(rec_fibb(4))


# установим аргумент name_arg пустым, а внутри функции будем проверять его
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[123])


def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_


print(adder(8, 3, 1, 2))

a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
# [[1, 2, 3], 4, 5, 6]

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
# [1, 2, 3, 4, 5, 6]

PI = 3.14
def test(r):
    global PI
    print(PI)
    PI = 3.1415
    return PI * (r ** 2)

print(test(10))

def check_palindrome(your_string):
    your_string = your_string.lower()
    your_string = your_string.replace(" ", "")
    if your_string == your_string[::-1]:
        return "Это палидром"
    else:
        return "Это не палидром"


print(check_palindrome(your_string="Кит на море не романтик"))


def kol_del(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    return count


print(kol_del(x=10))


def stairs(x):
    while x != 0:
        print("*" * x)
        x -= 1

print(stairs(x=6))


def del_func(a, n):
    if a % n == 0:
        print("N делитель A")
    else:
        print("N не делитель A")


print(del_func(a=2, n=2))


def char_frequency(text):
   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчёта символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")


text = input("Введите текст ")
print(char_frequency(text))


def pow_func(base, n=2): # функция, которая возводит любое число в степень n. Без аргумента n пользователя, возведет на 2
   print(base ** n)

pow_func(3)  # 9
pow_func(5, 3)  # 125


def print_2_add_2():
    x = 2 + 2
    print(x)
    return ""

def hello_world():
    print("Hello world!")


print(hello_world())
print(print_2_add_2())
lllist = ['ffff', 'dsffhgf', 'n555nhg']
print(list(map(len, lllist)))
print(list(len(x) for x in lllist))
print(list(x.upper() for x in lllist))

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
person = 5
for dish in cook_book:
    print(f'\n{dish[0].title()}:')
    for food in dish[1]:
        print(f'  {food[0]}, {food[1] * person}{food[2]}')

professions = ['IT', 'Физика', 'Математика']
persons = [['Гейтс', 'Джобс', 'Возняк'], ['Эйнштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]
for pro, person_list in zip(professions, persons):
    print(f'{pro}:')
    for person in person_list:
        print(person)
    print()

data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]
sum_ = 0
for i, el in enumerate(data):
    print(i, el)
    sum_ += el[i]
print(sum_)

# ---------------------------
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Тула', 'Россия']},
    {'visit7': ['Курск', 'Россия']},
    {'visit8': ['Архангельск', 'Россия']}
]
for log in geo_logs:
    print(list(log.values())[0][0], end=" ")
print()
geo_logs_copy = geo_logs.copy()
for log in geo_logs_copy:
    if 'Россия' not in list(log.values())[0]:
        geo_logs.remove(log)
print(geo_logs)
# ------------Метод 2---------------
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Тула', 'Россия']},
    {'visit7': ['Курск', 'Россия']},
    {'visit8': ['Архангельск', 'Россия']}
]
result = []
for log in geo_logs:
    # print(list(log.values())[0])
    if 'Россия' in list(log.values())[0]:
        result.append(log)
print(result)
# ---------------------------

bodycount = {
    'Проклятие Черной жемчужины': {
        'человек': 17
    },

    'Сундук мертвеца': {
        'человек': 56,
        'раков-отшельников': 1
    },

    'На краю света': {
        'человек': 88
    },

    'На странных берегах': {
        'человек': 56,
        'русалок': 2,
        'ядовитых жаб': 3,
        'пиратов зомби': 2
    }
}
dead = 0
for i in bodycount.values():
    for j in i.values():
        dead += j
print(dead)


people = {1: {'name': 'Oleg', 'age': '29', 'sex': 'Male'},
          2: {'name': 'Kate', 'age': '21', 'sex': 'Female'},
          3: {'name': 'Liza', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Pavel', 'age': '36', 'sex': 'Male'}}
age = 0
for i in people.values():
    age += int(i['age'])
print(age / len(people))


europe = {'spain': {'capital':'madrid'},
           'france': {'capital':'paris'},
           'germany': {'capital':'berlin'},
           'norway': {'capital':'oslo'}}
for country, info in europe.items():
    print(f'The capital of {country.title()} is {info["capital"].title()}')

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
for country in countries_temperature:
    print(f"Средняя температура в {country[0]} - {(sum(country[1])/len(country[1])) :.2f} F")

my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = [4, 5, 6, 7]

for number in my_list_1:
    if number in my_list_2:
        print('Такое число есть')
    else:
        print('Такое число не найдено')

data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]
reversed_data = [list(reversed(data[0])), list(reversed(data[1])), list(reversed(data[2])), list(reversed(data[3]))]
reversed_data = list(reversed(reversed_data))
print("Начальный массив")
for i, j, k, g in data:
    print(i, j, k, g)
print()
print("Перевернутый массив")
for i, j, k, g in reversed_data:
    print(i, j, k, g)
sum_ = 0
index = -1
for row in data:
    sum_ += row[index]
    index -= 1
print("Сумма диагонали (справа, в низ) начального массива равна", sum_)

# import time
# i = 10
# while i > -1:
#     print(i)
#     time.sleep(1)
#     i -= 1
# print("Время вышло")

for i in range(1, 10):
    for j in range(1, 10):
        print("%2d" % (i * j), end=" ")
    print()

# for i in range(1, 10):
#     for j in range(1, 11):
#         proz = i * j
#         print(f"{i} x {j} = {proz}")

for i in range(1, 10):
    print(str(i) * i)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
for el1, el2, el3 in my_list:
    print(el1, el2, el3)

for i, v in enumerate("1,2,3,4,5"):
    print(i, v)
print("---------")

n = int(input("Введите число: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

i = 1
sum_ = 0
while i != 0:  # можно заменать на while i: Так как любое число, кроме 0 является True
    i = int(input("Введите целое число: "))
    sum_ += i
print(sum_)

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d, sep="|")

# -------------------------

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "abcdefghijklmnopqrstuvwxyz"
c = "0123456789"
d = "[]{}()!@#$%^&<.?*"

all = a + b + c + d
lenght = 13
password = "".join(random.sample(all, lenght))
print(password)
# -------------------------

data2 = ["fgg", 'hello1']
print(*data2[1])

users_list = [
    ['+13213', 'Bob'],
    ['+8432', 'Mark'],
    ['+94232', 'Kate']
]

users_dict = dict(users_list)
print(users_dict)

users = {
    '+324234': 'Mark',
    '+54356': 'Bob',
    '+536222': 'Kate'
}
users_mod = users['+54356'] = 'Jim'
for key in users:
    print(f"phone {key} user: {users[key]}")

for key, values in users.items():
    items = key, values
    print(items)


data = [1, 4, 5, 3]
for i in data:
    if i == data[-1]:
        print(i)
    else:
        print(i, end=" ")

name = "Ivan"
age = 23
print(f"Меня зовут, {name}, мне {age} года")
def print_ladder(n):
    for i in range(1, n+1):
        print("*" * i)
        i += 1
    return "конец"
print(print_ladder(n=3))
print("\n")

print(list(range(20, 1, -2)))
S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

# --------------------------------

S = 1
N = 5
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение произведения на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S * i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение произведения после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: произведения равно = ", S)
# Та же программа, что и выше, но в упрощенном виде
P = 1
N = 5
for i in range(1, N+1):
    P *= i
print(P)
# --------------------------------

# ---------------------
N = 5
string = "*"
for i in range(1, N+1):
    print(string)
    string = string + "*"
# -----или так----
N = 5
for i in range(1, N + 1):
   print("*" * i)
# ---------------------

def bolshe(a, b, c):
    if a < 45 and (b > 45 and c > 45):
        return True
    if b < 45 and (a > 45 and c > 45):
        return True
    if c < 45 and (a > 45 and b > 45):
        return True
    else:
        return False
print(bolshe(a=344, b=240, c=3440))

num = 1234321

print(str(num) == str(num)[::-1])

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}
def check_user(username, password):
    if username in user_database:
        if user_database[username] == password:
            return True
        else:
            return False
    else:
        return False

print(check_user(username="hesoyam", password="greedisgood"))

def get_wind_class(speed):
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif speed >= 19:
        return "hurricane [4]"


print(get_wind_class(speed=5))

sezon = int(input("Введите цело число от 1 до 12: "))
if sezon in (3, 4, 5):
    print("Весна")
elif sezon in (6, 7, 8):
    print("Лето")
elif sezon in (6, 7, 8):
    print("Лето")
else:
    print("Зима")
def are_both_odd(A, B):
    return A % 2 != 0 and B % 2 != 0
print(are_both_odd(A = 3, B = 2))

x = 1
y = 2

if x > 0 and y > 0:           # x > 0, y > 0
         print("Первая четверть")
if x > 0 and y < 0:                 # x > 0, y < 0
         print("Четвертая четверть")
if x < 0 and y > 0:              # x < 0, y > 0
         print("Вторая четверть")
if x < 0 and y < 0:                # x < 0, y < 0
         print("Третья четверть")

print("\n\n")
# if s_znach == "a":
#     print()
# elif s_znach == "b":
#     print()
# else:
#     print()




# mas = ["Елена", "Петр", "Саша"]  # задание массива
# print("Привет, ", mas[1], "#выборка из массива mas")  # выборка из массива mas
# name = input("Сколько вам лет: ")  # пример взаимодействия

#x = input()



y = 4573574568345

print("3" in str(y) and "7" in str(y))

def leap_year(x):
    return (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))


print(leap_year(x=2700))


my_num = input("Введите число от 0 до 10: ")
str_numbers_lib = {'0': 'Ноль', '1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять', '6': 'Шесть'}
your_num = str_numbers_lib[my_num]
print("Вы ввели", your_num)

# if my_num % 2 == 0:
#     print("Число четное")
# else:
#     print("Число не четное")

print("\n")
if my_num % 2 == 0:
    print("Число четное")
else:
    print("Число не четное")

my_number = int(input("Введите целое число: "))
data = []
while my_number != 0:
    data.append(my_number)
    my_number = int(input("Введите целое число: "))
data.sort()
print(data)

users = [
    [15634602, 15647311, 15619304, 15701354],  # 'CustomerId' (ID)
    ['Hargrave', 'Hill', 'Onio', 'Boni'],  # 'Surname' (Имя)
    [619, 608, 502, 699],  # 'CreditScore' (Кредитный рейтинг)
    ['Female', 'Female', 'Male', 'Female'],  # 'Gender' (Пол)
    [42, 41, 42, 39],  # 'Age' (Возраст)
    [1, 0, 1, 0]  # Exited (Статус (1 = ушел, 0 = все еще клиент))
]
sr_cred_who_ushed = sum(users[2][::2]) / users[5].count(1)
sr_age = sum(users[4]) / len(users[4])
proc_ushed = (users[5].count(1) * 100) / len(users[5])

print("Средний кредитный рейтинг ушедших клиентов:", sr_cred_who_ushed)
print("Средний возраст клиентов:", int(sr_age))
print(proc_ushed, "% ушли")
print(users[0][::2])

print("\n")

config = {
    'server': {
        'host': '127.0.0.1',
        'port': '22'
    },
    'configuration': {
        'ssh': {
            'access': True,
            'login': 'some',
            'password': 'some'
        },
        'name': '2491Oaaf1414'
    }
}
print(config['configuration']['ssh']['access'])

fruit_dict = {
    'Банан': '16 рублей',
    'Яблоко': '28 рублей',
    'Персик': '37 рублей'
}
print(list(fruit_dict.values()))
print(list(fruit_dict.keys()))
print(list(fruit_dict.items()))
print(fruit_dict)
new_price = '20 рублей'
fruit_dict.update({'Банан': new_price})
print(fruit_dict)

fruits = ['Банан', 'Яблоко', 'Персик', 'Манго', 'Апельсин', 'Ананас']
prices = ['16 рублей', '28 рублей', '37 рублей', '100 рублей', '30 рублей', '20 рублей']
fruits_dict = dict(zip(fruits, prices))
print(fruits_dict)
print(fruits_dict.items())

order111 = ["рыба", "молоко", "яйца", "яйца"]
order111.remove("яйца")
pop_element = order111.pop(1)
print(pop_element)
print(order111)

my_list = list(range(-1, 25))
print(my_list[0:9:2])

order1 = 'Заказ: рыба, молоко, яйца'
order2 = 'Заказ: молоко, хлебцы, буженина'
order3 = 'Заказ: батон, вода'
orders = []
orders.append(order1)
orders.append(order2)
orders.append(order3)
print(orders)

order11 = ["рыба", "молоко", "яйца"]
order22 = ["рыба", "молоко", "яйца"]
order33 = ["рыба", "молоко", "яйца"]
orders2 = []
orders2.extend(order11)
orders2.extend(order22)
orders2.extend(order33)
print(orders2)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_before, '\n', list_id_after)
print(list_id_before == list_id_after)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])

shopping_center[-1].append("Uniqlo")

print(shopping_center)

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3 + 2
print(id(a))
print(id(b))
print(id(a) - id(b))

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
a, b = a.split(), b.split()
a_set, b_set = set(a), set(b)
a_and_b = a_set.symmetric_difference(b_set)
a_and_b = list(map(int, a_and_b))
print(sorted(a_and_b))
print(sorted(a_and_b, reverse=True))

unik_word = input("Введите любое слово:")
unik_word = list(set(unik_word))
print(len(unik_word))

title, author, year, = input("Введите название книги:"), input("Введите ее автора:"), input("Введите год издания:")

year = int(float(year))
book = dict()
book['title'] = title
book['author'] = author
book['year'] = year
print(book)

abit1 = {"ФИО": 'Фадеев О.Е.', "Количество баллов": 283, "Заявление": True}
abit2 = {"ФИО": 'Дружинин И.Я.', "Количество баллов": 278, "Заявление": False}
abit3 = {"ФИО": 'Афанасьев Д.Н.', "Количество баллов": 276, "Заявление": True}

abits = [abit1, abit2, abit3]
print(abits)

person = {'name': 'Ivan Petrov'}
# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'
print(person)
print(person['phone'])
print(person.keys())
print(person.values())
person.pop('phone')
print(person)

d = {'day': 22, 'month': 6, 'year': 2015}

print("||".join(d.keys()))

# -------------------------

in_num = input("Введите целое число от 0 до 5: ")
while type(in_num) != int:
    in_num = input("Введите целое число от 0 до 5: ")

mlist = ["ноль", "один", "два", "три", "четыре", "пять"]

print(mlist[in_num])

# -------------------------

# ---------------
print("-" * 20, "\nПерестановка переменных местами")
number1, number2 = 5, 9
print("Дано:", "number1=", number1, "number2=", number2)
number1, number2 = number2, number1
print("number1=", number1, "number2=", number2)
print("-" * 20)
# ---------------

# ---------------

list_of_ints = [80, 443, 8080, 8081]
print(', '.join(map(str, list_of_ints)))  # преобразование списка чисел в строку
# ---------------

# ---------------
print("-" * 20, "\nВыборка из сложных списков")
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1])  # выведет 'baz'
# ---------------

# ---------------
print("-" * 20, "\nСортировка, удаление")
z = [2, 7, 4, 1, 7]
z.sort(reverse=True)
print(z)
z.remove(7)
print(z)
# ---------------

string = input("Введите числа через пробел:")
list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))
list_of_numbers_first = list_of_numbers[0]
list_of_numbers[0] = list_of_numbers[-1]
list_of_numbers[-1] = list_of_numbers_first
list_of_numbers.append(sum(list_of_numbers))
print(list_of_numbers)

# таже программа, но в оптимизированном виде
numbers_list = list(map(float, input("Введите числа через пробел: ").split()))
numbers_list[0], numbers_list[-1] = numbers_list[-1], numbers_list[0]
numbers_list.append(sum(numbers_list))
print(numbers_list)

L = ["а", "б", "в", 1, 2, 3, 4]
print(L[-1:-4:-1])

L1 = ['3.3', '4.4', '5.5', '6.6']

print(list(map(float, L1)))

L2 = [3.3, 4.4, 5.5, 6.6]
# print(map(round, L2))
print(list(map(round, L2)))

# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']
letters.append('e')  # с помощью метода append() мы добавляем ещё один элемент в список
print(letters)
print(letters[len(letters) - 1])

colors = 'red blue green'
print(colors.split())
print(colors)

word = " /home/user/documents/file.txt"
print(word.split("/"))

colors_splited = colors.split()  # список цветов по-отдельности
colors_joined = ' and '.join(colors_splited)  # объединение строк
print(colors_joined)

age = 5

my_age = "I'm " + str(age)
print(my_age)
pi = 31.4159265
print("%.4e" % pi)

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2


my_age = "I'm %03d years old" % age
print(my_age)
my_age = "I'm %12d years old" % age
print(my_age)

numbers = "1 2 3 4 5 6 7"
numbers_splited = numbers.split()
numbers_splited = "\n".join(numbers_splited)
print(numbers_splited)

testword = "р"
print(testword.isdigit())
print(testword.isalpha())
print(testword.isalnum())
