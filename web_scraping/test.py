from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL:')
count = input('Enter count:')
position = input('Enter position:')
c = int(count)
p = int(position)

print('Retrieving:', url)

for i in range(c):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all anchor tags
    tags = soup('a')

    # Pick the link at the desired position (convert 1-based to 0-based)
    url = tags[p - 1].get('href', None)
    print('Retrieving:', url)

# # Extract last name from the final URL
# last_name = url.split("_")[-1].split(".")[0]
# print("\nLast name in sequence:", last_name)
