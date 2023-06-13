import lxml.html
from lxml import etree


tree = etree.parse('Test_parse.html', lxml.html.HTMLParser())

tag2 = tree.xpath('/html/body/tag1/tag2/text()')
tag3 = tree.xpath('/html/body/tag1/tag3/text()')

text = tag2[0].strip()
number = int(tag3[0])
print(number)
print(text)
print(tag2)
