
### Base Game Functions ###

def display_guessed_characters(character_list):
    print("Unguessed characters: "+ character_list[0])
    if character_list[1] != '':
        print("Guessed characters: "+ character_list[1])


def game_display_round(display_string,character_list,guesses_left):
    print()
    print("Word: " + display_string)
    display_guessed_characters(character_list)
    print("Guesses left: " +str(guesses_left))
