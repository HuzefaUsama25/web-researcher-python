import bs4
import requests
import sys
import re 
import unicodedata
import os
import random
import datetime
import linecache
import time
import urllib3

#create a for-loop which scrapes the links one by one from the links.txt file
for linenum in range (0,100):
    try:
        #open link num 1-49 from links.txt
        linenumthlink = str(linecache.getline('links.txt',linenum))
        if ('youtube' in linenumthlink):
            print("Skipping link which does not allow scraping....")
        else:
            #print the current number of website being scraped along with it's url
            print(str(str(linenum)+" "+str(linenumthlink)))
            filename=r"D:\Huzefa\Desktop\The Big Researcher\\"+str(linenum)+".html"
            #get request for current website from the links.txt file
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
            res = requests.get(linenumthlink, headers=headers, timeout=50)

            file = open(filename , 'wb')
            #loop through the websites html code and write each paragraph to the text file and then leave a line
            f=res.content
            file.write(f)
            file.close()

    except:
        continue

