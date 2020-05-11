column = int(input())
row = int(input())

if 2 <= row <= 7 and 2 <= column <= 7:
    print(8)
elif (row == 1 and (column == 1 or column == 8)) or (row == 8 and (column == 1 or column == 8)):
    print(3)
else:
    print(5)