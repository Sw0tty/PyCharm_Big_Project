from rectangle import Rectangle
from rectangle import Square
from rectangle import Circle

r1 = Rectangle(3, 4)  # Присваиваем переменной ширину и длинну для расчета
r2 = Rectangle(12, 5)
s1 = Square(5)
s2 = Square(10)
c1 = Circle(14)
c2 = Circle(3)

print(r1 == r2)
print(s1 > s2)
print(s1 < s2)
figures = [r1, r2, s1, s2, c1, c2]
print(type(figures))
for i in figures:
    if isinstance(i, Rectangle):
        print(i.get_area_r())
    elif isinstance(i, Square):
        print(i.get_area_s())
    else:
        print(i.get_area_c())
