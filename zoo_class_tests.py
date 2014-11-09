import unittest
from animal import Animal
from zoo_class import Zoo


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zz = Zoo(10, 10000)
        self.male_kitten = Animal('tiger', 'DiviaLud', 'male', 10, 150)
        self.female_kitten = Animal('tiger', 'DiviaLuda', 'female', 10, 150)
        self.female_ape = Animal('ape', 'Chico', 'female', 15, 35)
        self.zz.animals.append(self.male_kitten)
        self.zz.animals.append(self.female_kitten)
        self.zz.animals.append(self.female_ape)

    def test_init(self):
        self.assertIn(self.male_kitten, self.zz.animals)
        self.assertEqual(self.zz.capacity, 10)
        self.assertEqual(self.zz.budget, 10000.0)
        self.assertNotEqual(self.zz.animals, ['panda'])

    def test_accomodate_animal(self):
        self.male_tiger = Animal('tiger', 'tiger', 'male', 10, 150)
        self.assertRaises(ValueError, self.zz.accomodate_animal, (self.male_kitten))
        self.zz.accomodate_animal(self.male_tiger)
        self.assertIn(self.male_tiger, self.zz.animals)

    def test_have_money(self):
        self.zz.budget = 0
        self.assertFalse(self.zz.have_money())
        self.zz.budget = 1
        self.assertTrue(self.zz.have_money())

    def test_win_money(self):
        before_money = self.zz.budget
        self.zz.win_money()
        after_money = self.zz.budget
        self.assertGreaterEqual(after_money, before_money)

    def test_make_animals(self):
        self.zz.make_animals(self.male_kitten, self.female_kitten)
        self.assertTrue(self.female_kitten.pregnant)

    def test_feed_animals(self):
        self.zz.feed_animals()
        self.assertEqual(self.zz.budget, 9959.8)

    def test_check_for_dead_animals(self):
        count = len(self.zz.animals)
        self.zz.animals[0].age = self.zz.animals[0].info.life_expectancy() * 12 + 13
        self.zz.check_for_dead_animals()
        self.assertEqual(count - 1, len(self.zz.animals))

    # def test_update_pregnancy_born(self):
    #     self.female_kitten.pregnant = True
    #     self.female_kitten.pregnancy = self.female_kitten.info.gestation_period
    #     self.zz.update_pregnancy(self.female_kitten)

    #Needs more functionality
    # def test_check_if_reproduction(self):
    #     self.zz.animals.append('Female hourse')
    #     self.zz.animals.append('male hourse')
    #     self.zz.check_if_reproduction()
    #     self.assertIn('little house', self.zz.animals)

if __name__ == '__main__':
    unittest.main()
