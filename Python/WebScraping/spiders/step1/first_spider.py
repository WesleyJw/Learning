# The scraper test
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Example 1: Only use urlopen and print the result

#html = urlopen("http://pythonscraping.com/pages/page1.html")

# print(html.read())

# Example 2: Work with BeautifulSoup to get the specific elements
html = urlopen("https://www.didigalvao.com.br/")

bsObj = BeautifulSoup(html.read(), features="html.parser")

print(">>>>>> All content in h1.")
print(bsObj.body.h1)

print(">>>>>> Only the text into span tag.")
print(bsObj.body.h1.span.text)
