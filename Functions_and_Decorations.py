import random
import time


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
