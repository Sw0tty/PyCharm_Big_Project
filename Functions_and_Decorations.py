import random
import time
def my_decor(message='Message'):
    def decorated(func):

        def wrapper(arg_for_func):
            print(message)
            print("До")
            func(arg_for_func)
            print("После")
        return wrapper

    return decorated

@my_decor('Yeah')
def print_name(name):
    print(f"Hello, {name}")

print_name('Kirill')  # arg_for_func

def removeDuplicates(nums):
    for i in nums:
        if nums.count(i) > 1 and i != '_':
            for j in range(nums.count(i) - 1):
                nums.remove(i)
                nums.append('_')
    k = len(nums) - nums.count('_')
    return k, nums


# print(removeDuplicates([2, 2, 2, 2, 2]))

def reverse_number(x):
    return int(str(x)[::-1]) if '-' not in str(x) else int('-' + (str(x)[:-len(str(x)):-1]))


print(reverse_number(-824243))


def my_decor(func):
    def wrapper(n):
        print("Start decor")
        func(n)
        print("End decor")
    return wrapper

@my_decor
def my_func(number):
    print(number ** 2)
my_func(10)


# -----------Передача аргументов-------------
def decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):  # аргументы прибывают отсюда
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)  # arg1 -> first_name | arg2 -> last_name
    return a_wrapper_accepting_arguments


# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции


@decorator_passing_arguments  # == decorator_passing_arguments = function_to_decorate(print_full_name)
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)


print_full_name(arg1="Питер", arg2="Питерсон")
# ------------------------


# -------Простейший декоратор---------
def my_decorator(decoration_func):  # 3
    def wrapper():  # 5
        print("Начало обертки")  # 6
        decoration_func()  # 7
        print("Конец обертки")  # 10
    return wrapper  # 4


def my_func():  # 8
    print("--Я в обертке--")  # 9


func = my_decorator(my_func)  # 1

func()  # 2
# -----------------------
print()


# -------Простейший декоратор с синтаксическим сахаром---------
def my_another_decorator(decoration_func):
    def wrapper():
        print("Начало еще одной обертки обертки")
        decoration_func()
        print("Конец еще одной обертки обертки")
    return wrapper


@my_another_decorator  # == func = my_another_decorator(my_function_for_decor)
def my_function_for_decor():
    print("--Я тоже буду в обертке--")


my_function_for_decor()
# -----------------------
print()


# -------Декоратор в декораторе---------
def first_decorator(decoration_func):
    def wrapper():
        print("Я первая, но буду снаружи")
        decoration_func()
        print("Я первая, но буду снаружи")
    return wrapper


def second_decorator(decoration_func):
    def wrapper():
        print("Я вторая, но буду в центре")
        decoration_func()
        print("Я вторая, но буду в центре")
    return wrapper


@first_decorator
@second_decorator
def my_function_for_double_decor():
    print("--Я буду в центре двух оберток--")


my_function_for_double_decor()
# -----------------------
print()


# -----------------------
def scream():
    print("ДА!")


def do_something_before(func):
    print("Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал")
    print(func())


do_something_before(scream)


# ------Мы можем хранить функции в переменных------
def hello_world_1():  # 3
    print("Hello world")  # 4


hello = hello_world_1  # 1
hello()  # Вызов функции через переменную  # 2
# ------------


# ------Определять функции внутри других функций------
def wrapper_hello_world():  # 3
    def hello_world():  # 5
        print("Hello world")  # 6
    hello_world()  # 4


wrapper_world = wrapper_hello_world  # 1
wrapper_world()  # 2
# ------------


# -----Передавать функции в качестве аргументов и возвращать их из других функций------
def higher_order(func):  # 2
    print(f'Получена функция {func} в качестве аргумента')  # 3
    func()  # 4
    return func  # 7


def hello_world():  # 5
    print("Hello world 2")  # 6


print(higher_order(hello_world))  # 1
# -----------


# -----------Вебинар по функция----------------
# ---------------декоратор------------

# Первый способ
# def my_decor(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
# def my_func():
#     print("тут основная функция")
#
# my = my_decor(my_func)
# my()


# Второй способ
def my_decor(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper


@my_decor
def my_func():
    print("тут основная функция")


my_func()
# -----------------------------
