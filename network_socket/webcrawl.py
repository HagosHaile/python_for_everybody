import urllib.request as request
from bs4 import BeautifulSoup
#import ssl

#ctx = ssl._create_unverified_context()
url = 'https://data.pr4e.org/page1.htm'
response = request.urlopen(url).read()
#response = request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(response, 'html.parser')

links = list()
tags = soup('a')
for tag in tags:
    links.append(tag.get('href', None))

for link in links:
    response = request.urlopen(link)
    for line in response:
        print(line.decode().rstrip())

