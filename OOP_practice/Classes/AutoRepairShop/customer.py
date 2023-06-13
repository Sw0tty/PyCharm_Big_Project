class Customer:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

