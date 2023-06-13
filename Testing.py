import datetime
import random
import time
import ctypes
from math import pi as PI
from decimal import Decimal

import threading


def letterCombinations(digits: str):
    comb = []
    letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if not digits:
        return comb
    elif len(digits) == 1:
        return list(letters[digits])
    for i in letters[digits[0]]:
        comb.extend([i]*(len(letters[digits[0]])*len(digits)))


    # count = 0
    # while True:
    #     for i in letters[digits[count]]:
    #         for j in i:
    #             for k in letters[digits[count + 1]]:
    #                 for h in k:
    #                     comb.append(f"{j}{h}")
    #     if count + 1 == len(digits) - 1:
    #         break
    #     count += 1
    return comb

print(letterCombinations('234'))
dddd = "North East South West"
print(" ".join(dddd.split()[:3])+"...")

ff = {'user': 2}
print(ff.get('user'))
# print([i for i in time.localtime()[2::-1]])
print(datetime.datetime.now())
breakpoint()
result = float(Decimal('0.6') - Decimal('0.1'))
print(type(result))

print(float("inf"), float("-inf"), float("nan"))

seq = ["1", "435", "65", "-57"]
print(max(seq, key=str))
print(2.1.is_integer())

def go(direction):
    match direction:
        case "North" | "East" | "South" | "West":
            return "Хорошо, я пошел!"
        case _:
            return "Неизвестное направление..."

print(go("North"))
print(go("asfasdf"))

print((lambda x: x + 3)(13))


def func(x):
    intermediate_var = x**2 + x + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var ** 3 + 1

    # setting attributes here
    func.optional_return = intermediate_var
    func.is_awesome = 'Yes, my function is awesome.'

    return y

y = func(3)
print(func(3))
def show_letters(some_str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])


random_str = show_letters('A!sdf 09 _ w')
print(next(random_str))
print(next(random_str))

# -------------------------------------
def writer(x, event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wait()  # wait for event
        event_for_wait.clear()  # clean event for future
        print(x)
        event_for_set.set()  # set event for neighbor thread


# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=writer, args=(0, e1, e2))
t2 = threading.Thread(target=writer, args=(1, e2, e1))

# start threads
t1.start()
t2.start()

e1.set()  # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
# -------------------------------------



class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        return self.length*self.width


class Cube(Rectangle):

    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(2, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

print(Rectangle.__dict__)
def sum_(*args):
    return sum(args)

lpp = random.shuffle([1, 3, 4, 1])
print(lpp)

class O: ...
class A(O): ...
class B(O): ...
class C(O): ...
class D(O): ...
class E(O): ...
class K1(A, B, C): ...
class K2(B, D): ...
class K3(C, D, E): ...
class Z(K1, K2, K3): ...

def print_mro(T):
    print(*[i.__name__ for i in T.mro()], sep=' -> ')

print_mro(Z)

def int_to_roman(num):
    str_ = ''
    roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                  5: 'V', 4: 'IV', 1: 'I'}
    for i, j in roman_dict.items():
        str_ += j * (num // i)
        num -= i * (num // i)
        if not num:
            break
    return str_


print(int_to_roman(3114))



def romanToInt(s):
    sum_ = 0
    roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
                  'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    count = 0
    for i, j in enumerate(s):
        if count > 0:
            count = 0
            continue
        if j in ['I', 'C', 'X']:
            try:
                if j + s[i + 1] in roman_dict:
                    sum_ += roman_dict[j + s[i + 1]]
                    count += 1
                else:
                    sum_ += roman_dict[j]
            except IndexError:
                sum_ += roman_dict[j]
        else:
            sum_ += roman_dict[j]
    return sum_

print(romanToInt('DCXXI'))

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print(divmod(6, 6))
def sol_lst(lst):
    sum_ = 0
    new_lst = []
    for i in lst:
        if i < 30 and i % 3 == 0:
            new_lst.append(i)
        else:
            sum_ += i
    return f"Список отобранных элементов: {new_lst}\nСумма остльаных элементов: {sum_}"

print(sol_lst(lst))
def rev_words(str_):
    l_str_ = str_.split()
    str_ = " ".join(l_str_[::-1])
    return str_

print(rev_words("My name is Michele"))


def first_and_last(dif_list):
    return [dif_list[0], dif_list[-1]]

print(first_and_last([random.randint(1, 100) for i in range(10)]))

def start_game():
    count = 0
    number = random.randint(0, 9)
    print("Число загадано.")
    return count, number


game_stats = []
count, number = start_game()
while True:
    count += 1
    answer = int(input("Есть варианты? "))
    if answer < number:
        print("Загаданное число больше")
    elif answer > number:
        print("Загаданное число меньше")
    else:
        print("Да! Вы угадали!")
        game_stats.append((count, number))
        answer = input("Сыграем еще раз?(yes - да) ")
        if answer == 'yes':
            count, number = start_game()
            continue
        else:
            for i, j in enumerate(game_stats):
                print(f"Вот ваши результаты:\n\tВ партии №{i + 1} вам понадобилось {j[0]} попыток,"
                      f"чтобы отгадать число {j[1]}")
            break

choice_list = ['Камень', 'Ножницы', 'Бумага']
while True:
    choice = input("Чем сходите? ")
    if choice.lower().title() not in choice_list:
        print("Такой фигуры нет в этой игре")
        continue
    ai = random.choice(choice_list)
    if ai == choice_list[0] and choice.lower().title() == choice_list[1] or \
       ai == choice_list[1] and choice.lower().title() == choice_list[2] or \
       ai == choice_list[2] and choice.lower().title() == choice_list[0]:
        print(f"Компьютер выбрал {ai}, а вы выбрали {choice.lower().title()}. Вы проиграли")
    elif ai == choice.lower().title():
        print(f"Компьютер выбрал {ai}, а вы выбрали {choice.lower().title()}. Ничья!")
    else:
        print(f"Компьютер выбрал {ai}, а вы выбрали {choice.lower().title()}. Вы выиграли")
    break


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


u_list = [['Masha', 25, 'Female'], ['Spike', 22, 'Male']]

u_dict = {1: ['Masha', 25, 'Female'], 2: ['Spike', 22, 'Male']}
u_objects = []
print(u_dict[1])
for i in u_dict:
    user = User(*u_dict[i])
    print(user.name, user.age, user.gender)
# for i in u_list:
#     user1 = User(i[0], i[1], i[2])
#     u_objects.append(user1)
#     print(user1.name, user1.gender)


in_number = int(input("Для какого числа вывести все делители? "))
a = [1]
for i in range(2, in_number + 1):
    if in_number % i == 0:
        a.append(i)
print(a)

DD = {1: '1', 2: '2'}
DD[3] = DD.pop(1)
DD = dict(sorted(DD.items(), key=lambda x: x[0]))
print(DD)
rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for position in range(11):
    print('^' * 27)
    for letter in rus_lower:
        if rus_lower.index(letter) % 11 == position:
            print('| ', letter.upper(), letter, ' |', end='')
    print()
print('^' * 27)



def check_pass(pswd: str):
    D = {1: ['Длинна пароля меньше 8 символов', True], 2: ['Нет заглавного символа', True],
         3: ['Нет строчного символа', True], 4: ['Нет числа', True],
         5: ['Нет спец символа', True]}
    if len(pswd) >= 8:
        D[1][1] = False
    for i in pswd:
        if i.isupper():
            D[2][1] = False
        if i.islower():
            D[3][1] = False
        if i.isdigit():
            D[4][1] = False
        if not i.isdigit() and not i.isalpha():
            D[5][1] = False
        count = 0
        for i in D.values():
            if i[1] == True:
                count += 1
        if count == 0:
            return "Пароль идеален"
    return f"Выявленные недочеты пароля:\n{list(item[0] for item in D.values() if item[1] == True)}"


print(check_pass('fF1#23499'))

def shortener(str_):
    while '(' in str_ or ')' in str_:
        left = str_.rfind('(')
        right = str_.find(')', left)
        str_ = str_.replace(str_[left:right + 1], '')
    return str_

print(shortener('fdg(dfdg) () dgg (fghfg(dfgdfg)) bbb'))

def camel(str_: str) -> str:
    n_str = ''
    count = 2
    for i in str_:
        if i.isalpha():
            n_str += i.upper() if count % 2 == 0 else i.lower()
        else:
            n_str += i
            continue
        count += 1
    return n_str


print(camel('Gfg fghgjnynnn, !$ #yjkkkbxxzgGGGf ff'))

def top3(str_: str) -> str:
    str_ = str_.lower().replace(' ', '')
    D = sorted({item: str_.count(item) for item in str_}.items(), key=lambda x: x[1], reverse=True)
    s1, s2, s3 = D[0:3]
    return f"{s1[0]}-{s1[1]}, {s2[0]}-{s2[1]}, {s3[0]}-{s3[1]}"

print(top3('Gfg fghgjnynnnyjkkkbxxzgGGGf ff'))

def search_substr(substr: str, str_: str) -> str:
    return "Есть контакт!" if substr.lower() in str_.lower() else "Мимо!"


print(search_substr('ЛЬ', 'Пальма'))


def first_last(letter: str, str_: str) -> tuple:
    if letter.lower() not in str_.lower():
        return ('None', 'None')
    return (str_.lower().find(letter.lower()), str_.lower().rfind(letter.lower()))

print(first_last('п', 'пальпма'))

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return f"На счету: {self.__balance}"

    def deposit(self, amount):
        self.__balance += amount
        return f"Транзакция проведена. {self.get_balance()}"

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Транзакция проведена. {self.get_balance()}"
        else:
            return "Недостаточно средств"

    def __str__(self):
        return f"Сотояние счета на данный момент составляет ${self.__balance:,.2f}"


account = BankAccount(100)
print(account.get_balance())
print(account.deposit(1000))
print(account.withdraw(100))
print(account)

class Coin:
    def __init__(self):
        self.__sideup = 'Орел'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup


toss1 = Coin()
toss2 = Coin()
toss3 = Coin()
toss1.toss()
toss2.toss()
toss3.toss()


print(toss1.get_sideup(), toss2.get_sideup(), toss3.get_sideup())

ll = ['один', 'два']
my_set = set(ll)
print(my_set)
my_set.discard('3')
print(my_set)
phonebook = {'Крис': '919-555-1111', 'Кэти': '828-555-2222', 'Джоанна': '704-555-3333', 'Курт': '919-555-3333'}
# phonebook_copy = {item: phonebook[item] for item in phonebook if phonebook[item].startswith('919')}
phonebook_copy = {item: value for item, value in phonebook.items() if value.startswith('919')}
print(phonebook_copy)
def set_gen(lst):
    lst = {i: lst.count(i) for i in lst}
    lst = {str(i)*j for i, j in lst.items()}
    return lst

print(set_gen([1, 1, 1, 3, 3, 3]))




t_set = {i for i in range(0, 10)}
ttt = [i for i in range(0, 10)]
t_str = "1234"
print(t_set.issuperset(ttt))
print(set(t_str))
def tpl_sort(tpl: tuple):
    for i in tpl:
        if type(i) != int:
            return tpl
    tpl = tuple(sorted(tpl))
    return tpl
tpl = 8, 3, 1, 32, 5
print(tpl_sort(tpl))



def to_dict(lst):
    return {key: str(key) for key in lst}
print(to_dict([i for i in range(0, 10)]))


my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    # key, value = kwargs
    # my_dict[key] = value
    my_dict.update(kwargs)
    return my_dict
print(biggest_dict(mdict=2, name='Leme'))

def count_it(sequence):
    # Берем значение из списка, делаем из него ключ и считаем для значения
    sequence_dict = {str(key): sequence.count(key) for key in sequence}
    # Сортируем по значению 'key=lambda el: el[1]'
    sequence_dict = dict(sorted(sequence_dict.items(), key=lambda el: el[1], reverse=True))
    return sequence_dict
print(count_it('11144333355555551111111111333'))


# def replace_elements(dct: dict):
#     first, last = list(dct.items())[0], list(dct.items())[-1]
#     list(dct.items())[0], list(dct.items())[-1] = list(dct.items())[-1], list(dct.items())[0]
#     dct.pop(last[0])
#     #
#     # print(dct)
#     dct[first[0]] = dct[last[0]]
#     # dct[last[0]] = last[1]
#     return dct
# print(replace_elements({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}))

tl1 = ['Эйнштейн', 'Ньютон', 'Коперник', 'Кеплер']
for name in tl1:
    print(name)
numbers_l = [i for i in range(0, 5)]
numbers_l2 = numbers_l.copy()
print(numbers_l2 is numbers_l)
print(id(numbers_l), id(numbers_l2))
print(numbers_l, numbers_l2)
numbers_l.append(33)
print(numbers_l, numbers_l2)
print('dsgF№f32423v3'.endswith('vf3'))

tl1 = [2, 4, 8, 9]
tl2 = [i ** 2 for i in tl1]
print(tl2)
t1 = tuple(i for i in range(10))
print(t1)
t1 = list(t1)
t1.insert(0, 33333)
t1 = tuple(t1)
print(t1)

l1 = [[0] * 4 for i in range(1, 4)]
for i in range(len(l1)):
    for j in range(len(l1[0])):
        l1[i][j] = random.randint(0, 100)
print(l1)
r = ['ананас', 7, 1, 2, 3, 5]
r = [str(i) for i in r]
r.append('ананас')
r.sort()
r = list(map((lambda x: int(x) if x.isdigit() else x.title()), r))
# for i in r:
#     r[r.index(i)] = int(i) if i.isdigit() else i.title()
r.remove(3)
print(r)
del r[1:3]
print(r)
# r.remove(1)
# r.remove(1)
# r.insert(0, 2)
# print(r)


def test(first, *args):
    print(first)
    for i in args:
        print(i, "args")

test(3, 5, 6, 4, 23, 2)
# ----------How Work Iterator------------
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


simp = SimpleIterator(5)


for i in simp:
    print(i)
# ----------------------
# str_ = iter("123456")
# while True:
#     ques = input("Дальше?")
#     if ques:
#         print(next(str_))
# ----------------------

numbers_str = "33333"
new_str = ""
for i, j in enumerate(numbers_str):
    if i == 2:
        new_str += "$"
        continue
    new_str += j
print(new_str)

print(isinstance(numbers_str, int | bool | str))
A1 = range(10)
A5 = {i: i*i for i in A1}
print(A5)

b = 4 + 3j
print(type(b), b)
print(time.strftime("%Y-%m-%d"))

fr = 5
print(fr.bit_count())
amount = '1.1'
amount = float(amount)
if int(amount) == float(amount):
    amount = int(amount)
amount = str(amount)
amount.capitalize()
gg = '2344325545533313'
print(gg[-2::1])
print(gg[-2])

print([str(i) for i in range(6, 21)])

def sum_numbers(first_number, second_number):
    return first_number + second_number


again = "д"
while again.lower() == "д":
    first_number = random.randint(0, 1000)
    second_number = random.randint(0, 1000)
    print(f"Сколько будет:\n{first_number} + {second_number}?")
    answer = int(input("Ваш ответ: "))
    if answer == sum_numbers(first_number, second_number):
        print("Верно!")
    else:
        print(f"Ошибка! Правильный ответ: {sum_numbers(first_number, second_number)}")
    again = input("Еще пример? д = да")


def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300:
        return True
    else:
        return False

model = int(input("Модель"))
while is_invalid(model):
    model = int(input("Модель"))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("Число на проверку "))
if is_even(number):
    print("Число четное")
else:
    print("Число не четное")

print(random.uniform(0.1, 0.5))
print(random.choices(['f', 'g', 6, 'hello'], k=4))
print(random.choice(('f', 'g', 6, 'hello')))
HEAD = 1
TAIL = 2
TOSSES = 10
def rand_number():
    count = 0
    for toss in range(TOSSES):
        if random.randint(HEAD, TAIL) == HEAD:
            count += 1
            print("Орел")
        else:
            print("Решка")
    return f"Орел выпал {count} раз(а). А Решка выпала {TOSSES - count} раз(а)."

print(rand_number())


print(round(PI, 2))
SKID = 0.1
count = 0

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print(array)


def rec_fact(number):
    if number == 0:
        return 1
    else:
        return number * rec_fact(number - 1)


print(len(str(rec_fact(100))))


def main(num1, num2):
    return f"Сумма чисел {num1} и {num2} равняется {sum_(num1, num2)}"


def sum_(num1, num2):
    return num1 + num2


print(main(12, 45))

for i in range(5, -1, -1):
    print("#", " " * i, "#", sep="")
minutes_in_day = 0
for hour in range(24):
    for minutes in range(60):
        minutes_in_day += 1
print(minutes_in_day)
print("Число\tЕго квадрат")
for i in range(1, 10):
    print(f"{i}\t\t\t{i**2:02}")

bal_dict = ["A", "B", "C", "D", "F"]

bal = int(input("Сколько вы набрали баллов? "))
if bal >= 90:
    print(f"Ваша оценка {bal_dict[0]}")
elif bal >= 80:
    print(f"Ваша оценка {bal_dict[1]}")
elif bal >= 70:
    print(f"Ваша оценка {bal_dict[2]}")
elif bal >= 60:
    print(f"Ваша оценка {bal_dict[3]}")
else:
    print(f"Ваша оценка {bal_dict[-1]}")

print("Нью-Йорк" > "Бостон")

str_ = ""
for i in range(70, 75):
    str_ += chr(i)
print(str_)

count = 0
for i in "Mary":
    count += ord(i)
print(count)

if "Mary" > "Mark":
    print("Строка 'Mary' больше")
else:
    print("Строка 'Mark' больше")


print("a" < "b")

number = 1234567.456
print(f"{number:,.1f}")
val = 45
print(val - (val * SKID))

data = [13, 25, 13, 34]
sum_ = 0
for i, el in enumerate(data):
    print(f"{i} = {el}")
print(sum_)

print(input("Что вывести? "))
print(type(input()))
graph = {0: [1, 2, 3],
         1: [0, 2],
         2: [0, 1],
         3: [0]}

user32 = ctypes.windll.user32
W = ctypes.windll.user32.GetSystemMetrics(0)
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print(W)
stroka = "    fgfg f gdf g     "
print(stroka.lstrip() + "tttttt")
stroka = "H"
print(stroka.ljust(3, "-") + "tttttt")

def create_phone_number(n):
    return f"""({"".join(n[0:3])}) {n[3:6]}-{n[6:]}"""


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number2("2231143141"))

a = [1, 3, 41, 56, 74, 23]
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
player_rect_reaction = 0  # заводим счётчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохранённым,
        player_rect_reaction += 1  # то увеличиваем счётчик
    else:
        result += last + str(player_rect_reaction)  # иначе записываем в результат
        last = c  # и обновляем сохранённый символ с его счётчиком
        player_rect_reaction = 1

result += last + str(player_rect_reaction)  # и добавляем в результат последний символ
print(result)


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


# -------Выборка из сложных списков--------
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1])  # выведет 'baz'
# ---------------

# ------Сортировка, удаление---------
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
