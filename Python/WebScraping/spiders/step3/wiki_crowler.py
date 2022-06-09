# We go to crowler the wikipidea page
# In the page http://en.wikipedia.org/
# we are search for Kevin_Bacon page and
# Search for links to save links related with
# another equal pages.

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import re
import random
random.seed(datetime.datetime.now())


def get_links(articleURL):
    try:
        html = urlopen('https://wikipedia.org{}'.format(articleURL))
    except HTTPError as e:
        print(e)
    else:
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_links('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArcticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArcticle)
    links = get_links(newArcticle)
