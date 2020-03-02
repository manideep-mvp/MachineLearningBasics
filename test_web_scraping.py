# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:18:43 2020

@author: mpenm
"""

import requests
import urllib.request 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

#req = urllib.request.Request('https://seekingalpha.com/symbol/GOOG/earnings?s=goog', headers={'User-Agent': 'Mozilla/5.0'})

req = requests.get('https://www.passiton.com/inspirational-quotes', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(req.content,"html5lib")


quotes=[]  # a list to store quotes 
  
table = soup.find('section', attrs = {'class':'half-section bg-extra-dark-gray half-section'}) 
  
for row in table.findAll('div', attrs = {'id':'all_quotes'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt']
   
    quotes.append(quote) 
    

"""filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote)     
"""