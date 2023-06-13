from warehouse_item import WarehouseItem
import pickle
import os


HELP = 'help'
CHECK_ITEM = 1
SELL_ITEM = 2
CHANGE_ITEM = 3
ADD_ITEM = 4
THROW_OUT_ITEM = 5
QUIT = 6


FILE_NAME = 'warehouse.dat'


def main():
    choice = 0
    wh_items = items_load()
    while choice != QUIT:
        choice = input("Введите команду для склада. (help - команды)")
        if choice.isdigit():
            choice = int(choice)
        elif choice.isalpha():
            choice = choice.lower().strip()

        if choice == HELP:
            commands_menu()
        elif choice == CHECK_ITEM:
            items_check(wh_items)
        elif choice == SELL_ITEM:
            pass
        elif choice == CHANGE_ITEM:
            pass
        elif choice == ADD_ITEM:
            pass
        elif choice == THROW_OUT_ITEM:
            pass
        else:
            print("Команда не распознана!")

    close_warehouse(wh_items)


def items_load():
    try:
        with open(os.path.join(os.getcwd(), FILE_NAME), 'rb') as file:
            warehouse_dct = pickle.load(file)
    except IOError:
        warehouse_dct = {}

    return warehouse_dct


def commands_menu():
    menu = '--Меню--'
    print('^' + '-' * 20 + '^')
    print(f'{menu:^22}')
    print('  1 - Найти товар на складе')
    print('  2 - Продать товар со склада')
    print('  3 - Изменить цену товара')
    print('  4 - Закупить товар')
    print('  5 - Выбросить товар со склада')
    print('  6 - Закрыть склад')
    # print('7 - Найти товар на складе')


def items_check(wh_items):
    item = input("Какой товар найти на складе: ")
    print(wh_items.get(item, "Товар не найден"))


def add_item(wh_items):
    item = input("Какой товар закупить: ")
    if item in wh_items:
        print("Товар уже есть на складе. Произвести докупку?") # ###############
    else:
        name = input()
        value = int(input())
        price = input()
        manufacture = input()
        expiration_date = input()
        new_item = WarehouseItem(name, value, price, manufacture, expiration_date)


def close_warehouse(wh_items):
    with open(os.path.join(os.getcwd(), FILE_NAME), 'ab') as file:
        pickle.dump(wh_items, file)


if __name__ == '__main__':
    main()
