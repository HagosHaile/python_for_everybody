import urllib.request as request

url = 'http://data.pr4e.org/intro-short.txt'
response = request.urlopen(url)
for line in response:
    words = line.decode().rstrip()
    print(words)
response.close()
