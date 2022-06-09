from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.didigalvao.com.br/")
except URLError as e:
    print(e)
else:
    if html is None:
        print("HTML Page not found!")
    else:
        bsObj = BeautifulSoup(html.read(), features="html.parser")

        print(">>>>>> All content in h1.")
        print(bsObj.body.h1)

        print(">>>>>> Only the text into span tag.")
        print(bsObj.body.h1.span.text)
