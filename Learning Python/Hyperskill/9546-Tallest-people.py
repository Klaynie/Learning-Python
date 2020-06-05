def tallest_people(**names):
    tallest_people_list = []
    for name, height in names.items():
        if height == max(names.values()):
            tallest_people_list.append(f"{name} : {height}")
    tallest_people_list.sort()
    for item in tallest_people_list:
        print(item)

tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)