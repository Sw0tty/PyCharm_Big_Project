class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


class Dog(Cat):
    def get_pet(self):
        return f"{self.name} {self.age}"


class Client:
    def __init__(self, name, last_name, city, money):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.money = money

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.city}. Баланс: {self.money} руб."

    def shop_client(self):
        return f"{self.name} {self.last_name}. {self.city}."


