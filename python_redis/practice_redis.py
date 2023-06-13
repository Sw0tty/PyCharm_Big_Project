import redis
import json
import time


redis_connect = redis.Redis(
    host='',
    port=,
    password=''
)

command_dict = {'add': 'Добавить телефон и его владельца в БД',
                'show_all': 'Вывести список телефонной книги',
                'delete_number': 'Удалить телефон из телефонной книги',
                'delete_all': 'Удалить всю телефонную книгу',
                'close': 'Выйти из БД'}

while True:
    command = input("Введите команду для работы с БД. help - вывести список команд ")
    if command == 'help':
        for i, j in command_dict.items():
            print(f"{i:>8s} --- {j}")
    elif command == 'add':
        while True:
            number = input("Какой телефон нужно добавить?")
            if number.isdigit():
                if len(number) != 11:
                    print("Не хватает цифр")
                    continue
                break
            print("Телефон состоит из цифр")
            continue
        number = "{}-({}{}{})-{}{}{}-{}{}-{}{}".format(*list("".join(number)))
        while True:
            phone_owner = input("""Как записать владельца? Оставьте поле пустым, чтобы записать, как 'Неизвестный'""")
            if phone_owner.isspace():
                print("Строка содержит только пробелы")
                continue
            elif not phone_owner:
                phone_owner = "Неизвестный"
                break
            elif not phone_owner.isspace():
                break
            break
        try:
            converted_numbers_dict = json.loads(redis_connect.get('numbers_dict'))
            update_dict = converted_numbers_dict
            update_dict[number] = phone_owner
            redis_connect.set('numbers_dict', json.dumps(update_dict))
        except TypeError:
            new_number_dict = {number: phone_owner}
            redis_connect.set('numbers_dict', json.dumps(new_number_dict))
    elif command == 'show_all':
        try:
            converted_numbers_dict = json.loads(redis_connect.get('numbers_dict'))
            for i, j in converted_numbers_dict.items():
                print(f"{i:>11s} --- {j}")
        except TypeError:
            print("Телефонной книги не существует")

    elif command == 'delete_number':
        while True:
            number = input("Какой телефон удалить? ")
            if number.isdigit():
                if len(number) != 11:
                    print("Не хватает цифр")
                    continue
                break
            print("Телефон состоит из цифр")
            continue
        number = "{}-({}{}{})-{}{}{}-{}{}-{}{}".format(*list("".join(number)))


        try:
            converted_numbers_dict = json.loads(redis_connect.get('numbers_dict'))
            delete_number = converted_numbers_dict
            del delete_number[number]
            redis_connect.set('numbers_dict', json.dumps(delete_number))
        except TypeError:
            print("Телефон не найден")

    elif command == 'delete_all':
        confirmation = input("Вы ТОЧНО хотите удалить всю книгу, без способа восстановления? Y - да, N - нет ")
        if confirmation in command_dict:
            pass
        if confirmation.upper() == 'N':
            print("Процесс удаления предотвращен")
            time.sleep(1)
        elif confirmation == 'Y':
            print("Идет процесс удаления...")
            redis_connect.delete('numbers_dict')
            time.sleep(3)
            print("Телефонная книга удалена из БД")
            time.sleep(1)
        else:
            print("Введена неизвестная команда, процесс предотвращен")
            time.sleep(1)
    elif command == 'close':
        break


