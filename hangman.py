'''
game loop for guessing:
need to display '_' for letters player has not guessed yet
need to keep track of amount of wrong guesses left and subtract when wrong
need player to be able to input letters

'''
import debug
import backend

game_start_button = input("Welcome to Animal Hangman: Press Any Button to Play:\n")
if game_start_button == "debug":
    debug.debug_mode() # debug mode to add words
    print('debug exited')

current_word = backend.retrieve_random_word()
print(current_word)
