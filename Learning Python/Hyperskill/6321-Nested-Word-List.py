text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

input_length = int(input())
output_list = []
for list_ in text:
    for item in list_:
        if len(item) <= input_length:
            output_list.append(item)

print(output_list)