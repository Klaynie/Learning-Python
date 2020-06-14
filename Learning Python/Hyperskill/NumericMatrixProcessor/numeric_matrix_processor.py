def convert_matrix_2_string(matrix):
    result = ''
    for row_counter, row in enumerate(matrix, 1):
        for item_counter, item in enumerate(row, 1):
            if item_counter < len(row):
                result += str(item)
                result += ' '
            else:
                result += str(item)
        if row_counter < len(matrix):
            result += '\n'
    return result

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

def matrix_addition(number_of_matrices=2):
    result = []
    list_of_matrices = []
    for _ in range(number_of_matrices):
        number_of_rows, number_of_columns = get_row_and_column_numbers()
        matrix = get_matrix_input(number_of_rows)
        list_of_matrices.append(matrix)
    if matrices_can_be_added(list_of_matrices):
        result = add_matrices(list_of_matrices)
    return result

def multiply_matrix_by_constant(matrix, constant):
    result = []
    for row in matrix:
        result_row = [constant * item for item in row]
        result.append(result_row)
    return result

def get_constant():
    return int(input())

def matrix_by_constant_multiplication():
    result = []
    number_of_rows, number_of_columns = get_row_and_column_numbers()
    matrix = get_matrix_input(number_of_rows)
    constant = get_constant()
    result = multiply_matrix_by_constant(matrix, constant)
    return result
    
def matrix_calculator():
    #result = matrix_addition()
    result = matrix_by_constant_multiplication()
    if result == []:
        result = 'ERROR'
    else:
        result = convert_matrix_2_string(result)
    return result

if __name__ == "__main__":
    print(matrix_calculator())