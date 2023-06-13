class Employee:
    def __init__(self, name, id_, department, post):
        self.__name = name
        self.__id = id_
        self.__department = department
        self.__post = post

    def __str__(self):
        return f"Имя: {self.__name}\nID: {self.__id}\nОтдел: {self.__department}\nДолжность: {self.__post}"


if __name__ == '__main__':
    emp_list = [['Сьюзи Мейерс', 47899, 'Бухгалтерия', 'Вице-президент'],
                ['Марк Джоунс', 39119, 'IT', 'Программист'],
                ['Джой Роджерс', 81774, 'Производственный', 'Инженер']]

    emp_obj_list = []
    print("--Сотрудники компании--")
    for name, id_, department, post in emp_list:
        employee = Employee(name, id_, department, post)
        emp_obj_list.append(employee)

    for i in emp_obj_list:
        print(i)
        print()
