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

