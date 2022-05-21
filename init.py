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

### Init Game Functions ###

def game_init(current_word,difficulty):
    '''genrate the secret word to be displayed, the alphabet characters to guess, and lives left'''
    display_string = generate_display_string(current_word)
    character_list = generate_character_list()
    guesses_left = len(current_word)+difficulty
    return display_string,character_list,guesses_left

def generate_display_string(current_word):
    '''generates game string given current_word'''
    new_string = ''
    for i in current_word:
        new_string = new_string+"_ "
    return new_string

def generate_character_list():
    '''creates a list containing the guessed and unguessed characters ordered respectively'''
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    unguessed_characters = ''
    for i in alphabet_list:
        unguessed_characters = unguessed_characters + i + ' '
    guessed_characters = ''
    character_list = [unguessed_characters,guessed_characters]
    return character_list
