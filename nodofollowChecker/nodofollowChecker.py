import re 
import urllib.request 
from bs4 import BeautifulSoup  

page = urllib.request.urlopen('https://demosite.com/about')
html = BeautifulSoup(page.read(),"html.parser")
links = html.find_all('a', attrs={"rel": "nofollow", "href": re.compile(r'wiki/')}) 
for link in links:
    print(link)
#re.compile(r'example\.com/')