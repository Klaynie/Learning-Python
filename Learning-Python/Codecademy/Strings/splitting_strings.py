authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = list()

for full_name in author_names:
    full_name_list = full_name.split()
    last_name = full_name_list[1]
    author_last_names.append(last_name)

print(author_last_names)