import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_empty(self):
        """ test stock_price_summary with an empty list """

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual,expected) 

    def test_stock_price_zero(self):
        """ test stock_price_summary with a list of one element 0"""

        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(actual,expected)

    def test_stock_price_postive(self):
        """ test stock_price_summary with a list of only postive"""

        actual = a1.stock_price_summary([0.01,0.03,0,0.10,0])
        expected = (0.14, 0)
        self.assertEqual(actual,expected)


    def test_stock_price_negative(self):
        """ test stock_price_summary with a list of only negative"""

        actual = a1.stock_price_summary([-0.02,-0.14,-0.01])
        expected = (0, -0.17)
        self.assertEqual(actual,expected)

    def test_stock_price_both(self):
        """ test stock_price_summary with a list of both postive and negative"""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual,expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
