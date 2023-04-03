"""
Модуль рассчета площади круга и квадрата
"""
PI = 3.14


def circle_area(r: float) -> float:
    return pow(r, 2) * PI


def rectangle_area(a: float, b: float) -> float:
    return a * b


if __name__ == '__main__':  # проверяем работоспособность функции, дальнейшая часть не будет импортирована
    assert circle_area(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
    assert rectangle_area(5, 4) == 20
