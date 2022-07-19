import unittest
import lotto


class UnitTests(unittest.TestCase):
    
    def setUp(self):
        self.number_of_bill=lotto.Bill.set_number_of_bill(4)
        self.numb=lotto.Bill.valid_numbers([8, 19, 45, 34, 47, 24, 67, 78, 79, 89])
        self.route=lotto.Bill.route_type("Bari")
        self.combination=lotto.Bill.new_combination("terno")
        
    def test_distinct_classes(self):
        actual = lotto.Bill is not lotto.Ticket
        expected = True
        self.assertEqual(actual, expected, 'Expected Bill class to be a distinct class from the Ticket class.')
        
    def test_set_number_of_bill(self):
        actual= self.number_of_bill
        expected = 4
        self.assertEqual(actual, expected, "expected number of bill between 1 and 5")
        
    def test_numbers_1_90(self):
        actual = len(self.numb)
        expected = 10
        self.assertEqual(actual, expected, "expected len valid_numbers == 10")
        
    def test_route_type(self):
        

if __name__ == "__main__":
    unittest.main()