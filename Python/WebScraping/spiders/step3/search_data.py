from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

html = urlopen(
    "https://www.didigalvao.com.br/cotacao-da-cebola-nesta-sexta-05-em-cabrobo/")
bs = BeautifulSoup(html, "html.parser")

text = bs.find('div', {'class': 'td-post-content'}).get_text()

print(text)

print("-"*50)

patterns = {"yell_box2": r"(AMARELA CAIXA 2 .{8})",
            "yell_box3": r"(AMARELA CAIXA 3 .{8})",
            "red_box2": r"(ROXA CAIXA 2 .{8})",
            "red_box3": r"(ROXA CAIXA 3 .{8})"}

collection = {"yell_box2": None,
              "yell_box3": None,
              "red_box2": None,
              "red_box3": None}

for key, value in patterns.items():
    data = re.findall(value, text.upper())
    collection[key] = data

collection.update(date=bs.find('span', {'class': 'td-post-date'}).get_text())
print(collection)
