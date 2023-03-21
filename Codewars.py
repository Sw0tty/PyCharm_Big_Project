def mispelled(word1, word2):
    if abs(len(word1) - len(word2)) >= 2:
        return False
    else:
        word1 = list(sorted(word1))
        word2 = list(sorted(word2))
        first = word1
        second = word2
        if len(word1) > len(word2):
            first, second = word2, word1
        for i in first:
            if i in second:
                second.remove(i)
        if len(second) >= 2:
            return False
        else:
            return True


print(mispelled(word1="67qu", word2="67qu"))

# Функция перевода из двоичной системы в 10-чную. На вход принимает список чисел
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)  # Число 2 означает, что на вход будут приниматься лишь двочные числа


print(binary_array_to_number([1, 0, 1]))

# ----------------

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
