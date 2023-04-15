import requests
import json

# делаем запрос на сервер по переданному адресу !!! Запрос в формате HTML !!!
# response = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# response = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # Запрос в формате JSON
# response = requests.get('https://api.github.com')
# texts = json.loads(response.content)  # делаем из полученных байтов Python-объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль, оставим только первые 50 символов.
#     print(text[:50], '\n')
# d = json.loads(response.content)  # делаем из полученных байтов Python-объект для удобной работы
# print(type(d))
# print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
# response = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем POST-запрос
# print(response.content)

# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(
#     data))  # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)

# ------------
response = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # Запрос в формате JSON
texts = json.loads(response.content)  # делаем из полученных байтов Python-объект для удобной работы
print(texts)
# ------------
