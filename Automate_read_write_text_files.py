# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:57:49 2020

@author: mpenm

import requests
import urllib.request 
from bs4 import BeautifulSoup
from urllib.request import urlopen

#req = urllib.request.Request('https://seekingalpha.com/symbol/GOOG/earnings?s=goog', headers={'User-Agent': 'Mozilla/5.0'})

req = requests.get('https://seekingalpha.com/symbol/GOOG/earnings?s=goog', headers={'User-Agent': 'Mozilla/5.0'}).json()
soup = BeautifulSoup(req.content,"html5lib")
soup1 = soup.prettify()


quotes=[]  # a list to store quotes 
  
table = soup.find('section', attrs = {'class':'half-section bg-extra-dark-gray half-section'}) 
  
for row in table.findAll('div', attrs = {'id':'all_quotes'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt']
   
    quotes.append(quote) 

result = soup.find_all('body', class_= "new_symbols_page stick-hd has-slideup tp-modal-close")

with open("testhtml.txt", "w") as file:
    file.write(str(soup1))
"""    
  
import re

file = open("test_read_text.txt")
filename = ""

for line in file.readlines():

        match = re.search(r"Object :\s(.*)", line)
        match1 = re.search(r"DeviceId :\s(.*)", line)
        if match:
            filename = match.group(1)
            continue
        
        if match1:
            folder = match1.group(1)
            foldername = folder.rsplit('\\',2)[-1]
            continue   
       
        if filename:
            wfile = open(filename +'.txt','a')
            wfile.write(line)
        
        if line.strip() == "Endbyte":
            continue
            #break
"""
import re
string = "DeviceId : Synergies\BCX_1\FCU_1"
match1 = re.search(r"DeviceId :\s(.*)", string)
print(match1.group(1))    
    
"""


            
