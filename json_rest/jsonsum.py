import json
import urllib.request

response = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_2349658.json')
data = response.read().decode()
info = json.loads(data)
lst = list()
val = info["comments"]
for item in val:
    lst.append(int(item["count"]))
print(sum(lst))
