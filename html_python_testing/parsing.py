import requests
import lxml.html
from lxml import etree

# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head>,
# который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится
# основная информация о страничке, её название и инструкции по отображению в браузере)
# print(title)  # выводим полученный заголовок страницы


# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome_to_Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с
# помощью html-парсера. Сам html - это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент метода findall
# скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>.
    # Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью.
    time = li.find('time')
    print(f"Время добавления: {time.get('datetime'):<40s}", a.text)  # из этого тега забираем текст, это и будет нашим названием






