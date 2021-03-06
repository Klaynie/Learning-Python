from unittest import mock
from unittest.mock import patch, call
from unittest import TestCase
from Hyperskill.NumericMatrixProcessor.numeric_matrix_processor import *

class GetMatrixRowAndNumberCases(TestCase):
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_get_matrix_row_and_number_01(self, mocked_input):
        mocked_input.side_effect = ['4 5']
        result = (4, 5)
        self.assertEqual(get_row_and_column_numbers(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_get_matrix_row_and_number_02(self, mocked_input):
        mocked_input.side_effect = ['2 3']
        result = (2, 3)
        self.assertEqual(get_row_and_column_numbers(), result)
class GetMatrixInputCases(TestCase):
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_get_matrix_input_01(self, mocked_input):
        number_of_rows = 4
        mocked_input.side_effect = ['1 2 3 4 5', '3 2 3 2 1', '8 0 9 9 1', '1 3 4 5 6']
        result = [[1, 2, 3, 4, 5]\
                 ,[3, 2, 3, 2, 1]\
                 ,[8, 0, 9, 9, 1]\
                 ,[1, 3, 4, 5, 6]]
        self.assertEqual(get_matrix_input(number_of_rows), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_get_matrix_input_02(self, mocked_input):
        number_of_rows = 2
        mocked_input.side_effect = ['1 4 5', '4 5 5']
        result = [[1, 4, 5]\
                 ,[4, 5, 5]]
        self.assertEqual(get_matrix_input(number_of_rows), result)
class AddMatrixCases(TestCase):
    def test_matrix_addition_01(self):
        matrix_one = [[1, 2, 3, 4, 5]\
                     ,[3, 2, 3, 2, 1]\
                     ,[8, 0, 9, 9, 1]\
                     ,[1, 3, 4, 5, 6]]
        matrix_two = [[1, 1, 4, 4, 5]\
                     ,[4, 4, 5, 7, 8]\
                     ,[1, 2, 3, 9, 8]\
                     ,[1, 0, 0, 0, 1]]
        list_of_matrices = [matrix_one, matrix_two]
        result = [[2, 3, 7, 8, 10]\
                 ,[7, 6, 8, 9, 9]\
                 ,[9, 2, 12, 18, 9]\
                 ,[2, 3, 4, 5, 7]]
        self.assertEqual(add_matrices(list_of_matrices), result)
class MultiplyMatrixCases(TestCase):
    def test_matrix_multiplication_01(self):
        matrix_one = [[1, 7, 7]\
                     ,[6, 6, 4]\
                     ,[4, 2, 1]]
        matrix_two = [[3, 2, 4]\
                     ,[5, 5, 9]\
                     ,[8, 0, 10]]
        list_of_matrices = [matrix_one, matrix_two]
        result = [[94, 37, 137]\
                 ,[80, 42, 118]\
                 ,[30, 18, 44]]
        self.assertEqual(multiply_matrices(list_of_matrices), result)
    def test_matrix_multiplication_02(self):
        matrix_one = [[2, 4, 6]\
                     ,[1, 3, 5]]
        matrix_two = [[1, 2]\
                     ,[3, 4]\
                     ,[5, 6]]
        list_of_matrices = [matrix_one, matrix_two]
        result = [[44, 56]\
                 ,[35, 44]]
        self.assertEqual(multiply_matrices(list_of_matrices), result)
class TransposeMatrixCases(TestCase):
    def test_matrix_transpose_main_diagonal_01(self):
        matrix = [[1, 1, 1, 1]\
                 ,[2, 2, 2, 2]\
                 ,[3, 3, 3, 3]\
                 ,[4, 4, 4, 4]]
        result = [[1, 2, 3, 4]\
                 ,[1, 2, 3, 4]\
                 ,[1, 2, 3, 4]\
                 ,[1, 2, 3, 4]]
        self.assertEqual(transpose_main_diagonal(matrix), result)
    def test_matrix_transpose_main_diagonal_02(self):
        matrix = [[1, 7, 7]\
                 ,[6, 6, 4]\
                 ,[4, 2, 1]]
        result = [[1, 6, 4]\
                 ,[7, 6, 2]\
                 ,[7, 4, 1]]
        self.assertEqual(transpose_main_diagonal(matrix), result)
    def test_matrix_transpose_side_diagonal_01(self):
        matrix = [[1, 1, 1, -1]\
                 ,[2, 2, 2, -2]\
                 ,[3, 3, 3, -3]\
                 ,[4, 4, 4, -4]]
        result = [[-4, -3, -2, -1]\
                 ,[4, 3, 2, 1]\
                 ,[4, 3, 2, 1]\
                 ,[4, 3, 2, 1]]
        self.assertEqual(transpose_side_diagonal(matrix), result)
    def test_matrix_transpose_vertical_line_01(self):
        matrix = [[1, 2, 3, 4]\
                 ,[5, 6, 7, 8]\
                 ,[9, 10, 11, 12]\
                 ,[13, 14, 15, 16]]
        result = [[4, 3, 2, 1]\
                 ,[8, 7, 6, 5]\
                 ,[12, 11, 10, 9]\
                 ,[16, 15, 14, 13]]
        self.assertEqual(transpose_vertical_line(matrix), result)
    def test_matrix_transpose_horizontal_line_01(self):
        matrix = [[1, 2, 3, 4]\
                 ,[5, 6, 7, 8]\
                 ,[9, 10, 11, 12]\
                 ,[13, 14, 15, 16]]
        result = [[13, 14, 15, 16]\
                 ,[9, 10, 11, 12]\
                 ,[5, 6, 7, 8]\
                 ,[1, 2, 3, 4]]
        self.assertEqual(transpose_horizontal_line(matrix), result)
class MatrixCanBeAddedCases(TestCase):
    def test_matrix_can_be_added_01(self):
        matrix_one = [[1, 2, 3, 4, 5]\
                     ,[3, 2, 3, 2, 1]\
                     ,[8, 0, 9, 9, 1]\
                     ,[1, 3, 4, 5, 6]]
        matrix_two = [[1, 1, 4, 4, 5]\
                     ,[4, 4, 5, 7, 8]\
                     ,[1, 2, 3, 9, 8]\
                     ,[1, 0, 0, 0, 1]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertTrue(matrices_can_be_added(list_of_matrices))
    def test_matrix_can_be_added_02(self):
        matrix_one = [[1, 4, 5]\
                     ,[4, 5, 5]]
        matrix_two = [[0, 1, 0, 4, 5]\
                     ,[1, 7, 8, 9, 4]\
                     ,[1, 2, 3, 5, 6]\
                     ,[1, 3, 4, 3, 8]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertFalse(matrices_can_be_added(list_of_matrices))
class MatrixCanBeMultipliedCases(TestCase):
    def test_matrix_can_be_multiplied_01(self):
        matrix_one = [[1, 2, 3, 4, 5]\
                     ,[3, 2, 3, 2, 1]\
                     ,[8, 0, 9, 9, 1]\
                     ,[1, 3, 4, 5, 6]]
        matrix_two = [[1, 1, 4, 4, 5]\
                     ,[4, 4, 5, 7, 8]\
                     ,[1, 2, 3, 9, 8]\
                     ,[1, 0, 0, 0, 1]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertFalse(matrices_can_be_multiplied(list_of_matrices))
    def test_matrix_can_be_multiplied_02(self):
        matrix_one = [[1, 4, 5]\
                     ,[4, 5, 5]]
        matrix_two = [[0, 1, 0, 4, 5]\
                     ,[1, 7, 8, 9, 4]\
                     ,[1, 2, 3, 5, 6]\
                     ,[1, 3, 4, 3, 8]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertFalse(matrices_can_be_multiplied(list_of_matrices))
    def test_matrix_can_be_multiplied_03(self):
        matrix_one = [[1, 7, 7]\
                     ,[6, 6, 4]\
                     ,[4, 2, 1]]
        matrix_two = [[3, 2, 4]\
                     ,[5, 5, 9]\
                     ,[8, 0, 10]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertTrue(matrices_can_be_multiplied(list_of_matrices))
    def test_matrix_can_be_multiplied_04(self):
        matrix_one = [[2, 4, 6]\
                     ,[1, 3, 5]]
        matrix_two = [[1, 2]\
                     ,[3, 4]\
                     ,[5, 6]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertTrue(matrices_can_be_multiplied(list_of_matrices))
class ConvertMatrixToStringCases(TestCase):
    def test_convert_matrix_2_string_01(self):
        matrix = [[2, 3, 7, 8, 10]\
                 ,[7, 6, 8, 9, 9]\
                 ,[9, 2, 12, 18, 9]\
                 ,[2, 3, 4, 5, 7]]
        result = '2 3 7 8 10\n'\
                 '7 6 8 9 9\n'\
                 '9 2 12 18 9\n'\
                 '2 3 4 5 7'
        self.assertEqual(convert_matrix_2_string(matrix), result)
class PrintCorrectOutcomeTest(TestCase):
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_addition_01(self, mocked_input):
        mocked_input.side_effect = ['1'
                                   ,'4 5', '1 2 3 4 5', '3 2 3 2 1', '8 0 9 9 1', '1 3 4 5 6'\
                                   ,'4 5', '1 1 4 4 5', '4 4 5 7 8', '1 2 3 9 8', '1 0 0 0 1']
        result = '2 3 7 8 10\n'\
                 '7 6 8 9 9\n'\
                 '9 2 12 18 9\n'\
                 '2 3 4 5 7'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_multiply_by_constant_01(self, mocked_input):
        mocked_input.side_effect = ['2'
                                   ,'2 2', '1.5 7.0', '6.0 5.0'\
                                   ,'0.5']
        result = '0.75 3.5\n'\
                 '3.0 2.5'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_multiply_matrices_02(self, mocked_input):
        mocked_input.side_effect = ['3'
                                   ,'3 3', '1 7 7', '6 6 4', '4 2 1'\
                                   ,'3 3', '3 2 4', '5 5 9', '8 0 10']
        result = '94 37 137\n'\
                 '80 42 118\n'\
                 '30 18 44'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_multiply_matrices_02(self, mocked_input):
        mocked_input.side_effect = ['3'
                                   ,'2 3', '2 4 6', '1 3 5'\
                                   ,'3 2', '1 2', '3 4', '5 6']
        result = '44 56\n'\
                 '35 44'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_transpose_matrix_01(self, mocked_input):
        mocked_input.side_effect = ['4'
                                   ,'1'
                                   ,'4 4'
                                   ,'1 1 1 1', '2 2 2 2', '3 3 3 3', '4 4 4 4']
        result = '1 2 3 4\n'\
                 '1 2 3 4\n'\
                 '1 2 3 4\n'\
                 '1 2 3 4'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_transpose_matrix_02(self, mocked_input):
        mocked_input.side_effect = ['4'
                                   ,'2'
                                   ,'4 4'
                                   ,'1 1 1 -1', '2 2 2 -2', '3 3 3 -3', '4 4 4 -4']
        result = '-4 -3 -2 -1\n'\
                 '4 3 2 1\n'\
                 '4 3 2 1\n'\
                 '4 3 2 1'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_transpose_matrix_03(self, mocked_input):
        mocked_input.side_effect = ['4'
                                   ,'3'
                                   ,'4 4'
                                   ,'1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16']
        result = '4 3 2 1\n'\
                 '8 7 6 5\n'\
                 '12 11 10 9\n'\
                 '16 15 14 13'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_transpose_matrix_04(self, mocked_input):
        mocked_input.side_effect = ['4'
                                   ,'4'
                                   ,'4 4'
                                   ,'1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16']
        result = '13 14 15 16\n'\
                 '9 10 11 12\n'\
                 '5 6 7 8\n'\
                 '1 2 3 4'
        self.assertEqual(input_handler(), result)
    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_print_transpose_matrix_05(self, mocked_input):
        mocked_input.side_effect = ['4'
                                   ,'1'
                                   ,'3 3'
                                   ,'1 7 7', '6 6 4', '4 2 1']
        result = '1 6 4\n'\
                 '7 6 2\n'\
                 '7 4 1'
        self.assertEqual(input_handler(), result)
class MultiplyMatrixByConstantCases(TestCase):
    def test_matrix_by_constant_multiplication_01(self):
        matrix = [[1, 2, 3]\
                 ,[4, 5, 6]\
                 ,[7, 8, 9]]
        constant = 3
        result = [[3, 6, 9]\
                 ,[12, 15, 18]\
                 ,[21, 24, 27]]
        self.assertEqual(multiply_matrix_by_constant(matrix, constant), result)
    def test_matrix_by_constant_multiplication_02(self):
        matrix = [[1, 2, 3]\
                 ,[4, 5, 6]]
        constant = 0
        result = [[0, 0, 0]\
                 ,[0, 0, 0]]
        self.assertEqual(multiply_matrix_by_constant(matrix, constant), result)
    def test_matrix_by_constant_multiplication_03(self):
        matrix = [[1.5, 7.0]\
                 ,[6.0, 5.0]]
        constant = 0.5
        result = [[0.75, 3.5]\
                 ,[3.0, 2.5]]
        self.assertEqual(multiply_matrix_by_constant(matrix, constant), result)
class DeterimanteCalculationCases(TestCase):
    def test_determinante_calculation_01(self):
        matrix = [[1, 7, 7]\
                 ,[6, 6, 4]\
                 ,[4, 2, 1]]
        result = -16
        self.assertEqual(calculate_determinante(matrix), result)
    def test_determinante_calculation_02(self):
        matrix = [[1, 2, 3, 4, 5]\
                 ,[4, 5, 6, 4, 3]\
                 ,[0, 0, 0, 1, 5]\
                 ,[1, 3, 9, 8, 7]\
                 ,[5, 8, 4, 7, 11]]
        result = 191
        self.assertEqual(calculate_determinante(matrix), result)
    def test_determinante_calculation_03(self):
        matrix = [[8, 2, 3]\
                 ,[1, 0, 1]\
                 ,[2, 5, 1]]
        result = -23
        self.assertEqual(calculate_determinante(matrix), result)
    def test_determinante_calculation_04(self):
        matrix = [[8, 2, 3]\
                 ,[1, 0, 1]\
                 ,[2, 5, 1]]
        result = -23
        self.assertEqual(calculate_determinante(matrix), result)
    def test_determinante_calculation_05(self):
        matrix = [[1, -4]\
                 ,[-2, 5]]
        result = -3
        self.assertEqual(calculate_determinante(matrix), result)