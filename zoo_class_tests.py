import unittest
from animal import Animal
from zoo_class import Zoo


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zz = Zoo(10, 10000)
        self.male_kitten = Animal("tiger", "DiviaLud", "male", 10, 150)
        self.female_kitten = Animal("tiger", "DiviaLuda", "female", 10, 150)
        self.zz.animals.append(self.male_kitten)
        self.zz.animals.append(self.female_kitten)

    def test_init(self):
        self.assertIn(self.male_kitten, self.zz.animals)
        self.assertEqual(self.zz.capacity, 10)
        self.assertEqual(self.zz.budget, 10000.0)
        self.assertNotEqual(self.zz.animals, ['panda'])

    def test_accomodate_animal(self):
        self.zz.accomodate_animal(self.male_kitten)
        self.assertIn(self.male_kitten, self.zz.animals)

    def test_win_money(self):
        before_money = self.zz.budget
        self.zz.win_money()
        after_money = self.zz.budget
        self.assertGreaterEqual(after_money, before_money)

    def test_make_animals(self):
        self.zz.make_animals(self.male_kitten, self.female_kitten)
        self.assertTrue(self.female_kitten.pregnant)

    def test_born_animal(self):
        self.female_kitten.pregnant = True
        self.female_kitten.pregnancy = self.female_kitten.info.gestation_period
        self.assertTrue(self.zz.born_animal)

    def test_get_food_type(self):
        self.assertEqual(self.male_kitten.info.food_type(), "carnivore")

    def test_pay_expanditures(self):
        before_pay = self.zz.budget
        self.zz.pay_expanditures()
        after_pay = self.zz.budget
        self.assertLessEqual(after_pay, before_pay)


    # Needs more functionality
    # def test_check_for_dead_animals(self):
    #     self.zz.animals.append('horse')
    #     self.zz.animals['hourse'].age = 'hourse'.life_expectacy + 1
    #     self.zz.check_for_dead_animals()
    #     self.assertNotIn('horse', self.zz.animals)

    #Needs more functionality
    # def test_check_if_reproduction(self):
    #     self.zz.animals.append('Female hourse')
    #     self.zz.animals.append('male hourse')
    #     self.zz.check_if_reproduction()
    #     self.assertIn('little house', self.zz.animals)

if __name__ == '__main__':
    unittest.main()
