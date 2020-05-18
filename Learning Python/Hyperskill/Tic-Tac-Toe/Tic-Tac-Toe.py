cells = input("Enter cells:")
win_condition_x = 'XXX'
win_condition_o = 'OOO'
count_x = 0
count_o = 0
count_win_conditions = 0
count_x_wins = 0
count_o_wins = 0
error_game_states = ["Impossible"]
game_continues_state = ["Game not finished"]
game_final_states = ["X Wins", "O Wins", "Draw"]
keep_going = True

def check_new_field_input_is_valid(new_field_input):
    global cells
    if len(new_field_input) != 2:
        print("Please provide the correct amount of fields!")
        return False
    elif not new_field_input[0].isdigit() or not new_field_input[1].isdigit():
            print("You should enter numbers!")
            return False
    new_field_input[0], new_field_input[1] = int(new_field_input[0]), int(new_field_input[1])
    if new_field_input[0] < 1 or new_field_input[0] > 3 or new_field_input[1] < 1 or new_field_input[1] > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    else:
        cell_to_update = convert_user_input_to_cell(new_field_input)
        cell_content = return_cell_content(cell_to_update)
        if check_if_cell_is_occupied(cell_content):
            return False
        else:
            return True

def check_if_cell_is_occupied(cell_content):
    if cell_content != '_':
        print("This cell is occupied! Choose another one!")
        return True
    return False

def update_cell_with_x(cell_to_update):
    global cells
    cells = cells[:cell_to_update] + 'X' + cells[cell_to_update+1:]

def print_field():
    global cells
    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")

def convert_user_input_to_cell(new_field_input):
    if new_field_input == [1, 3]:
        return 0
    elif new_field_input == [1, 2]:
        return 3
    elif new_field_input == [1, 1]:
        return 6
    elif new_field_input == [2, 3]:
        return 1
    elif new_field_input == [2, 2]:
        return 4
    elif new_field_input == [2, 1]:
        return 7
    elif new_field_input == [3, 3]:
        return 2
    elif new_field_input == [3, 2]:
        return 5
    elif new_field_input == [3, 1]:
        return 8

def return_cell_content(cell_number):
    return cells[cell_number]

def convert_field_to_rows():
    return [cells[0]+cells[1]+cells[2], cells[3]+cells[4]+cells[5], cells[6]+cells[7]+cells[8]]

def convert_field_to_columns():
    return [cells[0]+cells[3]+cells[6], cells[1]+cells[4]+cells[7], cells[2]+cells[5]+cells[8]]

def convert_field_to_diagonals():
    return [cells[0]+cells[4]+cells[8], cells[6]+cells[4]+cells[2]]

def convert_field_to_states():
    rows = convert_field_to_rows()
    columns = convert_field_to_columns()
    diagonals = convert_field_to_diagonals()
    return [rows, columns, diagonals]

def count_symbols_on_field():
    global count_x, count_o
    for symbol in cells:
        if symbol == 'X':
            count_x += 1
        if symbol == 'O':
            count_o += 1

def count_field_states(field_states):
    global count_win_conditions, count_x_wins, count_o_wins
    for lists in field_states:
        for items in lists:
            if items == win_condition_x:
                count_x_wins += 1
                count_win_conditions += 1
            elif items == win_condition_o:
                count_o_wins += 1
                count_win_conditions += 1

print_field()
def game_loop():
    global keep_going
    while keep_going:
        new_field_input = input("Enter the coordinates: ").split()
        keep_going = not check_new_field_input_is_valid(new_field_input)
        if not keep_going:
            update_cell_with_x(convert_user_input_to_cell(new_field_input))
game_loop()
print_field()
#field_states = convert_field_to_states()

#count_symbols_on_field()
#count_field_states(field_states)

#if count_win_conditions > 1:
    #print("Impossible")
#elif count_o > count_x + 1 or count_x > count_o + 1:
    #print("Impossible")
#elif cells == '_________':
    #print("New Game")
#elif count_x_wins == 1:
    #print("X wins")
#elif count_o_wins == 1:
    #print("O wins")
#elif '_' in cells:
    #print('Game not finished')
#else:
    #print("Draw")