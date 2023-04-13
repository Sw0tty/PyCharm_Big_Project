import os
from datetime import datetime
import time
from contextlib import contextmanager  # Привер менеджера через генераторы


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
