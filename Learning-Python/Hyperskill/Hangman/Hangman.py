import random
from enum import IntEnum
import re

class OutcomeMessage(IntEnum):
    NO_IMPROVEMENTS = 0
    NO_SUCH_LETTER = 1
    YOU_GUESSED_RIGHT = 2

class GuardianMessage(IntEnum):
    ONLY_SINGLE_LETTER = 0
    ONLY_ASCII = 1
    ALREADY_TYPED = 2

title = 'H A N G M A N'
user_messages = ['Input a letter: ', 'Type "play" to play the game, "exit" to quit:']
play_keyword = 'play'
exit_keyword = 'exit'
outcome_messages = ['No improvements', 'No such letter in the word','You guessed the word!', 'You survived!', 'You are hanged!'] #Enum
guardian_messages = ['You should input a single letter', 'It is not an ASCII lowercase letter', 'You already typed this letter'] #Enum
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['python', 'java', 'kotlin', 'javascript']
placeholder_character = '-'
max_lives = 8 #Ausgeben

# Ab hier sind es Dinge, die sich in der Laufzeit ändern
strikes = 0 #Strikes anzeigen
correctly_guessed_letters = set()
guessed_letters = set()
word_to_guess_set = set()
word_to_guess = ''
user_output_word = ''


def set_word_to_guess():
    global word_list
    return random.choice(word_list)

def is_letter_in_word_to_guess(input_):
    return input_ in word_to_guess_set

def print_guardian_message(int_enum): # Generalisieren auf Print Message
    print(guardian_messages[int_enum])

def has_more_than_one_letter(input_):
    return len(input_) != 1

def input_guardian(input_): # Maximal 3 Values, sonst DTO/Type
    global ascii_letters, guessed_letters
    result = False

    if has_more_than_one_letter(input_):
        print_guardian_message(GuardianMessage.ONLY_SINGLE_LETTER) # Generalisieren auf Print Message
    elif input_ not in ascii_letters:
        print_guardian_message(GuardianMessage.ONLY_ASCII)
    elif input_ in guessed_letters:
        print_guardian_message(GuardianMessage.ALREADY_TYPED)
    else:
        result = True

    return result # Immer nur ein Return Value

def input_handler(input_):
    global user_output_word, guessed_letters, correctly_guessed_letters, strikes
    if input_guardian(input_):
        add_letter_to_guessed_letters(input_)
        if is_letter_in_word_to_guess(input_):
            add_letter_to_corretcly_guessed_letters(input_)
            generate_user_output_word2()
        else:
            strikes += 1
            print(outcome_messages[1])
    else:
        return None

def add_letter_to_corretcly_guessed_letters(letter):
    global correctly_guessed_letters
    correctly_guessed_letters.add(letter)

def add_letter_to_guessed_letters(letter):
    global guessed_letters
    guessed_letters.add(letter)

def convert_list_to_string(list_):
    return ''.join(list_)

def generate_user_output_word():
    global word_to_guess, user_output_word, correctly_guessed_letters
    user_output_word = list(user_output_word)
    word_iterator = 0
    for letter in word_to_guess:
        if letter in correctly_guessed_letters:
            user_output_word[word_iterator] = letter
        word_iterator += 1
    user_output_word = convert_list_to_string(user_output_word)
    return user_output_word

def generate_user_output_word2():
    global word_to_guess, user_output_word, correctly_guessed_letters, placeholder_character, ascii_letters
    regular_expr = get_regular_expression_for_user_output(user_output_word, correctly_guessed_letters)
    result = re.sub(regular_expr, placeholder_character, word_to_guess)
    user_output_word = result
    return result # Immer nur ein Return Value

def get_regular_expression_for_user_output(user_output_word, correctly_guessed_letters):
    result = '[' + ascii_letters + ']'
    for letter in correctly_guessed_letters:
        result = result.replace(letter, '')
    return result

def generate_word_to_guess_set():
    global word_to_guess
    return set(word_to_guess)

def initiate_session():
    global strikes, correctly_guessed_letters, word_to_guess, word_to_guess_set, user_output_word, guessed_letters
    strikes = 0
    correctly_guessed_letters.clear()
    guessed_letters.clear()
    word_to_guess = set_word_to_guess()
    word_to_guess_set = generate_word_to_guess_set()
    user_output_word = len(word_to_guess) * placeholder_character

def output_loss():
    print(outcome_messages[4])
    print('\n')

def output_win():
    print(word_to_guess)
    print(outcome_messages[OutcomeMessage.YOU_GUESSED_RIGHT])
    print(outcome_messages[3])
    print('\n')

def print_user_output_word():
    print('\n')
    print(user_output_word)

def session_loop():
    initiate_session()
    stay_in_session = True
    while stay_in_session:
        print_user_output_word() #Always print user output word after guessing
        input_handler(input(user_messages[0]))
        if strikes == max_lives:
            stay_in_session = False
            output_loss() #Always print user output word after guessing
        elif word_to_guess == user_output_word:
            stay_in_session = False
            output_win() #Always print user output word after guessing

def main_loop():
    stay_in_game = True
    while stay_in_game:
        start_or_stop = input(user_messages[1])
        if start_or_stop == play_keyword:
            session_loop()
        elif start_or_stop == exit_keyword:
            stay_in_game = False

def game_loop():
    global max_lives, strikes, user_output_word, guessed_letters, correctly_guessed_letters
    main_loop()
    

#Start the Game
print(title)
game_loop()