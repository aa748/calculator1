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
        print('Addition Test')
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'],row['Value 2'] ), float (row['Result']))
            self.assertEqual(self.calculator.result, float (row['Result']))

    def test_subtraction_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        print ('Subtraction Test')
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


    def test_division_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        print('Division Test')
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


    def test_multiplication_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        print('Multiplication Test')
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squaring_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        print('Squaring Test')
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_rooting_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        print ('Square Root Test')
        pprint(test_data)

        for row in test_data:
            #if self.calculator.result == float(row['Result']):
                self.assertEqual(self.calculator.rooting(row['Value 1']), float(row['Result']))
                self.assertEqual(self.calculator.result, float(row['Result']))
'''
 elif self.calculator.result != float(row['Result']):
                    self.assertEqual(self.calculator.rooting(row['Value 1']), float(row['Result']))
                    self.assertEqual(self.calculator.result, float(row['Result']))
'''





if __name__ == '__main__':
    unittest.main()
