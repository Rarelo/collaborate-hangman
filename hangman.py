'''
game loop for guessing:
allow player to input a letter
mutate display_string,character_list from player guess
subtract a life if wrong and game over when guesses = 0

'''
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
runtime.game_display_round(display_string,character_list,guesses_left)
