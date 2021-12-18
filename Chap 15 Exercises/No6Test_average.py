## No 6 tests cases:

import unittest
import Exercise15


class TestAverage(unittest.TestCase):
    """ Tests for Exercise15.average."""

    def test_average_empty(self):
        """ Test an empty list."""

        argument = Exercise15.average([])
        expected = None
        self.assertEqual(argument, expected, "The list is empty.")

    def test_average_allNone(self):
        """Test a list wth only missing values."""

        argument = Exercise15.average([None])
        expected = None
        self.assertEqual(argument, expected, "The list has only missing value.")

    def test_average_one_item(self):
        """Test a list of one item."""

        argument = Exercise15.average([20])
        expected = 20.0
        self.assertEqual(argument, argument, "The list has one item.")

    def test_average_noNone(self):
        """Test a list with no missing value."""

        argument = Exercise15.average([20, 30])
        expected = 25.0
        self.assertEqual(argument, expected, "The list has no missing value.")

    def test_average_someNone(self):
        """Test a list with missing value represented as None."""

        argument = Exercise15.average([None, 20, 30])
        expected = 25.0
        self.assertEqual(argument, expected, "The list has missing value.")

unittest.main()        
    
