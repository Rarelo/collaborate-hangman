import json
import random

### General JSON Functions ###

def retrieve_words():
    'pulls and outputs the array of programed words from the JSON'
    with open("hangman.json","r") as json_file:
        return json.load(json_file)

def retrieve_random_word():
    '''pull a random word from the JSON file'''
    current_words = retrieve_words()
    #print(current_words)
    return current_words[random.randint(0,len(current_words)-1)]
