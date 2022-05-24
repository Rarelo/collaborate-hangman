#fix the lives not draining
#add game over check/message

import debug
import init
import runtime

difficulty = 1 #the number of guesses the player gets + word length

game_start_button = input("Welcome to Animal Hangman: Press Any Button to Play: ")
if game_start_button == "debug":
    debug.debug_mode() # debug mode to add words
    print('debug exited')

current_word = init.retrieve_random_word()
print(current_word)

display_string,character_list,guesses_left = init.game_init(current_word,difficulty)
game_running = True

#make a check to not allow the same letter guessed in a single game

while game_running:
    runtime.game_display_round(display_string,character_list,guesses_left)
    letter = runtime.guess_a_character(character_list)
    #print(letter)
    #print(display_string)
    #print(character_list)
    #print(guesses_left)
    display_string,character_list,guesses_left = runtime.mutate_game_variabels(current_word,display_string,character_list,guesses_left,letter)
    #game over/victory check here
