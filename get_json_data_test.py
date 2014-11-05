import unittest

from get_json_data import GetJsonData


class TestGetJsonData(unittest.TestCase):

    def setUp(self):
        self.new_json = GetJsonData("database.json", "tiger")

    def test_life_expectancy(self):
        self.assertEqual(20, self.new_json.life_expectancy())

    def test_food_type(self):
        self.assertEqual("carnivore", self.new_json.food_type())

    def test_gestation_period(self):
        self.assertEqual(6, self.new_json.gestation_period())

    def test_newborn_weight(self):
        self.assertEqual(1, self.new_json.newborn_weight())

    def test_gained_weight_for_month(self):
        self.assertEqual(10, self.new_json.gained_weight_for_month())

    def test_food_for_weight(self):
        self.assertEqual(0.03, self.new_json.food_for_weight())

    def test_average_weight(self):
        self.assertEqual(180, self.new_json.average_weight())

if __name__ == '__main__':
    unittest.main()
