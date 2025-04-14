import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertEqual(log(-2, 8), "Error: Logarithm base and argument must be positive")
        self.assertEqual(log(2, -8), "Error: Logarithm base and argument must be positive")
        self.assertEqual(log(0, 5), "Error: Logarithm base and argument must be positive")

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertRaises(-4)
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