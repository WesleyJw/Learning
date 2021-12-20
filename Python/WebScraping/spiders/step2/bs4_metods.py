# In this spider we are studing about metods of library beautifulsoup

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# We scraping the web blog of a jornalist of the Cabrobó city.
# The Blog report of the onion price by week in the ceasa City.
# Get the title of the onion report in the fisrt page of cotation onion.
# We have 32 cotaion onion pages. Get the titles of the first page.
# This titles has the url to page with onion contation of the week

try:
    html = urlopen(
        "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola")
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), "html.parser")
    name_list = bs.find_all('h3', {'class': 'entry-title td-module-title'})
    for name in name_list:
        print(name.get_text())
