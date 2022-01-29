import requests
from datetime import datetime
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = input("enter the tiktok url:")
response = requests.get(url, headers=headers)
#uncomment for full unparsed response
#print(response.url)
aa = response.url
a = response.url.split("&user_id=")[1].split("&")[0]
lang = response.url.split("&language=")[1].split("&")[0]
device = response.url.split("&utm_medium=")[1].split("&")[0]
s = "&utm_source="
funct = ''
for i in aa[aa.index(s)+len(s):] : funct.join(i)

tsp = response.url.split("&timestamp=")[1].split("&")[0]
dt_object = datetime.fromtimestamp(int(tsp))
print(a + " = userid")
print("user device language: " + lang)
print("device OS link originated from: " + device)
print("link was generated using the " + funct + " function")
print("link was generated at " + str(dt_object) + " with the timestamp of " + tsp)
print("-----=====++++=====-----")
print("https://tiktok.com/@" + a)
print("program by jmdevcz")
