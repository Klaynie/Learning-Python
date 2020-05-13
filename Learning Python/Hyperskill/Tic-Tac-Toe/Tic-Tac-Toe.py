cells = input("Enter cells:")
print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")

row_1 = cells[0]+cells[1]+cells[2]
row_2 = cells[3]+cells[4]+cells[5]
row_3 = cells[6]+cells[7]+cells[8]

rows = [row_1, row_2, row_3]

column_1 = cells[0]+cells[3]+cells[6]
column_2 = cells[1]+cells[4]+cells[7]
column_3 = cells[2]+cells[5]+cells[8]

columns = [column_1, column_2, column_3]

diagonal_1 = cells[0]+cells[4]+cells[8]
diagonal_2 = cells[6]+cells[4]+cells[2]

diagonals = [diagonal_1, diagonal_2]

field_states = [rows, columns, diagonals]

win_condition_x = 'XXX'
win_condition_o = 'OOO'

count_x = 0
count_o = 0
count_win_conditions = 0
count_x_wins = 0
count_o_wins = 0

for symbol in cells:
    if symbol == 'X':
        count_x += 1
    if symbol == 'O':
        count_o += 1

for lists in field_states:
    for items in lists:
        if items == win_condition_x:
            count_x_wins += 1
            count_win_conditions += 1
        elif items == win_condition_o:
            count_o_wins += 1
            count_win_conditions += 1

if count_win_conditions > 1:
    print("Impossible")
elif count_o > count_x + 1 or count_x > count_o + 1:
    print("Impossible")
elif cells == '_________':
    print("New Game")
elif count_x_wins == 1:
    print("X wins")
elif count_o_wins == 1:
    print("O wins")
elif '_' in cells:
    print('Game not finished')
else:
    print("Draw")