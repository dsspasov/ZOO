import unittest

from animal import Animal


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("tiger", 10, "DiviaLud", "male", 150)

    def test_init(self):
        self.assertEqual("tiger", self.animal.species)
        self.assertEqual(10, self.animal.age)
        self.assertEqual("DiviaLud", self.animal.name)
        self.assertEqual("male", self.animal.gender)
        self.assertEqual(150, self.animal.weight)

    def test_eat(self):
        pass

    def test_grows(self):
        self.animal.grows()
        self.assertEqual(11, self.animal.age)
        self.assertEqual(151, self.animal.weight)

    def test_die(self):
        pass

if __name__ == '__main__':
    unittest.main()
