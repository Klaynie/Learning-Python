import random

title = 'H A N G M A N'
user_messages = ['Input a letter: ', 'Type "play" to play the game, "exit" to quit:']
play_keyword = 'play'
exit_keyword = 'exit'
outcome_messages = ['No improvements', 'No such letter in the word','You guessed the word!', 'You survived!', 'You are hanged!']
guardian_messages = ['You should input a single letter', 'It is not an ASCII lowercase letter', 'You already typed this letter']
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['python', 'java', 'kotlin', 'javascript']
placeholder_character = '-'
max_lives = 8
strikes = 0
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

def input_guardian(input_):
    global ascii_letters, guessed_letters
    if len(input_) != 1:
        print(guardian_messages[0])
        return False
    if input_ not in ascii_letters:
        print(guardian_messages[1])
        return False
    if input_ in guessed_letters:
        print(guardian_messages[2])
        return False
    return True

def input_handler(input_):
    global user_output_word, guessed_letters, correctly_guessed_letters, strikes
    if input_guardian(input_):
        add_letter_to_guessed_letters(input_)
        if is_letter_in_word_to_guess(input_):
            add_letter_to_corretcly_guessed_letters(input_)
            generate_user_output_word()
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
    print(outcome_messages[2])
    print(outcome_messages[3])
    print('\n')

def game_loop():
    global max_lives, strikes, user_output_word, guessed_letters, correctly_guessed_letters
    stay_in_game = True
    while stay_in_game:
        start_or_stop = input(user_messages[1])
        if start_or_stop == play_keyword:
            initiate_session()
            stay_in_session = True
            while stay_in_session:
                print('\n')
                print(user_output_word)
                input_handler(input(user_messages[0]))
                if strikes == max_lives:
                    stay_in_session = False
                    output_loss()
                elif word_to_guess == user_output_word:
                    stay_in_session = False
                    output_win()
        elif start_or_stop == exit_keyword:
            stay_in_game = False

#Start the Game
print(title)
game_loop()