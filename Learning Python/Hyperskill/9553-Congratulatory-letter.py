def congratulations(*names):
    print("Happy New Year! Take care of yourself and your loved ones!\nFor:")
    name_list = []
    for name in names:
        if ' ' in name:
            part = name.split()
            for name in part:
                name_list.append(name)
        elif ' ' not in name:
            name_list.append(name)
    for name in name_list:
       print(name)

congratulations("Alice", "Mike", "Roman Victoria")