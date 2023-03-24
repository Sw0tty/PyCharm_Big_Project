from pet import Cat
from pet import Dog

pet1 = Cat(name="Барон", sex="мальчик", age=2)
pet2 = Cat(name="Гоша", sex="мальчик", age=1)
pet3 = Cat(name="Мухтар", sex="мальчик", age=1)
pet4 = Cat(name="Сэм", sex="мальчик", age=3)
pet_test = Dog(name="Барон", sex="мальчик", age=2)

print(pet_test.get_pet())
print(f"Кличка: {pet1.name} \nПол: {pet1.sex} \nВозраст: {pet1.age}", end="\n\n")
print(f"Кличка: {pet2.name} \nПол: {pet2.sex} \nВозраст: {pet2.age}", end="\n\n")
print(f"Кличка: {pet3.name} \nПол: {pet3.sex} \nВозраст: {pet3.age}", end="\n\n")
print(f"Кличка: {pet4.name} \nПол: {pet4.sex} \nВозраст: {pet4.age}", end="\n\n")
