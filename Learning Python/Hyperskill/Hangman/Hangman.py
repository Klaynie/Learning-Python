import random

title = 'H A N G M A N'
user_message = 'Guess the word:'
outcome_messages = ['You survived!', 'You are hanged!']
word_list = ['python', 'java', 'kotlin', 'javascript']
word_to_guess = random.choice(word_list)
print(title)

input_ = input(user_message)
if input_ == word_to_guess:
    print(outcome_messages[0])
elif input_ != word_to_guess:
    print(outcome_messages[1])