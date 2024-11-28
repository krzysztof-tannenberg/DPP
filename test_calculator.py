import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        """Test dla funkcji add"""
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test dla funkcji subtract"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
