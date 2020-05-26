import random

title = 'H A N G M A N'
user_message = 'Guess the word: '
outcome_messages = ['You survived!', 'You are hanged!']
word_list = ['python', 'java', 'kotlin', 'javascript']

def generate_word_to_guess():
    global word_list
    return random.choice(word_list)

def check_user_input(input_):
    global outcome_messages, word_to_guess
    if input_ == word_to_guess:
        return outcome_messages[0]
    return outcome_messages[1]

def generate_user_hint():
    global word_to_guess
    return word_to_guess[:3] + (len(word_to_guess) - 3) * '-'

print(title)
word_to_guess = generate_word_to_guess()
input_ = input(user_message + generate_user_hint())
print(check_user_input(input_))