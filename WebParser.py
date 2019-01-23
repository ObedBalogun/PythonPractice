import urllib.request as url
import urllib.parse as par
import re

url_link = 'http://pythonprogramming.net'
values = {
    's':'basics',
    'submit':'search'
}
data = par.urlencode(values).encode('utf-8')
req = url.Request(url_link,data)
resp = url.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</>', str(respData))  #.*? basically prints everything
for paragraph in paragraphs:
    print(paragraph)