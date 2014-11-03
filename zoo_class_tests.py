import unittest
from zoo_class import Zoo


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zz = Zoo(10, 10000)

    def test_init(self):
        self.zz.animals.append('turtle')
        self.assertEqual(self.zz.animals, ['turtle'])
        self.assertEqual(self.zz.capacity, 10)
        self.assertEqual(self.zz.budget, 10000.0)
        self.assertNotEqual(self.zz.animals, ['panda'])

    def test_accomodate_animal(self):
        self.zz.accomodate_animal('rabbit')
        self.assertIn('rabbit', self.zz.animals)

    def test_win_money(self):
        before_money = self.zz.budget
        self.zz.win_money()
        after_money = self.zz.budget
        self.assertGreaterEqual(after_money, before_money)

    def test_pay_expanditures(self):
        before_pay = self.zz.budget
        self.zz.pay_expanditures()
        after_pay = self.zz.budget
        self.assertLessEqual(after_pay, before_pay)

    #Needs more functionality
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
