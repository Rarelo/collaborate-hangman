import json
import backend

### Debug Functions ###

def debug_mode():
    '''game debug mode/loop that is used to add new words'''
    debug_mode = True
    while debug_mode == True:
        user_input = input("Enter a Word to add to the Dictionary or type 'exit' to exit:\n")
        if user_input != "exit":
            save_word_to_json(user_input)
        else:
            return None

def save_word_to_json(user_input):
    '''pulls the old words to the json file and adds the new user input word'''
    try: current_words = backend.retrieve_words()
    except: current_words = ["foobar"]
    current_words.append(user_input)
    with open("hangman.json","w") as json_file:
        json.dump(current_words,json_file)
    return None
