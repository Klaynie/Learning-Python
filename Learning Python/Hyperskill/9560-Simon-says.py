def what_to_do(instructions):
    string_to_check = "Simon says"
    if string_to_check not in instructions:
        print("I won't do it!")
    else:
        print("I", instructions[:instructions.index(string_to_check)])

what_to_do(input())