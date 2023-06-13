# Классы и объекты
class Person:
    pass


tom = Person()

# Методы классов
class Person2:
    def say_hello(self):  # self указывает на . Можно заменить как Person2
        return "Hello"

    def print_message(self, message):  # self указывает на . Можно заменить как Person2
        return message


bob = Person2()
print(bob.print_message("Hello"))

# self
# self.атрибут
# self.метод

class Per:
    def say(self, message):
        print(message)

    def say_hello(self):
        self.say("hello")

kriss = Per()
kriss.say_hello()


# конструкторы
# __init__()
class MainPerson:
    def __init__(self):
        print("Создание объекта MainPerson")

    def say_hello(self):
        print("hello")


kriss = MainPerson()
kriss.say_hello()

# атрибуты объекта
# атрибуты хранят состояние объета

class Trip:
    def __init__(self, name):
        self.name = name
        self.age = 19

    def display_info(self):
        print(f"name: {self.name}, age: {self.age}")
vova = Trip('Vova')
vova.display_info()

print(vova.age, vova.name)

vova.age = 37
print(vova.age)

# инкапсуляция
class Person3:
    def __init__(self, name):
        self.__name = name
        self.__age = 14

    def set_age(self, age):
        if 1 < age < 100:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name
    def display_info(self):
        print(f"name: {self.__name}\t age: {self.__age}")

roma = Person3("Roma")
roma.display_info()
roma.display_info()
roma.set_age(-313)
roma.set_age(33)
roma.display_info()

# Наследование
class Geom:
    name = "Geom"

    def set_cords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Рисование примитива")

class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")

g = Geom()
g.set_cords(0, 0, 0, 0)
l = Geom()
r = Rect()
l.set_cords(1, 1, 2, 2)
r.set_cords(1, 3, 3, 2)
print(r.__dict__)
print(l.__dict__)

# Полиморфизм
class Parrot:
    def fly(self):
        print("Попугай умеет летать")

    def swim(self):
        print("Попугай не умеет плавать")

class Penguin:
    def fly(self):
        print("Пингвин не умеет летать")

    def swim(self):
        print("Пингвин умеет плавать")

def flying_test(bird):
    bird.fly()

kesha = Parrot()
peggy = Penguin()

flying_test(kesha)
flying_test(peggy)
