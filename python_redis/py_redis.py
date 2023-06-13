import redis
import json

redis_connect = redis.Redis(
    host='',
    port=,
    password=''
)

# redis_connect.set('var1', json.dumps('values3'))
#
# my_value = json.loads(redis_connect.get('var1'))
#
# print(my_value)

# redis_connect.delete('var1')
# print(redis_connect.get('var1'))


# dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
# redis_connect.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# converted_dict = json.loads(redis_connect.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
# # print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
# print(converted_dict)  # ну и выводим его содержание
