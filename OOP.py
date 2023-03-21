import time
import random


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

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

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)
# ----------------



class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False  # Проверка, есть ли в наличии


eggs = Product("eggs", "food", 5)
print(eggs.is_available())  # Проверяем наличие
# ------------------



# ------------------
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
