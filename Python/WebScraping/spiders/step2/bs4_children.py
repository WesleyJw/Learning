# In this spider we are studing about metods of library beautifulsoup

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# We still work with the bs4_methods.py problem.

# Work with the same search, now with the children method

try:
    html = urlopen(
        "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola")
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), "html.parser")
    for child in bs.find('div', {'class': 'td-ss-main-content'}).children:
        print(child)
