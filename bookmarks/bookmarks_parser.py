import lxml.html
from lxml import etree


tree = etree.parse('bookmarks_22.04.2023.html', lxml.html.HTMLParser())

hyper = tree.xpath('TITLE')

print(hyper)
