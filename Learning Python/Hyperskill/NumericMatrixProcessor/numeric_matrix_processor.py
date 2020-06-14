def add_matrices(list_of_matrices):
    result = []
    for row in list_of_matrices[0]:
        result_row = [0 for item in row]
        result.append(result_row)
    matrix_counter = 0
    for matrix in list_of_matrices:
        for i in range(len(matrix)):
            for j in range(len(row)):
                result[i][j] += list_of_matrices[matrix_counter][i][j]
        matrix_counter += 1
    return result

def matrices_can_be_added(list_of_matrices):
    result = True
    dimensions = []
    for matrix in list_of_matrices:
        dimensions.append((len(matrix), len(matrix[0])))
    for i in range(len(dimensions)):
        for j in range(len(dimensions)):
            if dimensions[0][j] != dimensions[i][j]:
                result = False
    return result

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
    list_of_matrices = []
    for _ in range(2):
        number_of_rows, number_of_columns = get_row_and_column_numbers()
        matrix = get_matrix_input(number_of_rows)
        list_of_matrices.append(matrix)
    if matrices_can_be_added(list_of_matrices):
        result = add_matrices(list_of_matrices)
    else:
        result = 'ERROR'

matrix_one = [[1, 4, 5],\
                [4, 5, 5]]
matrix_two = [[0, 1, 0, 4, 5],\
                [1, 7, 8, 9, 4],\
                [1, 2, 3, 5, 6],\
                [1, 3, 4, 3, 8]]
list_of_matrices = [matrix_one, matrix_two]
print(matrices_can_be_added(list_of_matrices))