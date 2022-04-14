import unittest
from city_functions import get_formatted_city_country


class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do City, Country inputs like Tokyo, Japan work?"""
        city_country = get_formatted_city_country('tokyo', 'japan')
        self.assertEqual(city_country, "Tokyo, Japan")

    def test_city_country_population(self):
        """Do inputs like Tokyo, Japan - population 13.96 million work?"""
        city_country = get_formatted_city_country('tokyo', 'japan',
                                                  '13,960,000')
        self.assertEqual(city_country,
                         "Tokyo, Japan - Population 13,960,000")


if __name__ == '__main__':
    unittest.main()
