import random

title = 'H A N G M A N'
user_messages = ['Input a letter: ', 'Thanks for playing!\nWe\'ll see how well you did in the next stage']
outcome_messages = ['No such letter in the word', 'You survived!', 'You are hanged!']
word_list = ['python', 'java', 'kotlin', 'javascript']
placeholder_character = '-'
max_tries = 8
current_tries = 0
correctly_guessed_letters = set()

def set_word_to_guess():
    global word_list
    return random.choice(word_list)

def is_letter_in_input(input_):
    word_to_guess_set
    return input_ in word_to_guess_set

def input_handler(input_):
    global user_output_word, correctly_guessed_letters
    if is_letter_in_input(input_):
        add_letter_to_corretcly_guessed_letters(input_)
        generate_user_output_word()
    else:
        print(outcome_messages[0])

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
    global max_tries, current_tries, user_output_word
    while current_tries <= max_tries:
        print('\n')
        print(user_output_word)
        input_handler(input(user_messages[0]))
        current_tries += 1
    print(user_messages[1])

#Setup Game Session Variables
word_to_guess = set_word_to_guess()
word_to_guess_set = generate_word_to_guess_set()
user_output_word = len(word_to_guess) * placeholder_character

#Start the Game
print(title)
game_loop()