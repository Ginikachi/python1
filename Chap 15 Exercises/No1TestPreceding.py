## No 1 Tests Cases:

import unittest
import Exercise15

class TestDoublePreceding(unittest.TestCase):
    """ Tests for Exercise15.double_preceding."""

    def test_double_preceding_empty(self):
        """Test an empty list."""

        argument = []
        expected = []
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list is empty.")

    def test_double_preceding_one_item(self):
        """Test a one-item list."""

        argument = [5]
        expected = [0]
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list contains one item.")

    def test_double_preceding_two_items(self):
        """Test a two-item list."""

        argument = [2, 5]
        expected = [0, 4]
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list contains two items.")

    def test_double_preceding_multi_positive(self):
        """Test a list of positive values."""

        argument = [1, 2, 3]
        expected = [0, 2, 4]
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list contains only positive values.")

    def test_double_preceding_multi_negative(self):
        """Test a list of negative values."""
        argument = [-3, -2, -1]
        expected = [0, -6, -4]
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list contains only negative values.")

    def test_double_preceding_multi_zeros(self):
        """Test a list of zeros."""

        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list contains only zeros.")

    def test_double_preceding_multi_mix(self):
        """Test a list containing mixture of negative values, zeros and
        positive values."""

        argument = [-1, 0, 5, -6, 1, 0]
        expected = [0, -2, 0, 10, -12, 2]
        Exercise15.double_preceding(argument)
        self.assertEqual(expected, argument,
                         "The list contains a mixture of negative values,"
                         + "zeros and positive values.")

unittest.main()
