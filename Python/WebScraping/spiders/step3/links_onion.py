# A first part of a web crowler

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# We scraping the web blog of a jornalist of the Cabrobó city.
# The Blog report of the onion price by week in the ceasa City.
# Get the title of the onion report in the fisrt page of cotation onion.
# We have 32 cotaion onion pages. Get the titles of the first page.
# This titles has the url to page with onion contation of the week


def get_onion_links(url):

    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        bs = BeautifulSoup(html.read(), "html.parser")
        name_list = bs.find_all('h3', {'class': 'entry-title td-module-title'})
        all_links = []
        for name in name_list:
            all_links.append(name.find('a').attrs['href'])
    return all_links


if __name__ == '__main__':
    url = "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola"
    for link in get_onion_links(url):
        print(link)
