def what_to_do(instructions):
    string_to_check = "Simon says"
    if string_to_check not in instructions or not (instructions.startswith(string_to_check) or instructions.endswith(string_to_check)):
        return "I won't do it!"
    return_string = "I "
    if instructions.startswith(string_to_check):
        return_string += instructions[len(string_to_check):].strip()
    elif instructions.endswith(string_to_check):
        return_string += instructions[:instructions.index(string_to_check)].strip()
    return return_string

print(what_to_do("make Simon says a wish"))