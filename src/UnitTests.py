import unittest
from calculator import Calculator


class Testing(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(5, 5), 10)
        self.assertEqual(self.calculator.result, 10)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(5, 5), 0)
        self.assertEqual(self.calculator.result, 0)

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
