class Car:
    def __init__(self, dealer, model, year):
        self.__dealer = dealer
        self.__model = model
        self.__year = year

    def get_dealer(self):
        return self.__dealer

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def set_dealer(self, new_dealer):
        self.__dealer = new_dealer

    def set_model(self, new_model):
        self.__model = new_model

    def set_year(self, new_year):
        self.__year = new_year
