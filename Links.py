import bs4
import requests
import sys
import os
import re 
import unicodedata

url = input("Search for: ")
filename = "links"

filename=r"D:\Huzefa\Desktop\The Big Researcher\\" +filename+ ".txt"
url = "https://search.yahoo.com/search?p="+url+"&n=100"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "lxml")
##
file = open(filename , 'wb')

search = soup.select("a.ac-algo.fz-l.ac-21th.lh-24")

for link in search[:100]:
    actlink = link.get('href')
    f = actlink
    file.write(unicodedata.normalize('NFD', re.sub("[\(\[].*?[\)\]]", "", f)).encode('ascii', 'ignore'))
    file.write(unicodedata.normalize('NFD', re.sub("[\(\[].*?[\)\]]", "", os.linesep)).encode('ascii', 'ignore'))
file.close()
