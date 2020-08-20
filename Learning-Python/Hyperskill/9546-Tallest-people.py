def tallest_people(**people):
    print('\n'.join(f'{name} : {people[name]}' for name in sorted(people)
                    if people[name] == max(people.values())))

tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)