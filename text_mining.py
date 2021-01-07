#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:23:42 2020

@author: holdenbruce
"""
import nltk
nltk.download('punkt')

from webscrape import getAndCleanWebScrapedContent,compileScript

all_the_scripts = compileScript()

#################################################
##### pre-procesing for sentiment analysis ######
#################################################

def preprocessingForSentimentAnalysis(script):
#strip punctuation and stopwords
    from string import punctuation
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words("english"))
    #this will split the script string on whitespace (by each word)
    split = script.split() 
        
    #loop through each word in script and if each word is 
    #not in stop_words, then add that word to the list of no_stopwords
    no_stopwords = []
    for word in split:
        if word.lower() not in stop_words:
            no_stopwords.append(word)
            
    #loop through each word in no_stopwords and if each item is 
    #not a punctuation, then add that item to the list of no_punctuation
    #this list contains only non-stopwords and does not include individual
    #items of punctuation that were before being interpreted as words
    no_punctuation_no_stopwords = []
    for word in no_stopwords:
        if word not in punctuation:
            no_punctuation_no_stopwords.append(word)
            
    #rejoin the list into one large string
    rejoined_string = ' '.join(split) 
    # rejoined_string = ' '.join(no_punctuation_no_stopwords) 
    #print(rejoined_string)
    return rejoined_string
             
    #word frequency before stopwords taken out
    word_freq = {}
    words = []
    for word in split:
        if word in words:
           word_freq[word] += 1
        else:
            words.append(word)
            word_freq[word] = 1
    #order by values
    sort_freqs = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    #print the top 10 most used words
    for i in sort_freqs[:10]:
    	print(i[0], i[1])
            
    #word frequency after stopwords taken out
    word_freq = {}
    words = []
    for word in no_punctuation_no_stopwords:
        if word in words:
           word_freq[word] += 1
        else:
            words.append(word)
            word_freq[word] = 1
    #order by values
    sort_freqs = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    #print the top 10 most used words
    for i in sort_freqs[:10]:
    	print(i[0], i[1])
        
            
##################################################
############# for sentiment analysis #############
##################################################

rejoined_string = preprocessingForSentimentAnalysis(all_the_scripts)



##tokenize by sentence
def tokenizeBySentence(string):
    from nltk.tokenize import sent_tokenize
    tokenized_script = sent_tokenize(string) 
    # tokenized_script = sent_tokenize(rejoined_string)
    #print(tokenized_script)
    return tokenized_script

#this is now the whole script tokenized by each sentence
tokenized_script = tokenizeBySentence(all_the_scripts)


###split script by character name
def splitCharacterByName(script):
    
    script_dict = {}
    character_names = []
    current_character = ''
    split_script = []

    for line in script:
        line = line.split(":")
        if line not in split_script:
            # print(line)
            split_script.append(line)
    for line in split_script:
        # if len(line)==2:
        #     print(line[0])         
        #if line contains character heading and character not in list of character names
        if len(line)==2 and line[0] not in character_names and len(line[0])<20: #and line[0].isupper()
            # print(line[1])
            # print(line[0])
            character_names.append(line[0])            
            current_character = line[0]    
            script_dict[current_character] = line[1]          
            # for element in line[1]:
            #     if punctuation not in element or stopwords not in element:
            #         script_dict_no_punct_no_stopwords[line[0]] = line[1].lower() #make the words lowercase
        #if line contains character heading and character IS in list of character names
        elif len(line)==2 and line[0] in character_names: #len(line)==2 and 
            current_character = line[0]    
            script_dict[current_character] += line[1] 
            # if len(line)==1:
            #     script_dict[current_character] += line
            # print(line)
                # if punctuation not in line or stopwords not in line:
                #     script_dict_no_punct_no_stopwords[current_character] += line.lower() #make the words lowercase
        #if line does not contain character heading, add it to the most recent character
        elif len(line)==1: 
            if current_character == '':
                pass
            else:    
                print(current_character)
                print(line[0])
                script_dict[current_character] += line[0] 
    print(script_dict)
    return script_dict


#this is a dictionary containing each character heading (like "Morty") and every
#line that comes after that unique character heading
script_dict = splitCharacterByName(tokenized_script)
# len(script_dict['Rick'])


##tokenize by word
def tokenizeByWord(script):
    from nltk.tokenize import word_tokenize
    # tokenized_script = sent_tokenize(all_the_scripts) 
    # check_list = []
    for character in script:
        script[character] = word_tokenize(script[character])
    
    return script

script_dict = tokenizeByWord(script_dict)
# len(script_dict['Rick'])



def mainCharacters(wordDict):

    main_characters = []
    ##determine main characters
    #order characters by number of words they said
    for character in wordDict:
        if len(wordDict[character]) > 175:
            main_characters.append(character)
            # print(character)    
        # print(sorted(wordDict.values()))#print(character, len(wordDict[character]))#word.lower()
    # main_characters
    
    # len(wordDict['Rick'])
    for character in main_characters:
        if 'Rick' in character and character!='Rick':
            wordDict['Rick'] += wordDict[character]
    for character in main_characters:
        if 'Morty' in character and character!='Morty':
            wordDict['Morty'] += wordDict[character]
    # len(wordDict['Rick'])
    
    main_characters = []
    for character in wordDict:
        if len(wordDict[character]) > 175:
            main_characters.append(character)

    return main_characters

main_characters = mainCharacters(script_dict)
# len(script_dict['Rick'])


character_script = splitCharacterByName(tokenized_script)
 



#redirecting
import sys
orig_stdout = sys.stdout
#redirecting

morty_lines = ''
rick_lines = ''
for character in character_script:
    # print(type(character_script[character]))
    if character == 'Morty':
        f = open('morty_lines.txt', 'w') #redirecting
        sys.stdout = f
        print(character_script[character]) #redirecting
        morty_lines += character_script[character]
    elif character == 'Rick':
        f = open('rick_lines.txt', 'w') #redirecting
        sys.stdout = f
        print(character_script[character]) #redirecting
        rick_lines += character_script[character]
#redirecting
sys.stdout = orig_stdout
f.close()



##### markov chains

from collections import defaultdict
# from Text_Analysis_Functions import RickLines, MortyLines
# import nltk
# from nltk.tokenize import word_tokenize


def MC(a): #MC = Markov Chain
    words = a #Tokenized words
    m_dict = defaultdict(list)
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)
    m_dict = dict(m_dict)
    return m_dict


split_morty_lines = morty_lines.split(' ')
mc_guess_morty = MC(split_morty_lines)
#print(mc_guess_morty)

split_rick_lines = rick_lines.split(' ')
mc_guess_rick = MC(split_rick_lines)


import random
def generate_sent(chain, count=25):
    word1 = random.choice(list(chain.keys()))
    sentence = word1.capitalize()
    for i in range(count-1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2
    sentence += '.'
    return sentence
generate_sent(mc_guess_morty)
sentence1 = generate_sent(mc_guess_morty)
sentence2 = generate_sent(mc_guess_morty)



#######################################
## TESTING
#######################################

import unittest

class TestRandM(unittest.TestCase):
 
    # Test that compileScipt function imported from webscrape is returning
    # the compilation of all the scripts
    def test_compileScript(self):
        #compile script
        test_all_the_scripts = compileScript()
        
        #obtain and check for correct length
        self.assertNotEqual(len(test_all_the_scripts), 0)
    
    # Test that preprocessing correctly pre-process the script for sentiment analysis
    def test_preprocessingForSentimentAnalysis(self):
        test_script = "Rick: This Huh, I'm seeing more croc than bot here.\
        Supernova: While Goddammit!\
        Morty: Uh, what happened on Dorian 5?\
        Supernova: Nothing!\
        Alan: Nothing?! We exterminated a planet!\
        Morty: W-Wait, huh?"
        
        correct_output = "Rick: This Huh, I'm seeing more croc than bot here. Supernova: While Goddammit! Morty: Uh, what happened on Dorian 5? Supernova: Nothing! Alan: Nothing?! We exterminated a planet! Morty: W-Wait, huh?"
        test_preString = preprocessingForSentimentAnalysis(test_script)
        
        self.assertEqual(test_preString, correct_output)
        
    # Test that tokenize by sentence function splits the script into an array of sentences
    def test_tokenizeBySentence(self):
        
        test_script2 = "If their DNA gets into Earth's food chain, our entire species could be sterilized. Morty: Then why aren't we killing them?"
        test_script2 = preprocessingForSentimentAnalysis(test_script2)
        test_preString2 = tokenizeBySentence(test_script2)
        correct_output2 = [''"If their DNA gets into Earth's food chain, our entire species could be sterilized.", "Morty: Then why aren't we killing them?"'']
        self.assertEqual(test_preString2, correct_output2)

    # Test that split characters by name correctly builds a dictionary where
    # the key is the character name and the value is their line in the script
    def test_splitCharacterByName(self):
        test_script3 = "Rick: If their DNA gets into Earth's food chain, our entire species could be sterilized. Morty: Then why aren't we killing them?"
        test_script3 = preprocessingForSentimentAnalysis(test_script3)
        test_tokenized_by_sentence = tokenizeBySentence(test_script3)
        
        test_scripDict = splitCharacterByName(test_tokenized_by_sentence)
        
        self.assertNotEqual(test_scripDict.get("Rick"), test_scripDict.get("Morty")) 
        self.assertEqual(test_scripDict.get("Rick"), " If their DNA gets into Earth's food chain, our entire species could be sterilized.")
        self.assertEqual(test_scripDict.get("Morty"), " Then why aren't we killing them?")

    # Test that tokenize by word correctly takes the sentence dictionary and
    # returns a new dictionary where the value is now an array of word
    def test_tokenizeByWord(self):
        test_script3 = "Rick: If their DNA gets into Earth's food chain, our entire species could be sterilized. Morty: Then why aren't we killing them?"
        test_script3 = preprocessingForSentimentAnalysis(test_script3)
        test_tokenized_by_sentence = tokenizeBySentence(test_script3)
        test_scripDict = splitCharacterByName(test_tokenized_by_sentence)
        
        test_tokenized_by_word = tokenizeByWord(test_scripDict)
        self.assertEqual(len(test_tokenized_by_word), 2)
        self.assertEqual(len(test_tokenized_by_word.get('Rick')), 17)
        self.assertEqual(len(test_tokenized_by_word.get('Morty')), 8)
    
    # Test that main characters function will return an array of characters with
    # more than 175 words 
    def test_mainCharacters(self):
        
        supportingCharacter = []
        for i in range(174):
            supportingCharacter.append('word')
        mainCharacter = []
        for i in range(176):
            mainCharacter.append('word')
            
        charDict = {
            'Main': mainCharacter,
            'Support': supportingCharacter
        }
        
        mainChars = mainCharacters(charDict)
        
        self.assertEqual(len(mainChars),1)
        self.assertEqual(mainChars[0],'Main')
        
        
    # test to see if Markov Chain is creating different values 
    def test_MC(self):
        self.assertNotEqual(mc_guess_morty, mc_guess_rick)
        self.assertTrue(mc_guess_morty.get("Then"), "Then")
        
    
    # test to see if generating a novel sentence is working
    def test_generate_sent(self):
        self.assertNotEqual(len(sentence1), 0)
        self.assertNotEqual(sentence1, sentence2)
        
        
if __name__ == '__main__':
     unittest.main()


    