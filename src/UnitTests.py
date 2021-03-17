import unittest
from calculator import Calculator


class Testing(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
