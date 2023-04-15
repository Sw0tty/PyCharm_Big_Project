"""
Модуль рассчета площади круга и квадрата
"""
PI = 3.14


def circle_area(r: float) -> float:
    return pow(r, 2) * PI


def circle_length(r: float) -> float:
    return 2 * PI * r


def rectangle_area(a: float, b: float) -> float:
    return a * b


def rectangle_perimeter(a: float, b: float) -> float:
    return (a + b) * 2


def rec(n):
    if n == 0:
        return
    else:
        rec(n-1)
        print(n)


if __name__ == '__main__':  # проверяем работоспособность функции, дальнейшая часть не будет импортирована
    try:
        assert circle_area(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
        assert rectangle_area(5, 4) == 20
    except AssertionError:
        print("Предпологаемый результат не сходится с вычислением программы")

    rec(5)
