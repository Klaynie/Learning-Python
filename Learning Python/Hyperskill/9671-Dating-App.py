potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"}, 
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"}, 
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]

def select_dates(list_):
    name_list = []
    for matches in list_:
        if check_date_list_item(matches) != None:
            name_list.append(check_date_list_item(matches))
    return ', '.join(name_list)

def check_date_list_item(matches):
    if matches['age'] > 30 and matches['city'] == 'Berlin' and 'art' in matches['hobbies']:
        return matches['name']
    return None

print(select_dates(potential_dates))