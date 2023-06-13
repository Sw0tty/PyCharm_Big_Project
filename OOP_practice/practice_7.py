class Human:

    # Statics fields
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 1000
        self.__house = None

    @staticmethod
    def default_info():
        return f"Значения класса по умолчанию:\nИмя: {Human.default_name}\nВозраст: {Human.default_age}"

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def info(self):
        return f"Значения класса:\n\tИмя: {self.name}\n\tВозраст: {self.age}\n\tДеньги: ${self.__money}\n\t" \
               f"Личный дом: {self.__house if self.__house is not None else 'Нету'}"

    def earn_money(self, cash):
        self.__money += cash
        return f"Пополнение счета на ${cash}. Текущий баланс ${self.__money}"

    def buy_house(self, house, discount=0):
        if house.final_price(discount) > self.__money:
            return "У вас недостаточно средств!"
        else:
            self.__make_deal(house, house.final_price(discount))
            return "Дом успешно приобретен"


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        if discount == 0:
            return self._price
        return self._price - ((self._price * discount) / 100)


class SmallHouse(House):

    default_area = '40м2'

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':
    print(Human.default_info())
    me = Human('Kirill', 23)
    print(me.info())
    house = SmallHouse(3500)
    print(me.buy_house(house, 20))
    print(me.earn_money(2000))
    print(me.buy_house(house, 20))
    print(me.info())
