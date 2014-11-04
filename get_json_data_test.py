import unittest

from get_json_data import GetJsonData


class TestGetJsonData(unittest.TestCase):

    def setUp(self):
        self.new_json = GetJsonData("database.json")

    def test_get_species_type(self):
        species = ['turtle', 'ape', 'lion', 'tiger', 'pengin']
        for item in species:
            self.assertIn(item, self.new_json.get_species_type())

    def test_get_life_expectancy(self):
        self.assertEqual(20, self.new_json.get_life_expectancy("tiger"))

    def test_get_food_type(self):
        self.assertEqual("carnivore", self.new_json.get_food_type("tiger"))

    def test_get_gestation_period(self):
        self.assertEqual(6, self.new_json.get_gestation_period("tiger"))

    def test_get_newborn_weight(self):
        self.assertEqual(1, self.new_json.get_newborn_weight("tiger"))

    def test_get_weight_age(self):
        self.assertEqual(10, self.new_json.get_weight_age("tiger"))

    def test_get_food_weight(self):
        self.assertEqual(0.03, self.new_json.get_food_weight("tiger"))

    def test_get_average_weight(self):
        self.assertEqual(180, self.new_json.get_average_weight("tiger"))

if __name__ == '__main__':
    unittest.main()
