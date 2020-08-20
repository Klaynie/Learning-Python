from enum import IntEnum
import numpy as np

class Keyword(IntEnum):
    EXIT = 0
    ADD = 1
    MULTI_BY_CONST = 2
    MATRIX_MULTI = 3
    TRANSPOSE = 4
    DETERMINANT = 5
    INVERSE = 6

class Transpose(IntEnum):
    MAIN_DIAGONAL = 1
    SIDE_DIAGONAL = 2
    VERTICAL_LINE = 3
    HORIZONTAL_LINE = 4

class UserMessage(IntEnum):
    ERROR = 0
    MENU = 1
    CHOICE = 2
    ADD_MATIRX_SIZE_1 = 3
    ENTER_MATRIX_1 = 4
    ADD_MATIRX_SIZE_2 = 5
    ENTER_MATRIX_2 = 6
    MATIRX_SIZE = 7
    ENTER_MATRIX = 8
    ENTER_CONSTANT = 9
    RESULT = 10
    TRANSPOSE = 11

keywords = ['EXIT']
user_messages = ['The operation cannot be performed.'
                ,'1. Add matrices\n'\
                 '2. Multiply matrix by a constant\n'\
                 '3. Multiply matrices\n'\
                 '4. Transpose matrix\n' \
                 '5. Calculate a determinant\n' \
                 '6. Inverse matrix\n' \
                 '0. Exit'
                ,'Your choice: '
                ,'Enter size of first matrix: '
                ,'Enter first matrix:'
                ,'Enter size of second matrix: '
                ,'Enter second matrix:'
                ,'Enter size of matrix: '
                ,'Enter matrix:'
                ,'Enter constant: '
                ,'The result is:'
                ,'1. Main diagonal\n'\
                 '2. Side diagonal\n'\
                 '3. Vertical line\n'\
                 '4. Horizontal line']

def convert_matrix_2_string(matrix):
    if matrix == []:
        result = []
    else:
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

def get_matrix_dimensions(list_of_matrices):
    result = []
    for matrix in list_of_matrices:
        result.append((len(matrix), len(matrix[0])))
    return result

def matrices_can_be_added(list_of_matrices):
    result = True
    dimensions = get_matrix_dimensions(list_of_matrices)
    for i in range(len(dimensions)):
        for j in range(len(dimensions)):
            if dimensions[0][j] != dimensions[i][j]:
                result = False
    return result

def get_row_and_column_numbers(message=None):
    number_of_rows, number_of_columns = (int(_) for _ in input(message).split())
    return number_of_rows, number_of_columns

def get_matrix_input(number_of_rows, message=None):
    result = []
    print(message)
    for row_counter in range(number_of_rows):
        raw_row = input().split()
        row = []
        for item in raw_row:
            temp_item = item
            if temp_item.replace('-','').isdigit():
                row.append(int(item))
            else:
                row.append(float(item))
        result.append(row)
    return result

def get_matrices_for_calculation():
    list_of_matrices = []
    n_row_first, n_column_first = get_row_and_column_numbers(user_messages[UserMessage.ADD_MATIRX_SIZE_1])
    first_matrix = get_matrix_input(n_row_first, user_messages[UserMessage.ENTER_MATRIX_1])
    list_of_matrices.append(first_matrix)
    n_row_second, n_column_second = get_row_and_column_numbers(user_messages[UserMessage.ADD_MATIRX_SIZE_2])
    second_matrix = get_matrix_input(n_row_second, user_messages[UserMessage.ENTER_MATRIX_2])
    list_of_matrices.append(second_matrix)
    return list_of_matrices

def matrix_addition():
    result = []
    list_of_matrices = get_matrices_for_calculation()
    if matrices_can_be_added(list_of_matrices):
        result = add_matrices(list_of_matrices)
    return result

def multiply_matrix_by_constant(matrix, constant):
    result = []
    for row in matrix:
        result_row = [constant * item for item in row]
        result.append(result_row)
    return result

def get_constant(message=None):
    result = input(message)
    if result.isdigit():
        result = int(result)
    else:
        result = float(result)
    return result

def get_single_matrix_data():
    result = []
    number_of_rows, number_of_columns = get_row_and_column_numbers(user_messages[UserMessage.MATIRX_SIZE])
    result = get_matrix_input(number_of_rows, user_messages[UserMessage.ENTER_MATRIX])
    return result

def matrix_by_constant_multiplication():
    result = []
    matrix = get_single_matrix_data()
    constant = get_constant(user_messages[UserMessage.ENTER_CONSTANT])
    result = multiply_matrix_by_constant(matrix, constant)
    return result

def multiply_matrices(list_of_matrices):
    result = []
    dimensions = get_matrix_dimensions(list_of_matrices)
    for i in range(dimensions[0][0]):
        row = []
        for k in range(dimensions[1][1]):
            figure = 0
            for j in range(dimensions[0][1]):
                figure += list_of_matrices[0][i][j] * list_of_matrices[1][j][k]
            row.append(figure)
        result.append(row)
    return result

def matrices_can_be_multiplied(list_of_matrices):
    result = True
    dimensions = []
    for matrix in list_of_matrices:
        dimensions.append((len(matrix), len(matrix[0])))
    if dimensions[0][1] != dimensions[1][0]:
        result = False
    return result

def matrix_multiplication():
    result = []
    list_of_matrices = get_matrices_for_calculation()
    if matrices_can_be_multiplied(list_of_matrices):
        result = multiply_matrices(list_of_matrices)
    return result

def get_menu_choice():
    return int(input(user_messages[UserMessage.CHOICE]))

def transpose_horizontal_line(matrix):
    result = []
    for i in range(len(matrix) - 1, -1, -1):
        row = matrix[i]
        result.append(row)
    return result

def transpose_vertical_line(matrix):
    result = matrix
    for row in result:
        row.reverse()
    return result

def transpose_side_diagonal(matrix):
    result = []
    for i in range(len(matrix) - 1, -1, -1):
        row = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            row.append(matrix[j][i])
        result.append(row)
    return result

def transpose_main_diagonal(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        result.append(row)
    return result

def transpose_matrix():
    result = []
    print('\n')
    print(user_messages[UserMessage.TRANSPOSE])
    action = get_menu_choice()
    matrix = get_single_matrix_data()
    if action == Transpose.MAIN_DIAGONAL:
        result = transpose_main_diagonal(matrix)
    elif action == Transpose.SIDE_DIAGONAL:
        result = transpose_side_diagonal(matrix)
    elif action == Transpose.VERTICAL_LINE:
        result = transpose_vertical_line(matrix)
    elif action == Transpose.HORIZONTAL_LINE:
        result = transpose_horizontal_line(matrix)
    return result

def calculate_determinante(matrix):
    matrix_array = np.array(matrix)
    result = np.linalg.det(matrix_array)
    return int(round(result))


def determinante_calculation():
    result = 0
    matrix = get_single_matrix_data()
    result = calculate_determinante(matrix)
    return result

def calculate_inverse(matrix):
    matrix_array = np.array(matrix)
    result = np.linalg.inv(matrix_array)
    return result
    

def inverse_calculation():
    result = []
    matrix = get_single_matrix_data()
    result = calculate_inverse(matrix)
    return result

def input_handler():
    result = None
    action = get_menu_choice()
    if action == Keyword.ADD:
        result = convert_matrix_2_string(matrix_addition())
    elif action == Keyword.MULTI_BY_CONST:
        result = convert_matrix_2_string(matrix_by_constant_multiplication())
    elif action == Keyword.MATRIX_MULTI:
        result = convert_matrix_2_string(matrix_multiplication())
    elif action == Keyword.TRANSPOSE:
        result = convert_matrix_2_string(transpose_matrix())
    elif action == Keyword.DETERMINANT:
        result = determinante_calculation()
    elif action == Keyword.INVERSE:
        result = convert_matrix_2_string(inverse_calculation())
    elif action == Keyword.EXIT:
        result = keywords[Keyword.EXIT]
    return result

def calculator_loop():
    global keywords, user_messages
    keep_going = True
    while keep_going:
        print(user_messages[UserMessage.MENU])
        result = input_handler()
        if result == keywords[Keyword.EXIT]:
            keep_going = False
        elif result == []:
            print(user_messages[UserMessage.ERROR])
            print('\n')
        else:
            print(user_messages[UserMessage.RESULT])
            print(result)
            print('\n')
        

if __name__ == "__main__":
    calculator_loop()