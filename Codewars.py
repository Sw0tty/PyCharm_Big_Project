
name = 'Barack hussein obama'
name_res = ""
count = 0
for i in name:
    if i == name[0] or count == 1:
        name_res += i.upper()
        count = 0
    elif i == " ":
        name_res += "."
        count += 1
print(name_res)

# def twoSum(nums, target):
#     index_list = []
#     sum_ = 0
#     for i in nums:
#         sum_ += i
#         for j in nums[1:]:
#             sum_ += j
#             print(sum_)
#             if sum_ == target:
#                 index_list.append(nums.index(i))
#                 index_list.append(nums.index(j))
#                 return index_list
#             print(index_list)
#         sum_ = 0
#
#
#
# print(twoSum(nums=[3, 3], target=6))


# def move_zeros(lst):
#     count = 0
#     for i in lst:
#         if i == 0:
#             count += 1
#     while count:
#         lst.remove(0)
#         lst.append(0)
#         count -= 1
#     return lst
#
#
# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
#
# # def move_zeros(a):
# #     a.sort(key=lambda v: v == 0)
# #     return a
#
#
# def speed_limit(speed, signals):
#     fine = 0
#     for i in signals:
#         print(speed, i)
#         if speed > i:
#             if 10 <= abs(i - speed) <= 19:
#                 fine += 100
#             elif 20 <= abs(i - speed) <= 29:
#                 fine += 250
#             elif abs(i - speed) >= 30:
#                 fine += 500
#         print(fine)
#     return fine
#
# print(speed_limit(speed=130, signals=[140, 130, 100]))
# print()
# def mispelled(word1, word2):
#     if abs(len(word1) - len(word2)) >= 2:
#         return False
#     else:
#         word1 = list(sorted(word1))
#         word2 = list(sorted(word2))
#         first = word1
#         second = word2
#         if len(word1) > len(word2):
#             first, second = word2, word1
#         for i in first:
#             if i in second:
#                 second.remove(i)
#         if len(second) >= 2:
#             return False
#         else:
#             return True
#
#
# print(mispelled(word1="67qu", word2="67qu"))
#
# # Функция перевода из двоичной системы в 10-чную. На вход принимает список чисел
# def binary_array_to_number(arr):
#     return int("".join(map(str, arr)), 2)  # Число 2 означает, что на вход будут приниматься лишь двочные числа
#
#
# print(binary_array_to_number([1, 0, 1]))
#
# # ----------------
#
# def add_binary(a=2,b=2):
#     return (f"""{a} + {b} = {a + b} in decimal or {format(a + b, "b")} in bianry""")
# print(add_binary())
#
#
# # Необходимо отсортировать число от большего к меньшему
# def descending_order(num):
#     return int("".join(sorted(str(num), reverse=True)))
#
#
# print(descending_order(num=123))
#
#
# # Функция, проверяющая слово на повторение одинаковых символом
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
