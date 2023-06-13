import os
from datetime import datetime
import time
from contextlib import contextmanager  # Привер менеджера через генераторы
import pickle
import random

def read_last(lines):
    with open(os.path.join(os.getcwd(), 'files_dir', 'article.txt'), 'r', encoding='utf8') as file:
        largest_word = [i.strip() for i in file.readlines()]
        for i in largest_word[-lines:]:
            print(i)

read_last(3)

with open(os.path.join(os.getcwd(), 'files_dir', 'article.txt'), 'r', encoding='utf8') as file:
    largest_word = []
    for i in file.read().split():
        if not largest_word:
            largest_word.append(i)
        elif len(i) > len(largest_word[-1]):
            largest_word.clear()
            largest_word.append(i)
        elif len(i) == len(largest_word[-1]):
            largest_word.append(i)
    print(largest_word)



with open(os.path.join(os.getcwd(), 'files_dir', 'sowpods.txt'), 'r') as file:
    random_word = random.choice(file.readlines())
    for_check = [[i, True] for i in random_word.strip()]
    print(random_word)


# def gallows():
#
#      r" O "
#      r"/|\"
#      r"/ \"
#     print("-" * 14)
#     for i in range(5):
#         print("|", " " * 10, "|")
#     print("-" * 14)
# print(gallows())

def print_word():
    for i, j in for_check:
        if j is True:
            print('_', end='')
        else:
            print(i, end='')
    print()


def checker(for_check, letter, count):
    for i, j in enumerate(for_check):
        if j[0] == letter.upper() and j[1] is True:
            for_check[i][1] = False
            count -= 1
    return count


print("""Добро пожаловать в 'Висельницу'""")
print(f"В загаданном слове {len(random_word)} букв")
count = len(random_word) - 1
while True:
    print_word()
    letter = input("Ваша буква: ")
    if letter.upper() in random_word:
        print("Да, такая буква есть")
        count = checker(for_check, letter, count)
        if count == 0:
            print("Поздравляю, вы разгадали загаданное слово!")
            break
    else:
        print("Такой буквы в слове нет")


D = {item: str(item**2) for item in range(1, 10)}
D2 = {'555-1111': 'Кэти', '555-2222': 'Крис'}
# with open(os.path.join(os.getcwd(), 'files_dir', 'pickle_objects.txt'), 'ab') as file:
#     pickle.dump(D2, file)

with open(os.path.join(os.getcwd(), 'files_dir', 'pickle_objects.txt'), 'rb') as file:
    while True:
        try:
            print(pickle.load(file))
        except EOFError:
            break
    print('Конец файла')
# print(loaded_d, loaded_d2, sep='\n')
# with open(os.path.join(os.getcwd(), 'files_dir', 'control_work.txt'), 'r', encoding='utf8') as file:
#     in_file = file.readlines()  # На вход получаем строку, в которой есть символ '\n'
#     for i in in_file:
#         in_file[in_file.index(i)] = i.rstrip('\n')  # Удаляем его и перезаписываем список
#     for i in in_file:
#         print(i)

l1 = ['Контратаковать', 'Подпоясать', 'Соединить', 'Сюсюкаться', 'Тужить']
l2 = [i for i in range(1, 11)]
print('test_dir' in os.listdir(os.path.join(os.getcwd(), 'files_dir')))
path_to = os.path.join(os.getcwd(), 'files_dir')
try:
    pass
    # with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'numbers.txt'), 'r', encoding='utf8') as file:
    #     old_data = file.read()
    #     print(type(old_data))
    #     for i in old_data:
    #         if i.rstrip() == '2':
    #             old_data = old_data.replace(i, '333')
    #             break
    #     with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'numbers.txt'), 'w', encoding='utf8') as file:
    #         file.write(old_data)
    # with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'employees.txt'), 'a', encoding='utf8') as file:
    #     while True:
    #         emp_name = input("Введите имя сотрудника: ")
    #         emp_id = input("Введите id сотрудника: ")
    #         emp_dept = input("Введите отдел сотрудника: ")
    #         file.write(f"{emp_name}|{emp_id}|{emp_dept}\n")
    #         print("Данные записаны.")
    #         answer = input("Добавить еще сотрудника? Y - да")
    #         if answer == 'Y':
    #             continue
    #         else:
    #             break
    # with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'employees.txt'), 'r', encoding='utf8') as file:
    #     emp_list = []
    #     for i in file:
    #         emp_name, emp_id, emp_dept = i.rstrip('\n').split('|')
    #         emp_list.append((emp_name, int(emp_id), emp_dept))
    #     print(emp_list)
    # with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'for_testing.txt'), 'w', encoding='utf8') as file:
    #     for i in l1:
    #         file.write(f"{i}\n")
    # with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'numbers.txt'), 'a', encoding='utf8') as file:
    #     for i in l2:
    #         file.write(f"{i}\n")
    # with open(os.path.join(os.getcwd(), 'files_dir', 'test_dir', 'numbers.txt'), 'r', encoding='utf8') as file:
    #     numbers_from_file = []
    #     while True:
    #         line = file.readline()
    #         if line:
    #             numbers_from_file.append(int(line))
    #         else:
    #             break
    #     print(numbers_from_file)
        # for i in file:
        #     print(int(i), "GG")
except FileNotFoundError:
    new_dir = 'test_dir'
    os.mkdir(os.path.join(path_to, new_dir))


# class OpenFile:
#     def __init__(self, a, b):
#         self.file = open(a, b, encoding='utf8')
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with OpenFile(os.path.join(os.getcwd(), 'files_dir', 'control_work.txt'), 'r') as f:
#     for i in f.readlines():
#         print(i, end="")

# ---Менеджер через класс---
# class Timer:
#     def __init__(self):
#         pass
#
#     def __enter__(self):  # Метод срабатывающий при входе в менеджер
#         self.start = datetime.utcnow()  # Получает точное время и дату системы
#         # return <объект> 1 если нужно вернуть что-либо
#
#     def __exit__(self, exc_type, exc_val, exc_tb):  # Метод срабатывающий на выходе из менеджера
#         # Подсчитаем количество времени от начала, до закрытия менеджера и переведем это время в секунды
#         print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")
#
#
# with Timer():  # 1 И сюда as <объект>
#     time.sleep(5)
# ------

# @contextmanager
# def timer():
#     start = datetime.utcnow()
#     yield  # 1 Если нужно что-либо вернуть, необходимо вставить сюда код
#     print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")
#
#
# with timer():  # 1 И сюда as <объект>
#     time.sleep(2)

# -----
# print(f"Мы в директории: {os.getcwd()}")  # получить текущую директорию
# print(f"В ней такие файлы: {os.listdir()}")  # получить список файлов текущей директории
#
# print(os.path.join(os.getcwd(), 'Modules_Practice'))
#
# # Проверка файла в списке, который берется из директории ниже
# if 'pet.py' in os.listdir(os.path.join(os.getcwd(), 'practice_C1')):
#     print("pet.py на месте")
#
# if 'Tasks.py' not in os.listdir():  # Проверка файла в списке, который берется в текущей директории
#     print("Файл отсутствует в данной директории")
# else:
#     print("Он тут")
# -----

# Запись в файл
# my_test_file = open(os.path.join(os.getcwd(), 'files_dir/test.txt'), 'w', encoding='utf8')  # Запись
# my_test_file.write("This is a test string\n")
# my_test_file.write("This is a new string\n")
# my_test_file.write("А это на русском языке\n")

# my_test_file.write(input("Что записать?"))

# my_test_file = open(os.path.join(os.getcwd(), 'files_dir/test.txt'), 'a', encoding='utf8')  # Дозапись
# sequence = ["other string\n", "123\n", "test test\n"]
# my_test_file.writelines(sequence)

# my_test_file.close()

# Чтение из файла
# my_test_file = open(os.path.join(os.getcwd(), 'files_dir', 'test.txt'), 'r', encoding='utf8')

# print(my_test_file.read(4))  # Читает от начала и до указанного символа
# print(my_test_file.read())  # Если перед такой строкой есть строка с указанием символа, то прочитает от него и до конца

# print(my_test_file.readlines())
# print(my_test_file.readline())
# print(my_test_file.read(30))
# print(my_test_file.readline())

# for i in my_test_file:
#     # print(i.strip())  # Пропускает символы переноса
#     print(i, end='')
#
# my_test_file.close()

# with open(os.path.join(os.getcwd(), 'files_dir', 'input.txt'), 'r', encoding='utf8') as input_file:
#     with open(os.path.join(os.getcwd(), 'files_dir', 'output.txt'), 'w', encoding='utf8') as output_file:
#         for i in input_file:
#             output_file.write(i)

# with open(os.path.join(os.getcwd(), 'files_dir', 'numbers.txt'), 'r', encoding='utf8') as numbers_file:
#     with open(os.path.join(os.getcwd(), 'files_dir', 'output.txt'), 'a', encoding='utf8') as output_file:
#         min_num = numbers_file.readline()
#         numbers_file.seek(numbers_file.tell() - numbers_file.tell())
#         max_num = numbers_file.readline()
#         for i in numbers_file:
#             if int(i) < int(min_num):
#                 min_num = i
#             if int(i) > int(max_num):
#                 max_num = i
#         result = int(max_num) + int(min_num)
#         output_file.write("\n" + str(result))

# with open(os.path.join(os.getcwd(), 'files_dir', 'control_work.txt'), 'r', encoding='utf8') as control_work_file:
#     for i in control_work_file:
#         point = int(i.split()[-1])
#         if point < 3:
#             print(i[:-2])

# with open(os.path.join(os.getcwd(), 'files_dir', 'control_work.txt'), 'r', encoding='utf8') as control_work_file:
#     for i in reversed(control_work_file.readlines()):
#         print(i)
