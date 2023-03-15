import random

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "abcdefghijklmnopqrstuvwxyz"
c = "0123456789"
d = "@#$%&<_*"
pass_list = []

pass_length = int(input("Задайте длинну пароля: "))
# while True:
#     pass_length = input("Задайте длинну пароля: ")
#     if pass_length == 1:
#         break
# pass_length = int(pass_length)
#
# print(type(pass_length))
special_symbols = input("Нужны ли в пароле спец. символы? Y/N ")

while special_symbols != "N" or special_symbols != "N":
    special_symbols = input("Нужны ли в пароле спец. символы? Y/N ")

if special_symbols == "Y":
    all = a + b + c + d
else:
    all = a + b + c

while pass_length != 0:
    pass_list.append(random.choice(all))
    pass_length -= 1
print(pass_list)

password = "".join(pass_list)
print(f"Ваш пароль: {password}")
