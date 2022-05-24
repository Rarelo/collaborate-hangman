import init
### Base Game Functions ###

###intra guessing display

def display_guessed_characters(character_list):
    print("Unguessed characters: "+ character_list[0])
    if character_list[1] != '':
        print("Guessed characters: "+ character_list[1])


def game_display_round(display_string,character_list,guesses_left):
    '''prints the interface shown between guesses'''
    print()
    print("Word: " + display_string)
    display_guessed_characters(character_list)
    print("Guesses left: " +str(guesses_left))

### player guessing

def guess_a_character(character_list):
    '''function that allows the player to input a letter to guess and then verifies it is a valid input'''
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    guessed_characters = character_list[1]
    #print(guessed_characters)
    guessing = True
    while guessing:
        checks_passed = 0 #checks checks_passed needs to equal 2 for the function to break the loop
        letter = input("Enter a character to guess: ")
        if len(letter) == 1:
            checks_passed += 1
        alphabet_check = 0 #check to make sure the input is a letter in the alphabet
        for i in alphabet_list:
            if letter == i:
                alphabet_check += 1
        if alphabet_check == 1:
            checks_passed += 1
        #test to prevent guessing the same letter
        repeat_letter = False
        for i in guessed_characters:
            if letter == i:
                repeat_letter = True
        if checks_passed == 2 and repeat_letter != True:
            guessing = False
        else:
            print("That's not an unguessed single letter!")
        #print("guessing",guessing)
        #print("checks_passed",checks_passed)
        #print("alphabet_check",alphabet_check)
    return letter

### processing each player guess

def mutate_game_variabels(current_word,display_string,character_list,guesses_left,letter):
    '''checks if the players input is in the current_word and acts accordingly'''
    character_list = regenerate_character_list(character_list,letter)
    display_string = handle_display_string(current_word,display_string,letter,guesses_left)
    return display_string,character_list,guesses_left
    #display string

def handle_display_string(current_word,display_string,letter,guesses_left):
    '''checks if display string should be mutated and mutates it accordingly'''
    try:
        position_in_string = current_word.index(letter)*2 #gives an error if the letter is not in the string
        display_string = mutate_string(position_in_string,display_string,letter)
    #the following to catch any letters that appear mutliple times
        position_in_string = current_word.index(letter)
        #must remove first character instance from current_word:
        current_word = mutate_string(position_in_string,current_word,0)
        multiple_occuranies_test = handle_display_string(current_word,display_string,letter,guesses_left)
        if display_string != multiple_occuranies_test:
            display_string = multiple_occuranies_test #multiple_occuranies_test currency broken
    except:
        #selected letter not in the string
        #display_string does not need to be changed
        guesses_left = guesses_left -1
    return display_string

def mutate_string(position_in_string,string,character_to_replace):
    '''mutates and returns a string because apparently assignment isn't a thing'''
    string_list = list(string)
    string_list[position_in_string] = character_to_replace
    return regenerate_display_string(string_list)

def regenerate_display_string(display_string_list):
    '''generates game string given display_string_list'''
    new_string = ''
    for i in display_string_list:
        new_string = new_string+str(i)
    return new_string

def regenerate_character_list(character_list,letter):
    '''takes in character list and guessed letter and updates the character list'''
    unguessed_temp_list = character_list[0].rsplit()
    guessed_temp_list = character_list[1].rsplit()
    unguessed_temp_list.remove(letter)
    guessed_temp_list.append(letter)
    new_unguessed_characters = ''
    for i in unguessed_temp_list:
        new_unguessed_characters = new_unguessed_characters + i + ' '
    new_guessed_characters = ''
    for i in guessed_temp_list:
        new_guessed_characters = new_guessed_characters + i + ' '
    character_list = [new_unguessed_characters,new_guessed_characters]
    return character_list


### victory/game over
