class WarehouseItem:
    def __init__(self, name, value, price, manufacture, expiration_date):
        self.__name = name
        self.__value = value
        self.__price = price
        self.__manufacture = manufacture
        self.__expiration_date = expiration_date

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_price(self):
        return self.__price

    def get_manufacture(self):
        return self.__manufacture

    def get_expiration_date(self):
        return self.__expiration_date

    def set_name(self, new_name):
        self.__name = new_name

    def set_value(self, new_value):
        self.__value = new_value

    def set_price(self, new_price):
        self.__price = new_price

    def set_manufacture(self, new_manufacture):
        self.__manufacture = new_manufacture

    def set_expiration_date(self, new_expiration_date):
        self.__expiration_date = new_expiration_date

    def __str__(self):
        return f"Наименование: {self.__name}\nКоличество: {self.__value}\nЦена: {self.__price}" \
               f"\nДата производства: {self.__manufacture}\nСрок хранения: {self.__expiration_date}"
