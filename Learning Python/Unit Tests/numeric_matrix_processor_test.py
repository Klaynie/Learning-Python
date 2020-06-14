from unittest import mock
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
        result = [[1, 2, 3, 4, 5],\
                  [3, 2, 3, 2, 1],\
                  [8, 0, 9, 9, 1],\
                  [1, 3, 4, 5, 6]]
        self.assertEqual(get_matrix_input(number_of_rows), result)

    @mock.patch('Hyperskill.NumericMatrixProcessor.numeric_matrix_processor.input', create=True)
    def test_get_matrix_input_02(self, mocked_input):
        number_of_rows = 2
        mocked_input.side_effect = ['1 4 5', '4 5 5']
        result = [[1, 4, 5],\
                  [4, 5, 5]]
        self.assertEqual(get_matrix_input(number_of_rows), result)

class AddMatrixCases(TestCase):
    def test_matrix_addition_01(self):
        matrix_one = [[1, 2, 3, 4, 5],\
                      [3, 2, 3, 2, 1],\
                      [8, 0, 9, 9, 1],\
                      [1, 3, 4, 5, 6]]
        matrix_two = [[1, 1, 4, 4, 5],\
                      [4, 4, 5, 7, 8],\
                      [1, 2, 3, 9, 8],\
                      [1, 0, 0, 0, 1]]
        list_of_matrices = [matrix_one, matrix_two]
        result = [[2, 3, 7, 8, 10],\
                  [7, 6, 8, 9, 9],\
                  [9, 2, 12, 18, 9],\
                  [2, 3, 4, 5, 7]]
        self.assertEqual(add_matrices(list_of_matrices), result)
class MatrixCanBeAddedCases(TestCase):
    def test_matrix_can_be_added_01(self):
        matrix_one = [[1, 2, 3, 4, 5],\
                      [3, 2, 3, 2, 1],\
                      [8, 0, 9, 9, 1],\
                      [1, 3, 4, 5, 6]]
        matrix_two = [[1, 1, 4, 4, 5],\
                      [4, 4, 5, 7, 8],\
                      [1, 2, 3, 9, 8],\
                      [1, 0, 0, 0, 1]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertTrue(matrices_can_be_added(list_of_matrices))
    def test_matrix_can_be_added_02(self):
        matrix_one = [[1, 4, 5],\
                      [4, 5, 5]]
        matrix_two = [[0, 1, 0, 4, 5],\
                      [1, 7, 8, 9, 4],\
                      [1, 2, 3, 5, 6],\
                      [1, 3, 4, 3, 8]]
        list_of_matrices = [matrix_one, matrix_two]
        self.assertFalse(matrices_can_be_added(list_of_matrices))