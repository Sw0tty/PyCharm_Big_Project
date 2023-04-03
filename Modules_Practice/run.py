from functions import circle_area, rectangle_area

r = float(input("Введите радиус круга: "))
a = float(input("Введите первую сторону прямоугольника: "))
b = float(input("Введите вторую сторону прямоугольника: "))

print(f"Площадь круга {circle_area(r)}, а площадь квадрата {rectangle_area(a, b)}")

if circle_area(r) > rectangle_area(a, b):
    print("Площадь круга больше площади квадрата")
else:
    print("Площадь квадрата больше площади круга")
