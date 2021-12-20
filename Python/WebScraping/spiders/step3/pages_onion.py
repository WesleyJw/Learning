# This Spider get the number of pages that store the cotation onion links

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# Get the pages number


def get_page_url(url):

    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
    else:
        if html is None:
            print("Page empty!")
        else:
            bs = BeautifulSoup(html, "html.parser")
            current = bs.find('span', {'class': 'current'}).get_text()
            title = str(int(current) + 1)
            try:
                next_page = bs.find('a', {'title': title}).attrs['href']
            except AttributeError:
                next_page = ""
    return next_page

# Get url of the next page


if __name__ == '__main__':
    url = "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola"
    while url:
        print(url)
        url = get_page_url(url)
