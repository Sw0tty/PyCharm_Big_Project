class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def set_name(self, new_name):
        self.__name = new_name

    def set_phone(self, new_phone):
        self.__phone = new_phone

    def set_email(self, new_email):
        self.__email = new_email

    def __str__(self):
        return f"Имя: {self.__name}\nТелефон: {self.__phone}\nЭл. почта: {self.__email}"
    