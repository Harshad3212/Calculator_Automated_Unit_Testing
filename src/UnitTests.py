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


if __name__ == '__main__':
    unittest.main()
