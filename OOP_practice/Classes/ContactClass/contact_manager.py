from contact import Contact
import pickle
import os


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILE_NAME = 'contacts.dat'


def main():
    choice = 0
    my_contacts = load_contacts()
    while choice != QUIT:
        choice = get_menu()
        if choice == LOOK_UP:
            look_up(my_contacts)
        elif choice == ADD:
            add_contact(my_contacts)
        elif choice == CHANGE:
            change(my_contacts)
        elif choice == DELETE:
            delete_contact(my_contacts)
        elif choice == QUIT:
            save_contacts(my_contacts)
            break
        else:
            print("Неизвестная команда")


def get_menu():
    print()
    print("----Меню----")
    print('1 - Найти контактное лицо')
    print('2 - Добавить новое контактное лицо')
    print('3 - Изменеить существующее контактное лицо')
    print('4 - Удалить существующее контактное лицо')
    print('5 - Выйти из программы')
    print()
    choice = int(input("Введите номер команды "))
    return choice


def load_contacts():
    try:
        with open(os.path.join(os.getcwd(), FILE_NAME), 'rb') as file:
            contact_dct = pickle.load(file)
    except IOError:
        contact_dct = {}

    return contact_dct


def delete_contact(my_contacts):
    name = input("Введите контакт для удаления: ")
    if name in my_contacts:
        del my_contacts[name]
        print("Запись удалена")
    else:
        print("Контакт не найден")


def add_contact(my_contacts):
    name = input("Введите имя пользователя: ")
    if name not in my_contacts:
        phone = input("Введите телефон пользователя: ")
        email = input("Введите Эл. почту пользователя: ")
        contact = Contact(name, phone, email)
        my_contacts[name] = contact
        print("Запись добавлена")
    else:
        print("Данное имя уже существует")


def look_up(my_contacts):
    name = input("Кто вас интересует? ")
    print(my_contacts.get(name, "Контакт не найден"))


def change(my_contacts):
    name = input("Какой контакт изменить? ")
    if name not in my_contacts:
        print("Контакт не найден")
    else:
        phone = input("На что поменять телефон? ")
        email = input("На какое имя Эл. почту? ")
        contact = Contact(name, phone, email)
        my_contacts[name] = contact
        print("Информация обновлена")


def save_contacts(my_contacts):
    with open(os.path.join(os.getcwd(), FILE_NAME), 'ab') as file:
        pickle.dump(my_contacts, file)


if __name__ == '__main__':
    main()
