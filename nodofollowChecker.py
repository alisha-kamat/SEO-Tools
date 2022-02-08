import re #regex
import urllib.request #URL handling module; used to fetch URLs
from bs4 import BeautifulSoup #for parsing html/xml docs. used to extract data from HTML; useful for web scraping

page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
html = BeautifulSoup(page.read(),"html.parser")
links = html.find_all('a', attrs={"rel": "nofollow", "href": re.compile(r'wiki/')}) #"/wiki/Special:RecentChangesLinked/Main_Page"})
for link in links:
    print(link)
#re.compile(r'crummy\.com/')