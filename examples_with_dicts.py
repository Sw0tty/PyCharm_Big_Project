professions = ['IT', 'Физика', 'Математика']
persons = [['Гейтс', 'Джобс', 'Возняк'], ['Эйнштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]
for pro, person_list in zip(professions, persons):
    print(f'{pro}:')
    for person in person_list:
        print(person)
    print()

list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_strings = ['Кетчуп', 'Торт', 'Тушенка', 'Яблоко', 'Апельсин', 'Паста']
print(dict(zip(list_of_numbers, list_of_strings)))

# --------------------------------

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

print("hesoyam" in user_database)
print(user_database['hesoyam'])

# --------------------------------

cook_book = {
    'first_el': 'картофель',
    'second_el': 'морковь'
}

for i, j in cook_book.items():
    print(f"{i} -- {j}")

# -------------------------------

# --------1-----------1--------
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Тула', 'Россия']},
    {'visit7': ['Курск', 'Россия']},
    {'visit8': ['Архангельск', 'Россия']}
]
for log in geo_logs:
    print(list(log.values())[0][0], end=" ")
print()
geo_logs_copy = geo_logs.copy()
for log in geo_logs_copy:
    if 'Россия' not in list(log.values())[0]:
        geo_logs.remove(log)
print(geo_logs)
# ------------Метод 2---------------
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Тула', 'Россия']},
    {'visit7': ['Курск', 'Россия']},
    {'visit8': ['Архангельск', 'Россия']}
]
result = []
for i in geo_logs:
    if 'Россия' in list(i.values())[0]:
        result.append(i)
print(result)
# -------1-----------------1---

bodycount = {
    'Проклятие Черной жемчужины': {
        'человек': 17
    },

    'Сундук мертвеца': {
        'человек': 56,
        'раков-отшельников': 1
    },

    'На краю света': {
        'человек': 88
    },

    'На странных берегах': {
        'человек': 56,
        'русалок': 2,
        'ядовитых жаб': 3,
        'пиратов зомби': 2
    }
}
dead = 0
for i in bodycount.values():
    for j in i.values():
        dead += j
print(f"За все фильмы было {dead} смертей разных существ")

# -----------------------------------

people = {1: {'name': 'Oleg', 'age': '29', 'sex': 'Male'},
          2: {'name': 'Kate', 'age': '21', 'sex': 'Female'},
          3: {'name': 'Liza', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Pavel', 'age': '36', 'sex': 'Male'}}
age = 0
for i in people.values():
    age += int(i['age'])
print(f"Общий возраст всех людей {age}")
print(f"Средний возраст всех людей {age / len(people)}")

# -----------------------------------

europe = {'spain': {'capital': 'madrid'},
          'france': {'capital': 'paris'},
          'germany': {'capital': 'berlin'},
          'norway': {'capital': 'oslo'}}
for country, info in europe.items():
    print(f'The capital of {country.title()} is {info["capital"].title()}')
