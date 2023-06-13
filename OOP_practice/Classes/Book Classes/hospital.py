class Patient:
    def __init__(self, name, address, phone_number, guarantor, guarantor_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__guarantor = guarantor
        self.__guarantor_number = guarantor_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def get_guarantor(self):
        return self.__guarantor

    def get_guarantor_number(self):
        return self.__guarantor_number

    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def set_guarantor(self, new_guarantor):
        self.__guarantor = new_guarantor

    def set_guarantor_number(self, new_guarantor_number):
        self.__guarantor_number = new_guarantor_number


class Procedure:
    def __init__(self, name, date, doctor_name, cost):
        self.__name = name
        self.__date = date
        self.__doctor_name = doctor_name
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_doctor_name(self):
        return self.__doctor_name

    def get_cost(self):
        return self.__cost

    def set_name(self, new_name):
        self.__name = new_name

    def set_date(self, new_date):
        self.__date = new_date

    def set_doctor_name(self, new_doctor_name):
        self.__doctor_name = new_doctor_name

    def set_cost(self, new_cost):
        self.__cost = new_cost
