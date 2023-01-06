# The following calculate_daily_return() function is given, which takes two arguments: open and close (open and close price of a financial instrument from a trading session). The function returns the value of the daily rate of return.



# def calculate_daily_return(open, close):
#     return (close / open - 1) * 100


# Complete the implementation of the TestCalculateDailyReturn class by adding three test methods:

# test_positive_return()

# using the method assertAlmostEqual  check if code calculate_daily_return(349.0, 360.0) returns the appropriate value


# test_negative_return()

# using the method assertAlmostEqual check if code calculate_daily_return(349.0, 340.0) returns the appropriate value


# test_zero_return()

# using the method assertAlmostEqual check if code calculate_daily_return(349.0, 349.0) returns the appropriate value



# Note: Note how the assertAlmostEqual method works.



# You only need to implement test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


import unittest
 
 
def calculate_daily_return(open, close):
    return (close / open - 1) * 100
 
 
class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self):
        self.assertAlmostEqual(
            calculate_daily_return(349, 360), 13.1518625
        )
 
    def test_negative_return(self):
        self.assertAlmostEqual(
            calculate_daily_return(349, 340), -2.5787966
        )
 
    def test_zero_return(self):
        self.assertAlmostEqual(
            calculate_daily_return(349.0, 349.0), 0.0
        )


if __name__ in '__main__':
    unittest.main()