import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width  # 10
        self.height = height  # 5

    def __eq__(self, other): # Определяет поведение оператора меньше, ==
        return self.width == other.width and self.height == other.height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area_r(self):
        return self.width * self.height


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_s(self):
        return self.a ** 2

    def __lt__(self, other):  # Определяет поведение оператора меньше, <
        return self.a < other.a

    def __gt__(self, other):  # Определяет поведение оператора меньше, >
        return self.a > other.a


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_c(self):
        return round(math.pi * self.r ** 2, 4)
