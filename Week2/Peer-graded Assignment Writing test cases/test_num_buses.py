import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    
    # Add your test methods for a1.num_buses here.

    def test_num_buses_boundry(self):
        """ Test num_buses with 0 smallest value and a boundry """

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    
    def test_num_buses_inbetween(self):
        """ Test num_buses with 20 a value between 0 and bus capacity"""

        actual = a1.num_buses(20)
        expected = 1
        self.assertEqual(expected, actual)
        
    
    def test_num_buses_maxcap(self):
        """ Test num_buses with 50 the value of bus capacity"""

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    
    def test_num_buses_smallest(self):
        """ Test num_buses with 51 a value larger by 1 from bus capacity"""

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
