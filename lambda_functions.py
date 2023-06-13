import random

print(list(map(lambda x: x**2, range(1, 11))))

my_list = [random.randrange(0, 100) for i in range(10)]
print(my_list)
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)
mapping_list = list(map(lambda x: str(x) + chr(random.randint(0, 100)), filtered_list))
print(mapping_list)

# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]
print(sorted(data, key=lambda x: x[0]/x[1]**2))
print(min(data, key=lambda x: x[0]/x[1]**2))

d = {2: "c", 1: "d", 4: "a", 3: "b"}

# Чтобы отсортировать его по ключам, нужно сделать так
print(dict(sorted(d.items())))

# А по значениям
print(dict(sorted(d.items(), key=lambda x: x[1])))

