import unittest
from calculator import Calculator


class Testing(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(5, 5), 10)
        self.assertEqual(calculator.result, 10)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(5, 5), 0)
        self.assertEqual(calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
