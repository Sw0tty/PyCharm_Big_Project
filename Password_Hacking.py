a = "abcdefghijklmnopqrstuvwxyz"
b = "maf"
maybe_pass = []

# def c3():
#     for k in a:
#         print(k)
#     print()
#
# def c2():
#     for j in a:
#         print(j)
#     print()
#
# def c1():
#     for i in a:
#         print(i)
#         c2()
#         c3()
#     print()



# c1()


# def itog():
#     global maybe_pass
#     maybe_pass = "".join(maybe_pass)
#     if maybe_pass == a:
#         print(f"Вы загадали: {a}")
#         break
#     return ""


for i in a:
    for j in a:
        for k in a:
            maybe_pass = [i, j, k]
            # print(i, j, k, end="!!! ")
            maybe_pass = "".join(maybe_pass)
            if maybe_pass == b:
                print(f"Вы загадали: {b}")
                break
        if maybe_pass == b:
            break
        # print()
    if maybe_pass == b:
        break
    # print()
print("Конец!")