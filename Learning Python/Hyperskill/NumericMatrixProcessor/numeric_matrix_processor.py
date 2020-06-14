def get_row_and_column_numbers():
    number_of_rows, number_of_columns = (int(_) for _ in input().split())
    return number_of_rows, number_of_columns

def get_matrix_input(number_of_rows):
    result = []
    for row_counter in range(number_of_rows):
        row = [int(_) for _ in input().split()]
        result.append(row)
    return result

def matrix_calculator():
    result = []
    for _ in range(2):
        number_of_rows, number_of_columns = get_row_and_column_numbers()
        matrix = get_matrix_input(number_of_rows)
    result.append(matrix)
    print(matrix)