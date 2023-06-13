# —------Генераторы--------—
D = {item: str(item**2) for item in range(1, 11) if item % 2 == 0}
L = [i for i in range(0, 10)]
M = [i for i in range(10, 0, -1)]
# zip(L, M) == [(0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]
N = [a * b for a, b in zip(L, M)]
print(D)
print(N)

L = [i for i in range(0, 10)]
print(any(L))

L = [int(input()) % 2 == 0 for i in range(5)]
print(L)

L = [input() for i in range(3)]
print(L)

multiplication_table = [[i * j for i in range(1, 11)] for j in range(1, 11)]
print(multiplication_table)
for i in multiplication_table:
    for j in i:
        print("%2d" % j, end=" ")
    print()

squares = [i**2 for i in range(1, 11)]
print(squares)

squares = [i**2 for i in range(1, 11) if i % 2 == 1]
print(squares)

list_tuples = [(i, i**2) for i in range(1, 11)]
print(list_tuples)

M = [[i+j for j in range(5)] for i in range(5)]
print(M)
# —--------------—
