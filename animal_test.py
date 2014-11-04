import unittest

from animal import Animal


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("tiger", "DiviaLud", "male", 10, 150)
        self.animal2 = Animal("tiger", "DiviaLud", "male", 10, 175)

    def test_init(self):
        self.assertEqual("tiger", self.animal.species)
        self.assertEqual(120, self.animal.age)
        self.assertEqual("DiviaLud", self.animal.name)
        self.assertEqual("male", self.animal.gender)
        self.assertEqual(150, self.animal.weight)

    def test_eat(self):
        food_in_kilos = self.animal.eat()
        self.assertEqual(4.5, food_in_kilos)

    def test_grows(self):
        self.animal.grows()
        self.animal2.grows()
        self.assertEqual(121, self.animal.age)
        self.assertEqual(160, self.animal.weight)
        self.assertEqual(180, self.animal2.weight)

    def test_chance_of_dying(self):
        chance = self.animal.chance_of_dying()
        self.assertEqual(0.5, chance)


if __name__ == '__main__':
    unittest.main()
