# Инкапсуляцию, без @property
class Test:
    a = "a"  # public
    _b = "_b"  # protected
    __c = "__c"  # private

    def get_a(self):
        return self.a

    def get_b(self):
        return self._b

    def get_c(self):
        return self.__c

    def set_c(self, value):
        try:
            if isinstance(value, str):
                self.__c = value
                print('Done')
            else:
                raise ValueError(f"Значение -> {value} , не явялется строкой")
        except ValueError as err:
            print(err)


t = Test()
print(t.a, t._b, t.get_c())
print(t.get_c())
t.set_c("3")
print(t.get_c(), '\n')


# Тоже самое, но с @property
class Test2:
    a = "a"  # public
    _b = "_b"  # protected
    __c = "__c"  # private

    def get_a(self):
        return self.a

    def get_b(self):
        return self._b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        try:
            if isinstance(value, str):
                self.__c = value
                print('Done')
            else:
                raise ValueError(f"Значение -> {value} , не явялется строкой")
        except ValueError as err:
            print(err)


t = Test2()
print("with setter, property", t.a, t._b, t.c)
print(t.c)
t.c = "fgh"
print(t.c)
# ------------------


# ----Полиморфизм-----
class Payment:
    _balance = 100

    def pay(self, price):
        pass


class Card(Payment):
    def pay(self, price):
        self._balance -= price
        return f"Оплата картой. Баланс: {self._balance}"


class Cash(Payment):
    def pay(self, price):
        change = self._balance - price
        self._balance = change
        return f"Оплата наличными. Сдача: {self._balance}"


p1 = Card()
print(p1.pay(30))
p2 = Cash()
print(p2.pay(50))
# -------------------------
# Сортировка вставками
array = [2, 4, 3, 9, 6, 8]

for i in range(1, len(array)):
    a = array[i]
    ind = i
    while ind > 0 and array[ind - 1] > a:
        array[ind] = array[ind - 1]
        ind -= 1
    array[ind] = a

print(array)
