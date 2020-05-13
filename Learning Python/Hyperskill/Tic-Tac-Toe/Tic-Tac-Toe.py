cells = input("Enter cells:")
print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")

row_1 = cells[0]+cells[1]+cells[2]
row_2 = cells[3]+cells[4]+cells[5]
row_3 = cells[6]+cells[7]+cells[8]

column_1 = cells[0]+cells[3]+cells[6]
column_2 = cells[1]+cells[4]+cells[7]
column_3 = cells[2]+cells[5]+cells[8]

diagonal_1 = cells[0]+cells[4]+cells[8]
diagonal_2 = cells[6]+cells[4]+cells[2]

win_condition_x = 'XXX'
win_condition_o = 'OOO'

if cells == '_________':
    print("New Game")
elif row_1 == win_condition_x:
    print("X wins")
elif row_2 == win_condition_x:
    print("X wins")
elif row_3 == win_condition_x:
    print("X wins")
elif column_1 == win_condition_x:
    print("X wins")
elif column_2 == win_condition_x:
    print("X wins")
elif column_3 == win_condition_x:
    print("X wins")
elif diagonal_1 == win_condition_x:
    print("X wins")
elif diagonal_2 == win_condition_x:
    print("X wins")
elif row_1 == win_condition_o:
    print("O wins")
elif row_2 == win_condition_o:
    print("O wins")
elif row_3 == win_condition_o:
    print("O wins")
elif column_1 == win_condition_o:
    print("O wins")
elif column_2 == win_condition_o:
    print("O wins")
elif column_3 == win_condition_o:
    print("O wins")
elif diagonal_1 == win_condition_o:
    print("O wins")
elif diagonal_2 == win_condition_o:
    print("O wins")