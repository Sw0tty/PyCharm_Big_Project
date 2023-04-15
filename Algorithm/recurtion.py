def rec(i):
    if i <= 0:
        return i
    else:
        print(i)
        return rec(i - 1)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def sum_rec(lst):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[-1] + sum_rec(lst[:-1])


def str_rec(my_str):
    if len(my_str) == 1:
        return my_str[0]
    elif not my_str:
        return "Пустая строка"
    else:
        return my_str[-1] + str_rec(my_str[:-1])


if __name__ == '__main__':
    print(rec(5), '\n')
    print(factorial(3), '\n')
    print(sum_rec([1, 4, 6, 4]), "сумма")
    print(str_rec('shark'))
