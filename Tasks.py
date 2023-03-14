import math
key = None
tasks_list = [{'1.1': 'Выведите на экран строковые представления числа 53 в двоичной, восьмеричной и шестнадцатеричной системах счисления'},
              {'1.3': 'Зная, что 1372 является числом в восьмеричной системе счисления, выведите на экран значение этого числа в десятичной'
                      'системе счисления (Начальное условие) Свое условие: Написать программу перевода любого целового числа в 8-ичной СС в 10-чную СС'},
              {'1.7': 'Даны два действительных числа a и b. Вычислите их сумму, разность, произведение и частное при a=3.79 и b=84.93.'
                      'Округлите результаты до сотых и выведите их на экран'},
              {'1.8': 'Вычислите значение выражения (10/2.3 - 3^4)*0.7 + 9^0.5,'
                      'округлив результат до трех знаков после десятичной точки и найдя его модуль'},
              {'1.10': 'Извлеките квадратный корень из 196 тремя способами'},
              {'1.11': 'Выведите на экран результат вычисления sin(π/6) и cos(45°) округлив результат до двух знаков после десятичной точки'},
              {'1.12': 'Вычислите значение арифметического выражения при заданных значениях переменных и выведите полученный результат на экран: 5.2a^3 + 3b^5 - 7.3 при a=3, b=2.5'},
              {'2.12': 'Дана строка "-..-.--..-.--". После каждой точки допишите еще по одной точке и выведите результат на экран'},
              {'2.13': 'Дана строка "131231442145". Подсчитайте в ней количество символов "1" и выведите результат на экран'},
              {'2.14': 'Посчитайте устно, а затем проверьте себя, выведя на экран сумму индексов символа "а" в строках "повар" и "Пайтон"'},
              {'***': 'Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию (пример данных представлен ниже).'
                      'Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и отображать информацию о суммарном количестве требуемых ингредиентов в указанном виде'}]
final_result = ["Сыр: 210 гр", "Томаты: 6 шт", "Огурцы: 60 гр", "Маслины: 30 гр", "Оливковое масло: 60 мл",
        "Салат: 30 гр", "Перец: 60 гр", "Колбаса: 90 гр", "Бекон: 90 гр", "Оливки: 30 гр", "Томаты: 60 гр",
        "Тесто: 300 гр", "Лимон: 3 шт", "Вода: 600 мл", "Сахар: 30 гр", "Лайм: 60 гр"]


def task_1_1():
    print("\n", "------------------------", sep="")
    number = 53
    print("Дано число - 53", f"2-ичная {bin(number)}", "8-ричная %o" % number, "16-ричная %x" % number, sep="\n")
    print("------------------------")
    return ""


def task_1_3():
    print("\n", "------------------------", sep="")
    number_in_eight = input("Введите число для перевода из 8-чной в 10-чную СС: ")
    n = len(number_in_eight) - 1
    in_ten = 0
    number_spliter = list(map(int, number_in_eight))
    for i_tennety in number_spliter:
        tennety = i_tennety * pow(8, n)
        n -= 1
        in_ten += tennety
    print("8-ричная", number_in_eight)
    print("В 10-чной:", in_ten)
    print("------------------------")
    return ""


def task_1_7():
    print("\n", "------------------------", sep="")
    a = 3.79
    b = 84.93
    print("Даны числа 3.79 и 84.93", "\n", f"Сумма:{round(a + b, 2)}, Разность:{round(a - b, 2)}, "
                                           f"Произведение:{round(a * b, 2)}, Частное:{round(a / b, 2)}", sep="")
    print("------------------------")
    return ""


def task_1_8():
    print("\n", "------------------------", sep="")
    print("Вычислить: (10/2.3 - 3(в степени 4))*0.7 + 9(в степени 0.5)", "\n",
          f"Ответ:{abs(round((10 / 2.3 - pow(3, 4) * 0.7 + pow(9, 0.5)), 3))}",
          sep="")
    print("------------------------")
    return ""


def task_1_10():
    print("\n", "------------------------", sep="")
    print("Извлеките квадратный корень из 196 тремя способами:", "\n",
          f"Через функцию sqrt: {int(math.sqrt(196))}\nЧерез оператор **: {int(196 ** 0.5)}"
          f"\nЧерез функцию pow(): {int(pow(196, 0.5))}", sep="")
    print("------------------------")
    return ""


def task_1_11():
    print("\n", "------------------------", sep="")
    print(f"sin(π/6): {round(math.sin(math.pi / 6), 2)}\ncos(45°): {math.cos(math.radians(45))}", sep="")
    print("------------------------")
    return ""


def task_1_12():
    print("\n", "------------------------", sep="")
    a = 3
    b = 2.5
    print(f"Ответ: {5.2 * pow(a, 3) + 3 * pow(b, 5) - 7.3}")
    print("------------------------")
    return ""


def task_2_12():
    print("\n", "------------------------", sep="")
    dot_tere = "-..-.--..-.--"
    new_dot_tere = ""
    last_one = "-"
    for i in dot_tere:
        if i == "-" and last_one != "-":
            new_dot_tere += "."
            new_dot_tere += i
        else:
            new_dot_tere += i
        last_one = i
    print(dot_tere)
    print(new_dot_tere)
    print("------------------------")
    return ""


def task_2_13():
    print("\n", "------------------------", sep="")
    element = 0
    for i in "131231442145":
        if i == "1":
            element += 1
    print(element)
    print("------------------------")
    return ""


def task_2_14():
    print("\n", "------------------------", sep="")
    element = 0
    first_string = "повар"
    second_string = "Пайтон"
    for i in first_string:
        if i == "а":
            element += first_string.index(i)
    for i in second_string:
        if i == "а":
            element += second_string.index(i)
    print(element)
    print("------------------------")
    return ""


def task_vebinar():
    print("\n", "------------------------", sep="")
    cook_book = {
        'салат': [
            {'ingredient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
            {'ingredient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},  #
            {'ingredient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},  #
            {'ingredient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},  #
            {'ingredient_name': 'салат', 'quantity': 10, 'measure': 'гр'},  #
            {'ingredient_name': 'перец', 'quantity': 20, 'measure': 'гр'}  #
        ],
        'пицца': [
            {'ingredient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
            {'ingredient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},  #
            {'ingredient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},  #
            {'ingredient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},  #
            {'ingredient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
            {'ingredient_name': 'тесто', 'quantity': 100, 'measure': 'гр'}  #
        ],
        'лимонад': [
            {'ingredient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},  #
            {'ingredient_name': 'вода', 'quantity': 200, 'measure': 'мл'},  #
            {'ingredient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},  #
            {'ingredient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},  #
        ]
    }
    portion = int(input("На сколько порций рассчитать ингредиентов? "))
    new_recept = []
    final_recept = []
    check = 0
    check2 = 0
    for i in cook_book:
        for j in cook_book[i]:
            new_recept.append(list(j.values()))
    for i in new_recept:
        for j in new_recept:
            if j[0] == i[0] and j[2] == i[2]:
                check += 1
                check2 += j[1]
        if check < 2:
            i[1] = i[1] * portion
            final_recept.append(i)
        else:
            more_then_two = [i[0], check2, i[2]]
            more_then_two[1] = more_then_two[1] * portion
            if more_then_two not in final_recept:
                final_recept.append(more_then_two)
        check2 = 0
        check = 0
    for i in final_recept:
        for j in i:
            print(f"{j[0].title()}: {j[1]} {j[2]}", end=" ")
        print()

    # string1 = []
    # string2 = []
    #
    # for i in cook_book:
    #     for j in cook_book[i]:
    #         main_rec = [j['ingredient_name'], j['measure']]
    #         print(main_rec)
    #         for k in cook_book[i]:
    #             main_rec2 = [k['ingredient_name'], k['measure']]
    #             if main_rec == main_rec2:
    #                 check += 1
    #             print(main_rec2)
    #         print(check)
    #         check = 0
    #         print(main_rec)
    # print('\n' * 5)
    # for k in j.values():
    #     string2.append(k)
    #     #print(k)
    #     for m in j.values():
    #         string1.append(m)
    #     print(string1)
    #     print(string2)
    #     new_recept.append(string1)
    #     string1 = []
    # final_recept.append(string2)
    # string2 = []
    # print(new_recept)
    # print(len(final_recept))


    # for i in new_recept:
    #     for j in new_recept:
    #         if j[0] == i[0] and j[2] == i[2]:
    #             check += 1
    #             check2 += j[1]
    #     if check < 2:
    #         i[1] = i[1] * portion
    #         final_recept.append(i)
    #     else:
    #         ppp = [i[0], check2, i[2]]
    #         ppp[1] = ppp[1] * portion
    #         if ppp not in final_recept:
    #             final_recept.append(ppp)
    #     check2 = 0
    #     check = 0
    # for i in final_recept:
    #     for j in i:
    #         print(j, end=" ")
    #     print()

    print("------------------------")
    return ""


while key != "quit":
    key = input("Какую задачу решить (номер)? Вывести список - tasks, Выйти - quit ")
    if key == "tasks":
        for i_tasks in tasks_list:
            print(f"Задача - {list(i_tasks.keys())[0]} - {list(i_tasks.values())[0]}")
    if key == "1.1":
        print(task_1_1())
    if key == "1.3":
        print(task_1_3())
    if key == "1.7":
        print(task_1_7())
    if key == "1.8":
        print(task_1_8())
    if key == "1.10":
        print(task_1_10())
    if key == "1.11":
        print(task_1_11())
    if key == "2.12":
        print(task_2_12())
    if key == "2.13":
        print(task_2_13())
    if key == "2.14":
        print(task_2_14())
    if key == "***":
        print(task_vebinar())
