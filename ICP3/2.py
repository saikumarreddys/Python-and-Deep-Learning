import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Deep_learning"
response=requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")


# Extracting title of the page.
print(soup.select('title')[0].text.strip())

# Extracting <a> tags
result = soup.findAll('a')
print(result)


# Iterating over <a> tags and getting extracting href with links.
for r in result:

    if(str(r.get('href')).startswith('https')):
        print(r.get('href'))
