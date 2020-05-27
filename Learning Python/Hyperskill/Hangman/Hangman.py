import random

title = 'H A N G M A N'
user_messages = ['Input a letter: ']
outcome_messages = ['No improvements', 'No such letter in the word','You guessed the word!', 'You survived!', 'You are hanged!']
word_list = ['python', 'java', 'kotlin', 'javascript']
placeholder_character = '-'
max_lives = 8
strikes = 0
correctly_guessed_letters = set()
keep_going = True

def set_word_to_guess():
    global word_list
    return random.choice(word_list)

def is_letter_in_word_to_guess(input_):
    return input_ in word_to_guess_set

def input_handler(input_):
    global user_output_word, correctly_guessed_letters, strikes
    if is_letter_in_word_to_guess(input_) and input_ not in correctly_guessed_letters:
        add_letter_to_corretcly_guessed_letters(input_)
        generate_user_output_word()
    elif is_letter_in_word_to_guess(input_) and input_ in correctly_guessed_letters:
        strikes += 1
        print(outcome_messages[0])
    else:
        strikes += 1
        print(outcome_messages[1])

def add_letter_to_corretcly_guessed_letters(letter):
    correctly_guessed_letters.add(letter)

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

def game_loop():
    global max_lives, strikes, user_output_word, keep_going
    while keep_going:
        print('\n')
        print(user_output_word)
        input_handler(input(user_messages[0]))
        if strikes == max_lives:
            keep_going = False
            print(outcome_messages[4])
        elif word_to_guess == user_output_word:
            keep_going = False
            print(outcome_messages[2])
            print(outcome_messages[3])

#Setup Game Session Variables
word_to_guess = set_word_to_guess()
word_to_guess_set = generate_word_to_guess_set()
user_output_word = len(word_to_guess) * placeholder_character

#Start the Game
print(title)
game_loop()