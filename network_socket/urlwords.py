import urllib.request as request

url = 'http://data.pr4e.org/intro-short.txt'
response = request.urlopen(url)
count = dict()
for line in response:
    words = line.decode().rstrip()
    for word in words.split():
        count[word] = count.get(word, 0) + 1
response.close()

print(count)
