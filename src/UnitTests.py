import unittest
from CsvReader import CsvReader
from calculator import Calculator

test_data = CsvReader('/src/UnitTestAll.csv').data


class Testing(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        for row in test_data:
            self.assertEqual(self.calculator.add(row['avalue1'], row['avalue2']), int(row['aresult']))
            self.assertEqual(self.calculator.result, int(row['aresult']))

    def test_subtract_method_calculator(self):
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['svalue1'], row['svalue2']), int(row['subresult']))
            self.assertEqual(self.calculator.result, int(row['subresult']))

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25)
        self.assertEqual(self.calculator.result, 25)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(5, 5), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.result, 25)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.squareroot(25), 5)
        self.assertEqual(self.calculator.result, 5)


if __name__ == '__main__':
    unittest.main()
