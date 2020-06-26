import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEquals(self.calculator.result,0)



    def test_add_method_calculator(self):
        test_data = CsvReader ('/src/Unit Test Addition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'],row['Value 2'] ), float (row['Result']))
            self.assertEqual(self.calculator.result, float (row['Result']))




    def test_subtraction_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_multiplication_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_squaring_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_rooting_method_calculator(self):
        self.assertEqual(self.calculator.rooting(4), 2)
        self.assertEqual(self.calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
