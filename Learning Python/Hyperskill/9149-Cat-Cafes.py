cafe_list = []
while True:
    input_ = input()
    if input_ == 'MEOW':
        break
    split_input = input_.split()
    cafe_list.append(split_input)

max_number = 0
cafe = ''
for item in cafe_list:
    if int(item[1]) > max_number:
        max_number = int(item[1])
        cafe = item[0]

print(cafe)