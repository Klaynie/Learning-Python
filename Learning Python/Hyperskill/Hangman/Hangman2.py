import random
from enum import IntEnum
import re

class GameSession():

    def __init__(self):
        self.strikes = 0
        self.correctly_guessed_letters = set()
        self.guessed_letters = set()
        self.word_to_guess = set_word_to_guess(word_list)
        self.word_to_guess_set = set(self.word_to_guess)
        self.user_output_word = len(self.word_to_guess) * placeholder_character

    def add_letter_to_guessed_letters(self, letter):
        self.guessed_letters.add(letter)

    def add_letter_to_corretcly_guessed_letters(self, letter):
        self.correctly_guessed_letters.add(letter)

    def is_letter_in_word_to_guess(self, letter):
        return letter in self.word_to_guess_set

    def update_user_output_word(self, word):
        self.user_output_word = word

class UserMessage(IntEnum):
    INPUT_LETTER = 0
    KEYWORD_PROMPT = 1

class Keyword(IntEnum):
    PLAY = 0
    EXIT = 1

class OutcomeMessage(IntEnum):
    NO_SUCH_LETTER = 0
    GUESSED_RIGHT = 1
    SURVIVED = 2
    HANGED = 3

class GuardianMessage(IntEnum):
    ONLY_SINGLE_LETTER = 0
    ONLY_ASCII = 1
    ALREADY_TYPED = 2

title = 'H A N G M A N'
keywords = ['play', 'exit']
user_messages = ['Input a letter: ', f'Type "{keywords[Keyword.PLAY]}" to play the game, "{keywords[Keyword.EXIT]}" to quit:']
outcome_messages = ['No such letter in the word','You guessed the word!', 'You survived!', 'You are hanged!']
guardian_messages = ['You should input a single letter', 'It is not an ASCII lowercase letter', 'You already typed this letter']
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['python', 'java', 'kotlin', 'javascript']
placeholder_character = '-'
max_lives = 8

def set_word_to_guess(word_list):
    return random.choice(word_list)

def has_more_than_one_letter(input_):
    return len(input_) != 1

def input_guardian(input_, game_session):
    result = False

    if has_more_than_one_letter(input_):
        print(guardian_messages[GuardianMessage.ONLY_SINGLE_LETTER])
    elif input_ not in ascii_letters:
        print(guardian_messages[GuardianMessage.ONLY_ASCII])
    elif input_ in game_session.guessed_letters:
        print(guardian_messages[GuardianMessage.ALREADY_TYPED])
    else:
        result = True

    return result

def input_handler(input_, game_session):
    if input_guardian(input_, game_session):
        game_session.add_letter_to_guessed_letters(input_)
        if game_session.is_letter_in_word_to_guess(input_):
            game_session.add_letter_to_corretcly_guessed_letters(input_)
            game_session.update_user_output_word(generate_user_output_word(game_session))
        else:
            game_session.strikes += 1
            print(outcome_messages[OutcomeMessage.NO_SUCH_LETTER])
    else:
        return None

def generate_user_output_word(game_session):
    regular_expr = get_regular_expression_for_user_output(game_session.user_output_word, game_session.correctly_guessed_letters)
    return re.sub(regular_expr, placeholder_character, game_session.word_to_guess)

def get_regular_expression_for_user_output(user_output_word, correctly_guessed_letters):
    result = '[' + ascii_letters + ']'
    for letter in correctly_guessed_letters:
        result = result.replace(letter, '')
    return result

def output_loss():
    print('\n')
    print(outcome_messages[OutcomeMessage.HANGED])
    print('\n')

def output_win():
    print('\n')
    print(outcome_messages[OutcomeMessage.GUESSED_RIGHT])
    print(outcome_messages[OutcomeMessage.SURVIVED])
    print('\n')

def print_session_close(game_session):
    print('\n')
    print(game_session.user_output_word)
    if game_session.strikes == max_lives:
        output_loss()
    elif game_session.user_output_word == game_session.word_to_guess:
        output_win()

def session_over_condition(game_session):
    result = False
    if game_session.strikes == max_lives:
        result = True
    elif game_session.user_output_word == game_session.word_to_guess:
        result = True
    return result

def session_loop():
    game_session = GameSession()
    stay_in_session = True
    while stay_in_session:
        print('\n')
        print(game_session.user_output_word)
        input_handler(input(user_messages[UserMessage.INPUT_LETTER]), game_session)
        if session_over_condition(game_session):
            print_session_close(game_session)
            stay_in_session = False

def main_loop():
    stay_in_game = True
    while stay_in_game:
        start_or_stop = input(user_messages[UserMessage.KEYWORD_PROMPT])
        if start_or_stop == keywords[Keyword.PLAY]:
            session_loop()
        elif start_or_stop == keywords[Keyword.EXIT]:
            stay_in_game = False

def game_loop():
    global keywords, user_messages, guardian_messages, ascii_letters, word_list, placeholder_character, max_lives
    main_loop()

#Start the Game
print(title)
game_loop()