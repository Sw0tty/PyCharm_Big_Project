import os
import string
import math
import time


print(f"Мы в директории: {os.getcwd()}")  # получить текущую директорию
print(f"В ней такие файлы: {os.listdir()}")  # получить список файлов текущей директории
print(dir(math))

print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))

named_tuple = time.localtime()  # получить struct_time
time_string = time.strftime("%H:%M:%S", named_tuple)
date_string = time.strftime("%d-%m-%Y", named_tuple)
minutes_string = time.strftime("%M", named_tuple)
month_string = time.strftime("%m", named_tuple)

print(time_string)
print(date_string)
print(minutes_string)
print(month_string)
