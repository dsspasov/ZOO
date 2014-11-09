import unittest
from simulate_zoo import SimulateZoo
from zoo_class import Zoo
from animal import Animal


class SimulateZooTests(unittest.TestCase):
    def setUp(self):
        zoo = Zoo()
        zoo.budget = 10000
        self.animal = Animal("tiger", "Pesho", "male", 4, 100)
        self.animal2 = Animal("tiger", "Penka", "female", 3, 78)
        self.zoo.animals.append(self.animal)
        self.zoo.animals.append(self.animal2)   

    def test_init(self):
        pass

    def test_See_animals(self):
        pass
if __name__ == '__main__':
    unittest.main()
