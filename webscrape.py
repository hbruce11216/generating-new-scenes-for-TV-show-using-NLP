#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:12:51 2020

@author: holdenbruce
"""


#Python program to scrape genius.com
#and save entire script from website
import requests
from bs4 import BeautifulSoup #import beautiful soup to do the web scraping
import csv

def getAndCleanWebScrapedContent(URL):
    URL = 'https://rickandmorty.fandom.com/wiki/Vindicators_3:_The_Return_of_Worldender/Transcript'
    r = requests.get(URL) #get content from url
    
    # from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('div', {'class': ['poem','mw-content-ltr mw-content-text']})
    
    ##extracting all the text from a page
    text = table.get_text()
    
    table2 = []
    table2 = str(text)
    table2 = table2.replace("<br/>","")
    table3 = table2.replace("<i>","")
    table4 = table3.replace("</i>", "")
    table5 = table4.replace("<b>","")
    table6 = table5.replace("</b>", "")
    table7 = table6.replace("<p>", "")
    table8 = table7.replace("</p>", "")
    table9 = table8.replace("<!--sse-->","")
    table10 = table9.replace("<!--/sse-->","")
    table11 = table10.replace("<div>", "")
    table12 = table11.replace("</div>","")
    table13 = table12.replace('<div class="lyrics">', "")

    return(table13)


# for url in list_URL:
#     script = getAndCleanWebScrapedContent(url)    
#     all_the_scripts += script




# URL = "https://genius.com/Rick-and-morty-pilot-annotated" #url of site we will be scraping
# #calling function defined in webscrape to pull script down and clean it
# script = getAndCleanWebScrapedContent(URL)    
# print(script)

def compileScript():
    
    list_URL = [
        'https://rickandmorty.fandom.com/wiki/A_Rickle_in_Time/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Alien:_Covenant_Rick_and_Morty/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Anatomy_Park_(episode)/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Auto_Erotic_Assimilation/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Big_Trouble_in_Little_Sanchez/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Edge_of_Tomorty:_Rick_Die_Rickpeat/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Get_Schwifty/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Interdimensional_Cable_2:_Tempting_Fate/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Close_Rick-counters_of_the_Rick_Kind/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Lawnmower_Dog/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Look_Who%27s_Purging_Now/Transcript',
                       'https://rickandmorty.fandom.com/wiki/M._Night_Shaym-Aliens!/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Meeseeks_and_Destroy/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Morty%27s_Mind_Blowers/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Mortynight_Run/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Never_Ricking_Morty/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Pickle_Rick/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Pilot/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Raising_Gazorpazorp/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Rattlestar_Ricklactica/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Rest_and_Ricklaxation/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Rick_Potion_No._9/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Rickmancing_the_Stone/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Ricksy_Business/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Rixty_Minutes/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Something_Ricked_This_Way_Comes/Transcript'
                       'https://rickandmorty.fandom.com/wiki/Star_Mort_Rickturn_of_the_Jerri/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Tales_From_the_Citadel/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_ABC%27s_of_Beth/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_Rickchurian_Mortydate/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_Ricks_Must_Be_Crazy/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_Rickshank_Rickdemption/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_Vat_of_Acid_Episode/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_Wedding_Squanchers/Transcript',
                       'https://rickandmorty.fandom.com/wiki/The_Whirly_Dirly_Conspiracy/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Total_Rickall/Transcript',
                       'https://rickandmorty.fandom.com/wiki/Vindicators_3:_The_Return_of_Worldender/Transcript'
                      ]

    all_the_scripts = ''
    for url in list_URL:
        script = getAndCleanWebScrapedContent(url)    
        all_the_scripts += script
    # print(all_the_scripts)
    all_the_scripts = all_the_scripts.strip() #.lower()
    
    
    #redirecting
    import sys
    orig_stdout = sys.stdout
    f = open('all_the_scripts.txt', 'w') 
    sys.stdout = f
    print(all_the_scripts) #redirecting to text file all_the_scripts.txt
    sys.stdout = orig_stdout
    f.close()
    
    # print(all_the_scripts)
    
    
# ##tokenize by sentence
# # def tokenizeBySentence():
#     from nltk.tokenize import sent_tokenize
#     tokenized_script = sent_tokenize(all_the_scripts) 
#     # tokenized_script = sent_tokenize(rejoined_string)
#     return tokenized_script
#     #this is now the whole script tokenized by each sentence
#     tokenized_script = tokenizeBySentence()


#     script_dict = {}
#     character_names = []
#     current_character = ''
#     split_script = []

#     for line in tokenized_script:
#         # print(line)
#         line = line.split(":")
#         if line not in split_script:
            
#             # print(line)
#             split_script.append(line)
    
    
#     for line in split_script:
#         if line[0]=='Gear Girl #1':
#             print(line)
    
    
    return all_the_scripts




