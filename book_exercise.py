# Напишите несколько строк кода, выводящих на экран ваше имя и почто-
# вый адрес. Адрес напишите в формате, принятом в вашей стране. Ника-
# кого ввода от пользователя ваша первая программа принимать не будет,
# только вывод на экран и больше ничего.

# name = "Кирилл"
# post_address = "1470"
# print(f"Приверт {name}. Ваш почтовый адрес {post_address}")

# Напишите программу, запрашивающую у пользователя его имя. В ответ
# на ввод на экране должно появиться приветствие с обращением по имени,
# введенному с клавиатуры ранее.

# name = input("Как вас зовут? ")
# print(f"{name}, приятно познакомиться!")

# Напишите программу, запрашивающую у  пользователя длину и  ширину
# комнаты. После ввода значений должен быть произведен расчет площади
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами
# измерения, принятыми в вашей стране. Это могут быть футы или метры.

# HEIGHT = float(input("Введите длину комнаты "))
# WIDTH = float(input("Введите ширину комнаты "))
#
# print(f"Площадь вашей комнаты {HEIGHT * WIDTH} квадратных метров")

# Создайте программу, запрашивающую у пользователя длину и  ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.
# Подсказка. В одном акре содержится 43 560 квадратных футов.

# akr = 43560
# HEIGHT = float(input("Введите длину участка "))
# WIDTH = float(input("Введите ширину участка "))
#
# print(f"Площадь вашего участка {akr / (HEIGHT * WIDTH)} акров")

# Во многих странах в стоимость стеклотары закладывается определенный
# депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
# тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
# ки большего объема – $0,25.
# Напишите программу, запрашивающую у пользователя количество бу-
# тылок каждого размера. На экране должна отобразиться сумма, которую
# можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
# вывод так, чтобы сумма включала два знака после запятой и дополнялась
# слева символом доллара.

tara1 = ""
tara2 = ""
while not tara1.isdigit():
    tara1 = input("Сколько у вас бутылок 1 и меньше литров? ")
while not tara2.isdigit():
    tara2 = input("Сколько у вас бутылок больше 1 литра? ")

tara1, tara2 = int(tara1), int(tara2)
print(f"Продав все бутылки, вы сможите выручить ${round(tara1 * 0.1 + tara2 * 0.25, 2)}")

# Программа, которую вы напишете, должна начинаться с запроса у поль-
# зователя суммы заказа в ресторане. После этого должен быть произведен
# расчет налога и  чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
# де программа должна отобразить отдельно налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.
