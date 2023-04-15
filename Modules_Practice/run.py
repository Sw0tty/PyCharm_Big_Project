from functions import circle_area, rectangle_area, rectangle_perimeter, circle_length

r = float(input("Введите радиус круга: "))
a = float(input("Введите первую сторону прямоугольника: "))
b = float(input("Введите вторую сторону прямоугольника: "))

print(f"Площадь круга {circle_area(r):.4f}, длина окружности {circle_length(r):.4f},"
      f"площадь прямоугольника {rectangle_area(a, b):.4f}, периметр прямоугольника {rectangle_perimeter(a, b):.4f}")

if circle_area(r) > rectangle_area(a, b):
    print("Площадь круга больше площади квадрата")
else:
    print("Площадь квадрата больше площади круга")
