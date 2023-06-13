class Tomato:

    states = {1: 'Даже не зацвел', 2: 'Цветение', 3: 'Зеленый', 4: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._states = self.states[index]

    def grow(self):
        for i, j in self.states.items():
            if j == self._states and self._states != self.states[4]:
                self._states = self.states[i + 1]
                return f"Помидор теперь в стадии {self._states}"

            elif j == self._states and self._states == self.states[4]:
                return "Данный помидор уже созрел!"

    def is_ripe(self):
        if self._states == self.states[4]:
            return "Пора срывать."
        return f"Пока что рано. Стадия: {self._states}"


class TomatoBush:

    def __init__(self, value):
        self.tomatoes = [Tomato(int(input("Введите стадию созревания 1-4"))) for i in range(value)]

    def grow_all(self):
        for i in self.tomatoes:
            print(i.grow())

    def all_are_ripe(self):
        count = 0
        for i in self.tomatoes:
            if i.is_ripe() == 'Пора срывать.':
                count += 1
        if count == len(self.tomatoes):
            return True
        return False

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name):
        self.name = name
        self._plant = bush.tomatoes

    def work(self):
        for i in self._plant:
            i.grow()

    def harvest(self):
        if TomatoBush.all_are_ripe(bush):
            TomatoBush.give_away_all(bush)
            return "Урожай собран, до следующего сезона"
        return "Еще не все созрели"

    @staticmethod
    def knowledge_base():
        return 'Пока не все помидоры не созреют, нужно ухаживать'


print(Gardener.knowledge_base())
bush = TomatoBush(4)
gardener = Gardener('Peter')
bush.grow_all()
bush.all_are_ripe()
gardener.work()
print(gardener.harvest())


class Soda:
    def __init__(self, s_with=''):
        if isinstance(s_with, str):
            self.__s_with = s_with
        else:
            self.__s_with = None

    def show_my_drink(self):
        if self.__s_with:
            return f"Газировка с {self.__s_with}"
        return "Обычная газировка"


soda = Soda()
print(soda.show_my_drink())


class TriangleChecker:

    __slots__ = ['a', 'b', 'c']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not isinstance(self.a, int) or not isinstance(self.b, int) or not isinstance(self.c, int):
            return "Нужно вводить только числа!"
        elif self.a == 0 or self.b == 0 or self.c == 0:
            return "У треугольника должно быть ровно три строны!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        return "Ура! Из этого получится прекрасный треугольник!"


triangle = TriangleChecker(1, 123, 3)
print(triangle.is_triangle())


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return round(self.__kg * 2.205, 4)

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


weight = KgToPounds(12)
print(weight.to_pounds())
weight.kg = 22
print(weight.kg)
print(weight.to_pounds())


class RealString:
    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)

        return len(self.some_str) == len(other.some_str)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)

        return len(self.some_str) < len(other.some_str)

    def __le__(self, other):
        return self == other or self < other


real_str = RealString('Яблоко')
real_str2 = RealString('Apple')
print(real_str == real_str2)


class Kirill:

    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name.lower().title() == 'Kirill':
            self.name = 'Kirill'
        else:
            self.name = f"I'm not a {name}, I'm Kirill!"
        self.age = age


my_class = Kirill('Bob', 23)


class Cez:

    def __init__(self, word):
        self.word = word

    def code_word(self, step):
        new_word = ''
        for i in self.word:
            if ord(i) + step > 122:
                new_word += chr(96 + ((ord(i)+step) - 122))
            # elif ord(i) - step < 97:
            #     new_word += chr(121 - ((ord(i)-step) - 97))
            else:
                new_word += chr(ord(i) + step)
        return new_word


for_cez = Cez('apple')
print(for_cez.code_word(11))
print(ord('a'))
print(ord('z'))
