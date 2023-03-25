from pet import Cat
from pet import Dog
from pet import Client

pet1 = Cat(name="Барон", sex="мальчик", age=2)
pet2 = Cat(name="Гоша", sex="мальчик", age=1)
pet3 = Cat(name="Мухтар", sex="мальчик", age=1)
pet4 = Cat(name="Сэм", sex="мальчик", age=3)
pet_test = Dog(name="Барон", sex="мальчик", age=2)
client1 = Client("Иван", "Петров", "Москва", 30)
client2 = Client("Василий", "Старков", "Санкт-Петербург", 25)
client3 = Client("Петр", "Иванов", "Москва", 30)
client4 = Client("Артур", "Орлов", "Подольск", 110)
client5 = Client("Станислав", "Слутский", "Москва", 450)

all_shop_clients = [client1, client2, client3, client4, client5]

print(pet_test.get_pet())
print(f"Кличка: {pet1.name} \nПол: {pet1.sex} \nВозраст: {pet1.age}", end="\n\n")
print(f"Кличка: {pet2.name} \nПол: {pet2.sex} \nВозраст: {pet2.age}", end="\n\n")
print(f"Кличка: {pet3.name} \nПол: {pet3.sex} \nВозраст: {pet3.age}", end="\n\n")
print(f"Кличка: {pet4.name} \nПол: {pet4.sex} \nВозраст: {pet4.age}", end="\n\n")
print(client1)
print()

for i in all_shop_clients:
    print(i.shop_client())
