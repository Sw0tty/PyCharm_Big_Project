import datetime


class Animal:
    def __init__(self, color: str) -> None:  # color: str - всего лишь подсказка для нужного типа данных
        self.color: str = color

    def roar(self):
        return "ARARAR"

    def roar_test(self):  # Тест полиморфизма
        return "I'm Animal"

    def roar_test_2(self, type_=None):  # Тест полиморфизма методом перегрузки
        if type_:
            return "It's just another!"
        return "I'm Animal"


class Cats(Animal):
    def meow(self):
        return "Meow"

    def roar_test(self):  # Тест полиморфизма
        return "I'm Cats"


a = Animal("red")
b = Cats("red")

print(a.color)
print(a.roar())

print(b.color)
print(b.roar())
print(b.meow())
print(a.roar_test())
print(b.roar_test())
print(a.roar_test_2(type_="Car"))  # Тест полиморфизма методом перегрузки
print("\n")
p = [1, 2, 3, 4]
print(p.index(3))

class ParentClass:

    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


ParentClass.method(555)
ParentClass.call_original_method()

ChildClass.method(0)
ChildClass.call_original_method()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property  # тот самый магический декоратор
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле — шкала счастья
    @property
    def happiness(self):
        return self.dog_happiness

    @happiness.setter
    # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
    def happiness(self, dog_happiness):
        if dog_happiness <= 100 and dog_happiness >= 0:
            self.dog_happiness = dog_happiness
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.dog_happiness = 50
print(jane.name, jane.age)
print(jane.human_age)
print(jane.happiness)


class Squre:
    def __init__(self, side):
        self.side = side


class SquareFactory:
    @staticmethod
    def side(side):
        return Squre(side)


squre_side = SquareFactory.side(5)
print(squre_side.side)


class StaticClass:
    @staticmethod  # помечаем метод, который мы хотим сделать статичным декоратором @staticmethod
    def bar():
        print("bar")


StaticClass.bar()




class Lime:
    def __init__(self, lem):
        self.lem = lem

    def add_lem(self):
        if self.lem:
            return "Чай с лемоном"
        else:
            return "Чай без лемона"


tea = Lime("")
print(tea.add_lem())


# ----------Наследование класса-----------
class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


class Food(Product):  # Дочерний класс, в который передается родительский класс - Product
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(isinstance(eggs, Food))  # Проверка принадежности
print(eggs.max_quantity)  # Запрос переменной из родительского класса
print(eggs.is_available())  # Запрос метода из родительского класса
print(eggs.is_critical)  # Запрос значения из дочернего класса
# ---------------------
print()


# --------Использование get_ и set_ (геттеры, сеттер)-------------
class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age, int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age  # Записываем новое значение
        else:
            print("Значение неверно, возвращаю старое значение")


h = Human()
print(f"Старое значние: {h.get_age()}")
h.set_age(12)  # Задаем новое значение через setter
print(f"Новое значние: {h.get_age()}")  # Запрашиваем значение у getter
# ---------------------------------------

# ---------------------
events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):  # Задание значения по умолчанию
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):  # Метод выборки из словаря по ключу
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")


for i in events:
    event_obj = Event()
    event_obj.init_from_dict(i)
    print(event_obj.timestamp)
# -----------------------
print()


# -----------------------
class Event2:
    def __init__(self, timestamp, event_type, session_id):  # Задание значения по умолчанию
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id


for event in events:
    event_obj = Event2(timestamp=event.get("timestamp"), event_type=event.get("type"), session_id=event.get("session_id"))
    print(event_obj.type)
# ----------------


# -----------------------
class Product1:
    def __init__(self, name, category, quantity_in_stock):  # Метод
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):  # Тоже метод
        return True if self.quantity_in_stock > 0 else False  # Проверка, есть ли в наличии

    def add_product(self):
        return self.quantity_in_stock + 10


eggs = Product1("eggs", "food", 5)
print(eggs.is_available())  # Проверяем наличие
print(eggs.name.capitalize(), eggs.add_product())  # Выводит название продукта (с заглавной, .title()) и добавляет 10 к уже тому что есть
# ------------------

print()


# --------"Магический" метод __init__----------
class UserInit:
    def __init__(self, name, email, sex):
        self.name = name
        self.email = email
        self.sex = sex


peter = UserInit(name="Peter Robertson", email="peterrobertson@mail.com", sex="male")  # Более наглядный вид
julia = UserInit("Julia Donaldson", "juliadonaldson@mail.com", "female")  # Тоже самое, но без конкретики, что к чему относится
# chris = UserInit()

# print(chris.name)
print(peter.name)
print(julia.email)

# ------------------
print()


# ------------------
class User:
    pass


peter = User()  # Создание экземляра класса User
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)


class User2:
    number_of_fingers = 5
    number_of_eyes = 2


lancelot = User2()
print(lancelot.number_of_eyes)
