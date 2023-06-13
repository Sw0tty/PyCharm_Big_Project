class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_animal_type):
        self.__animal_type = new_animal_type

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    name = input("Введите кличку вашего питомца: ")
    animal_type = input("Что у вас за питомец: ")
    age = input("Сколько ему лет: ")
    my_pet = Pet(name, animal_type, age)
    print(f"Имя питомца: {my_pet.get_name()}\nТип питомца: {my_pet.get_animal_type()}\nВозраст: {my_pet.get_age()}")
