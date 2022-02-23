import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Ralph Cajipe' work?"""
        formatted_name = get_formatted_name('ralph', 'cajipe')
        self.assertEqual(formatted_name, 'Ralph Cajipe')

    def test_first_last_middle_name(self):
        """Do names like 'Ralph Henrik Cajipe' work?"""
        formatted_name = get_formatted_name(
            'ralph', 'cajipe', 'henrik'
        )
        self.assertEqual(formatted_name, 'Ralph Henrik Cajipe')


if __name__ == '__main__':
    unittest.main()
