from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, type_wallet: str = "General"):
        self.balance: int = 0
        self.name: str = name
        self.type_wallet: str = type_wallet

    def get_balance(self) -> int:
        return self.balance

    def change_balance(self, value: int):
        if self.balance + value < 0:
            print(f"Not enough balance. You only have: {self.balance}")
        else:
            self.balance += value


class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)  # super() Вызывает метод родителя, который указан в наследовании

    def change_type_wallet(self):
        if self.balance < 100:  # Стоимость смены карты
            print(f"Not enough balance. You only have: {self.balance}")
        else:
            self.balance -= 100
            card = ProCard(self.name)
            card.balance = self.balance
            return card


class ProBalance:
    def change_balance(self, value: int):
        if self.balance + value * 0.95 < 0:
            print(f"Not enough balance. You only have: {self.balance}")
        else:
            self.balance += value * 0.95 if self.balance + value * 0.95 < self.balance else value


class ProCard(ProBalance, Wallet):
    def __init__(self, name, type_wallet="PRO"):
        super().__init__(name, type_wallet)

    def __str__(self):  # Меняет отображение ОБЪЕКТА
        return f"ggg {self.balance}"


class CreditCard(Wallet):
    def __init__(self, name, type_wallet="CREDIT", limit=-1000):
        self.limit = limit
        super().__init__(name, type_wallet)

    def change_balance(self, value: int):
        if self.balance + value < self.limit:
            print(f"Not enough balance. You only have: {self.balance - self.limit}")
        elif self.balance + value < 0 and self.balance > self.limit:
            self.balance += value
            print(f"Attention! You have crossed the value of your funds working loan. Your balance: {self.balance}")
        else:
            self.balance += value


card = ProCard("Sam")
print(card.type_wallet)
print(card.balance)
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-800)
print(card.get_balance())
card.change_balance(-300)
print(card.get_balance())
