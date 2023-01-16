import unittest
from calculator import solve


class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(solve(2, 4, "+"), 6)

    def test_dif(self):
        self.assertEqual(solve(2, 4, "-"), -2)

    def test_mul(self):
        self.assertEqual(solve(2, 4, "*"), 8)

    def test_div(self):
        self.assertEqual(solve(2, 4, "/"), 0.5)

    def test_pow(self):
        self.assertEqual(solve(2, 4, "^"), 16)

    def test_mod(self):
        self.assertEqual(solve(5, 3, "%"), 2)


if __name__ == "__main__":
    unittest.main()
