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

if __name__ == '__main__':
    unittest.main()
