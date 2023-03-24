import datetime


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
