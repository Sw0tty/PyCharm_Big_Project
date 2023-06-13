from vehicles import *


def main():
    used_car = Car('Audi', 2007, 12500, 21500.0, 4)
    used_truck = Truck('Toyota', 2002, 40000, 12500.0, '4WD')
    used_suv = SUV('Volvo', 2000, 30000, 18500.0, 5)

    used_list = [used_car, used_truck, used_suv]
    print("==Авто в наличии==")
    for i in used_list:
        print(f"Тип авто: {type(i).__name__}")
        print(f"Марка: {i.get_make()}")
        print(f"Модкль: {i.get_model()}")
        print(f"Пробег: {i.get_mileage()}")
        print(f"Цена: {i.get_price()}")
        if type(i).__name__ == 'Car':
            print(f"Количество дверей: {i.get_doors()}")
        elif type(i).__name__ == 'Truck':
            print(f"Тип привода: {i.get_drive_type()}")
        elif type(i).__name__ == 'SUV':
            print(f"Мест для пассажиров: {i.get_pass_cap()}")
        print()


if __name__ == '__main__':
    main()
