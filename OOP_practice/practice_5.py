# class Progression:
#     def __init__(self, start, step):
#         self._start = start
#         self._step = step
#         self.cache = {}
#
#     @property
#     def start(self):
#         return self._start
#
#     @start.setter
#     def start(self, value):
#         self._start = value
#         self.cache.clear()
#
#     @property
#     def step(self):
#         return self._step
#
#     @step.setter
#     def step(self, value):
#         self._step = value
#         self.cache.clear()
#
#     def get_number(self, pos):
#         if pos in self.cache:
#             return self.cache[pos]
#         else:
#             number = self.start + self.step * pos
#             self.cache[pos] = number
#             return number
#
#
# my_num = Progression(0, 3)
#
# print(my_num.get_number(5))
# print(my_num.cache)
#
# my_num.start = 1000
# print(my_num.cache)
# print(my_num.get_number(5))
# print(my_num.cache)

# -----------------------

# G = {
#     1: {
#         2: 7,
#         3: 9,
#         6: 14
#         },
#     2: {
#         2: 7,
#         3: 10,
#         6: 14
#         },
#     3: {
#         1: 9,
#         2: 10,
#         6: 2
#         },
#     6: {
#         1: 14,
#         3: 2
#         }
#      }
#
#
# start = 2
# D = {i: 1000 for i in G.keys()}
# D[start] = 0
# U = {i: False for i in G.keys()}
#
# for _ in range(len(G.keys())):
#     candidate = [k for k in U.keys() if not U[k]]
#     min_k = min(candidate, key=lambda x: D[x])
#
#     for v, l in G[min_k].items():
#         if D[v] > D[min_k] + l:
#             D[v] = D[min_k] + l
#     U[min_k] = True
#
# print(D)

# ---------------
# __str__ __repr__ служат для того, чтобы преобразовывать класс к строке
# class A:
#     def __init__(self):
#         self.a = 1
#
#     def __str__(self):
#         return f"a = {self.a}"
#
#     def __repr__(self):
#         return "A()"
#
#
# a = A()
# print(str(a))
# print(repr(a))
# print(a)
# print([a, a])  # Вызовется repr, так как передан список
#
# c = "A()\nb=\n4"
# print(repr(c))

# -----------------

class A:
    def method(self):
        print("I'm A!")


class C:
    def method(self):
        print("I'm C!")


class B(A, C):
    def method(self):
        super().method()  # Работает перебором списка классов, который можно узнать через метод .mro()
        print("I'm B!")


# a = B()
# a.method()

print(B.mro())

# --------------------

