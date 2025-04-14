# https://github.com/Fergui67/lab10-CW-FG.git
import unittest
from calculator import *
# Partner 1: Fernando Guillen.
# Partner 2: Cade Wedekind

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)

        self.assertEqual(add(-1, 1), 0)

        self.assertEqual(add(5, 0), 5)
    #     fill in code

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)

        self.assertEqual(subtract(-1, -1), 0)

        self.assertEqual(subtract(0, 5), -5)
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 8), 24)           # 3 * 8 = 24
        self.assertNotEqual(mul(2, 2), 6)         # 2 * 2 = 4, so this should pass
        self.assertAlmostEqual(mul(3.6, 2), 7.2)  # 3.6 * 2 = 7.2

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(4, 0), "Error: Division by zero")

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)

        self.assertAlmostEqual(logarithm(10, 100), 2)

        self.assertAlmostEqual(logarithm(math.e, math.e), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
<<<<<<< HEAD
        with self.asserRaises(ValueError):
            logartithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -8)
=======
        self.assertEqual(logarithm(-2, 8), "Error: Logarithm base and argument must be positive")
>>>>>>> 7b8786d43a052057321df8d8e1aba6160c66afa3

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(16), 4.0)
        with self.assertRaises(ValueError):
            square_root(-1)
             # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()