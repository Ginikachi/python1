import unittest
import Exercise15

class TestAllPrefixes(unittest.TestCase):
    """Tests for all_prefixes."""

    def test_empty(self):
        """Test the empty string."""

        argument = Exercise15.all_prefixes('')
        expected = set()
        self.assertEqual(expected, argument, 'Argument is empty string.')

    def test_single_letter(self):
        """Test a one-character string."""

        argument = Exercise15.all_prefixes('x')
        expected = {'x'}
        self.assertEqual(expected, argument, 'Argument is single letter.')

    def test_word(self):
        """Test a word with unique letters."""

        argument = Exercise15.all_prefixes('water')
        expected = {'w', 'wa', 'wat', 'wate', 'water'}
        self.assertEqual(expected, argument,
                         'Argument is word with unique letters.')

    def test_multiple(self):
        """Test a word with multiple occurences of the first letter."""

        argument = Exercise15.all_prefixes('puppet')
        expected = {'p', 'pu', 'pup', 'pupp', 'puppe', 'puppet'}
        self.assertEqual(expected, argument,
                         'First letter occurs multiple times')

unittest.main()
