## No 4 tests Cases:

import unittest
import Exercise15

class TestIsSorted(unittest.TestCase):
    """ Tests for Exercise15.is_sorted."""

    def test_is_sorted_empty(self):
        """Test an empty list."""

        argument = []
        expected = True
        result = Exercise15.is_sorted(argument)
        self.assertEqual(expected, result, "The list is empty.")

    def test_is_sorted_one_item(self):
        """Test a list of one item."""

        argument = [2]
        expected = True
        result = Exercise15.is_sorted(argument)
        self.assertEqual(expected, result, "The list has one item.")

    def test_is_sorted_duplicates(self):
        """Test a sorted list with duplcate values."""

        argument = [1, 2, 2, 3]
        expected = True
        result = Exercise15.is_sorted(argument)
        self.assertEqual(expected, result,
                               "The list has duplicate values.")

    def test_is_sorted_not_sorted(self):
        """Test an unsorted list."""
        
        argument = [1, 3, 1]
        expected = False
        result = Exercise15.is_sorted(argument)
        self.assertEqual(expected, result, "The list is not sorted.")

        
unittest.main()
