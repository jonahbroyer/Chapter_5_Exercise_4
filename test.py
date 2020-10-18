import unittest
from main import fibonacci


class TestFib(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fibonacci(10), 55)


if __name__ == '__main__':
    unittest.main()
