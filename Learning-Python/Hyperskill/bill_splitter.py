from random import randint

my_dict = {}
num_friends = int(input('Enter the number of friends joining (including you):\n'))

print('\nEnter the name of every friend (including you), each on a new line:')
for _ in range(num_friends):
    my_dict[input()] = 0

bill = float(input('\nEnter the total bill value:\n'))

for key in my_dict.keys():
    my_dict[key] = round(bill / num_friends, 2)

lucky_input = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
lucky_flag = lucky_input == 'Yes'

if lucky_flag:
    names = list(my_dict.keys())
    lucky_person = names[randint(0, num_friends - 1)]
    print(f'\n{lucky_person} is the lucky one!')
    for key, value in my_dict.items():
        if key != lucky_person:
            my_dict[key] = round(bill / (num_friends - 1), 2)
        else:
            my_dict[key] = 0
else:
    print('\nNo one is going to be lucky')

print('\n')
print(my_dict)