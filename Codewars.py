def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


def add_binary(a=2,b=2):
    return (f"""{a} + {b} = {a + b} in decimal or {format(a + b, "b")} in bianry""")
print(add_binary())


# Необходимо отсортировать число от большего к меньшему
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(num=123))


# Функция, проверяющая слово на повторение одинаковых символом
def is_isogram(string):
    return len(string) == len(set(string.lower()))