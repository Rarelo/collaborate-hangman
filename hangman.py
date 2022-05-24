#fix the lives not draining
#add game over check/message

import debug
import init
import runtime

def test_for_victory(current_word,display_string):
    game_running = True
    new_current_word = ""
    for i in current_word:
        new_current_word += i+" "
    #print(new_current_word)
    #print(display_string[0])
    #print(new_current_word == display_string[0])
    if new_current_word == display_string[0]:
        game_running = False
        print(" ")
        print("You Win!")
        return game_running
    return game_running

difficulty = 3 #the number of guesses the player gets + word length

game_start_button = input("Welcome to Animal Hangman: Press Any Button to Play: ")
if game_start_button == "debug":
    debug.debug_mode() # debug mode to add words
    print('debug exited')

current_word = init.retrieve_random_word()
#print(current_word)

display_string,character_list,guesses_left = init.game_init(current_word,difficulty)
game_running = True

#make a check to not allow the same letter guessed in a single game

while game_running:
    #function below keeps finding display_string as a tuple on occasion so have to make it output a corrected version
    display_string = runtime.game_display_round(display_string,character_list,guesses_left)
    letter = runtime.guess_a_character(character_list)
    #print(letter)
    #print(display_string)
    #print(character_list)
    #print(guesses_left)
    display_string,character_list,guesses_left = runtime.mutate_game_variabels(current_word,display_string,character_list,guesses_left,letter)
    try:
        game_running = test_for_victory(current_word,display_string)
    except:
        display_string = display_string[0]
        try:
            game_running = test_for_victory(current_word,display_string)
        except:
            display_string = display_string[0]
            try:
                game_running = test_for_victory(current_word,display_string)
            except:
                display_string = display_string[0]
                game_running = test_for_victory(current_word,display_string)
    if guesses_left == 0:
        game_running = False
        print(" ")
        print("You Lose!")
        print("The word was: "+str(current_word))
