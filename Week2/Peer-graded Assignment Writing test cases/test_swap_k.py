import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.

    def test_swap_k_empty_zero(self):
        """
        Test swap_k with empty list and k = 0 (boundry)
        """

        L = []
        L_expected = []

        a1.swap_k(L, 0)

        self.assertEqual(L, L_expected)

    def test_swap_k_full_zero(self):
        """
        Test swap_k with a list of numbers and k = 0
        """

        L = [1, 2, 3, 4, 5, 6]
        L_expected = [1, 2, 3, 4, 5, 6]

        a1.swap_k(L, 0)

        self.assertEqual(L, L_expected)

    def test_swap_k_full_max(self):
        """
        Test swap_k with a list of numbers and k = len(L)// 2
        """

        L = [1, 2, 3, 4, 5, 6]
        L_expected = [4, 5, 6, 1, 2, 3]

        a1.swap_k(L, 3)

        self.assertEqual(L, L_expected)

    def test_swap_k_inbetween_even(self):
        """
        Test swap_k with a list of even number and k = 2
        """

        L = [1, 2, 3, 4, 5, 6]
        L_expected = [5, 6, 3, 4, 1, 2]

        a1.swap_k(L, 2)

        self.assertEqual(L, L_expected)

    def test_swap_k_inbetween_odd(self):
        """
        Test swap_k with a list of odd numbers and k = 1
        """

        L = [1, 2, 3]
        L_expected = [3, 2, 1]

        a1.swap_k(L, 1)

        self.assertEqual(L, L_expected) 

        
    def test_swap_k_smallest_list(self):
        """
        Test swap_k with a list of two number and k = 1
        """

        L = [1, 2]
        L_expected = [2, 1]

        a1.swap_k(L, 1)

        self.assertEqual(L, L_expected)

if __name__ == '__main__':
    unittest.main(exit=False)
