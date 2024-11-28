import unittest
from shared.operations import addition, subtraction, multiplication, division


class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(5, 3), 8, "5 + 3 should equal 8")
        self.assertEqual(addition(-2, 5), 3, "-2 + 5 should equal 3")
        self.assertEqual(addition(0, 0), 0, "0 + 0 should equal 0")
        self.assertEqual(addition(1.5, 2.5), 4.0, "1.5 + 2.5 should equal 4.0")

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2, "5 - 3 should equal 2")
        self.assertEqual(subtraction(-2, 5), -7, "-2 - 5 should equal -7")
        self.assertEqual(subtraction(0, 0), 0, "0 - 0 should equal 0")
        self.assertEqual(subtraction(1.5, 0.5), 1.0, "1.5 - 0.5 should equal 1.0")

    def test_multiplication(self):
        self.assertEqual(multiplication(5, 3), 15, "5 * 3 should equal 15")
        self.assertEqual(multiplication(-2, 5), -10, "-2 * 5 should equal -10")
        self.assertEqual(multiplication(0, 100), 0, "0 * 100 should equal 0")
        self.assertEqual(multiplication(1.5, 2.0), 3.0, "1.5 * 2.0 should equal 3.0")

    def test_division(self):
        self.assertEqual(division(6, 3), 2, "6 / 3 should equal 2")
        self.assertEqual(division(-9, 3), -3, "-9 / 3 should equal -3")
        self.assertAlmostEqual(division(1, 3), 0.3333333333333333, places=7,
                               msg="1 / 3 should approximately equal 0.3333333")

        with self.assertRaises(ValueError) as context:
            division(5, 0)
        self.assertEqual(str(context.exception), "Division by zero is not allowed.")


# Виконання тестів
if __name__ == '__main__':
    unittest.main()
