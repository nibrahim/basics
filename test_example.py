import unittest

import example

class TestBasic(unittest.TestCase):
    def test_single(self):
        self.assertEqual(example.capital("Noufal"), 1)

    def test_multiple(self):
        self.assertEqual(example.capital("Noufal Ibrahim"), 2)

    def test_none(self):
        self.assertEqual(example.capital("noufal ibrahim"), 0)

if __name__ == "__main__":
    unittest.main()
        
