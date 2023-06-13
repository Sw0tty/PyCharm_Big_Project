def rec_sum(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num + rec_sum(num - 1)


def rec_rev_str(str_: str) -> str:
    if len(str_) == 1:
        return str_
    else:
        return str_[-1] + rec_rev_str(str_[:-1])


def rec_factorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * rec_factorial(num - 1)


def rec_list_sum(numbers_list: list, start: int, end: int) -> int:
    if start > end:
        return 0
    else:
        return numbers_list[start] + rec_list_sum(numbers_list, start + 1, end)


def rec_fib(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return rec_fib(num - 1) + rec_fib(num - 2)


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)


if __name__ == '__main__':
    print(rec_sum(3))
    print(rec_rev_str('Start'))
    print(rec_factorial(5))
    print(rec_list_sum([1, 2, 3, 4, 5, 6, 7], 0, 3))
    print(rec_fib(10))
    print(gcd(15, 31))
