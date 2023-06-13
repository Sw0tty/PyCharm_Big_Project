class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def break_car(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


if __name__ == '__main__':
    my_car = Car(2014, 'Porshe')
    for i in range(5):
        my_car.accelerate()
        print(my_car.get_speed())
    for i in range(5):
        my_car.break_car()
        print(my_car.get_speed())
