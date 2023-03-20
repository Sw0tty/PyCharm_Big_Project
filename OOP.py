import time
import random


class User:
    pass


peter = User()  # Создание экземляра класса User
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)


class User2:
    number_of_fingers = 5
    number_of_eyes = 2


lancelot = User2()
print(lancelot.number_of_eyes)
