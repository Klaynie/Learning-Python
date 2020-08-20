def congratulations(*employees):
    print("Happy New Year! Take care of yourself and your loved ones!", "For:", *employees, sep="\n")

congratulations("Alice", "Mike", "Roman Victoria")