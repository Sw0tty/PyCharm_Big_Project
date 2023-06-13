from cell_phone import CellPhone
from time import sleep as time_sleep


def main():
    print("--Чтобы завести телефон на склад, заполните данные.--")

    phones_list = make_list()

    answer = input("--Хотите посмотртеть информацию о товарах? (Y - да)--")
    if answer == 'Y':
        return return_data_list(phones_list)
    return "Заполнение закончено"


def return_data_list(phones_list):
    for i, j in enumerate(phones_list):
        print(f"Информация о {i + 1} товаре:")
        print(f"\tПроизводитель: {j.get_manufact()}", f"\tМодель: {j.get_model()}",
              f"\tЦена: {j.get_retail_price()}", sep='\n')
    return "Товары закончились"

def make_list():
    phones_list = []
    for i in range(5):
        manufact = input("Введите производителя: ")
        model = input("Введите модель: ")
        retail_price = input("Введите розничную цену: ")
        print("--Идет добавление товара на склад.--")
        new_phone = CellPhone(manufact, model, retail_price)
        phones_list.append(new_phone)
        time_sleep(1)
        print("--Товар успешно добавлен--")
    return phones_list


if __name__ == '__main__':
    print(main())
