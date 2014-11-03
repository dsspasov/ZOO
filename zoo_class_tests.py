import unittest
from zoo_class import Zoo


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zz = Zoo()
        self.zz.animals.append('trutle')
        self.zz.capacity = 10
        self.zz.budget = 10000.0

    def test_init(self):
        self.assertEqual(self.zz.animals, ['turtle'])
        self.assertEqual(self.zz.capacity, 10)
        self.assertEqual(self.zz.budget, 10000.0)

if __name__ == '__main__':
    unittest.main()
