import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEquals(calculator.result,0)

    def test_add_method_calculator(self):
        self.assertEqual(calculator.add(2,2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtraction_method_calculator(self):
        self.assertEqual(calculator.subtract(2,2), 0)
        self.assertEqual(calculator.result, 0)

    def test_division_method_calculator(self):
        self.assertEqual(calculator.divide(2, 2), 1)
        self.assertEqual(calculator.result, 1)

    def test_multiplication_method_calculator(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_squaring_method_calculator(self):
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_rooting_method_calculator(self):
        self.assertEqual(calculator.square(4), 2)
        self.assertEqual(calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
