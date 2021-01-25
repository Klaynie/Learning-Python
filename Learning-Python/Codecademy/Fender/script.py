import os
import csv
import json


def generate_file_path(file_name):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, file_name)


input_file = generate_file_path('passwords.csv')
compromised_users = []

with open(input_file, newline='') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])

output_file = generate_file_path('compromised_users.txt')

with open(output_file, 'w') as compromised_user_file:
    compromised_user_file.writelines(user + '\n' for user in compromised_users)

message = generate_file_path('boss_message.json')

with open(message, 'w') as boss_message:
    boss_message_dict = {}
    boss_message_dict['recipient'] = 'The Boss'
    boss_message_dict['message'] = 'Missin Success'
    json.dump(boss_message_dict, boss_message)

new_passwords = generate_file_path('new_passwords.csv')

with open(new_passwords, 'w', newline='') as new_passwords_obj:
    slash_null_sig = """
     _  _     ___   __  ____             
    / )( \   / __) /  \(_  _)            
    ) \/ (  ( (_ \(  O ) )(              
    \____/   \___/ \__/ (__)             
     _  _   __    ___  __ _  ____  ____  
    / )( \ / _\  / __)(  / )(  __)(    \ 
    ) __ (/    \( (__  )  (  ) _)  ) D ( 
    \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
            ____  __     __   ____  _  _ 
     ___   / ___)(  )   / _\ / ___)/ )( \\
    (___)  \___ \/ (_/\/    \\___ \) __ (
           (____/\____/\_/\_/(____/\_)(_/
     __ _  _  _  __    __                
    (  ( \/ )( \(  )  (  )               
    /    /) \/ (/ (_/\/ (_/\             
    \_)__)\____/\____/\____/
    """
    new_passwords_obj.write(slash_null_sig)