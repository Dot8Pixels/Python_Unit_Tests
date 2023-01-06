# Exercise 8
# The calculate_tax() function is given (no argument validation):



# def calculate_tax(amount, tax_rate, age):
#     """The function returns the amount of income tax."""
 
#     if age <= 18:
#         return int(min(amount * tax_rate, 5000))
#     elif age <= 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 8000))


# Implement a function called test_calculate_tax() that asserts the following test cases:

# calculate_tax(60000, 0.15, 10) == 5000

# calculate_tax(60000, 0.15, 18) == 5000

# calculate_tax(60000, 0.15, 19) == 9000

# calculate_tax(60000, 0.15, 65) == 9000

# calculate_tax(60000, 0.15, 66) == 8000

# Then call test_calculate_tax() function.


def calculate_tax(amount, tax_rate, age):
    """The function returns the amount of income tax."""
 
    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))
 
 
def test_calculate_tax():
    assert calculate_tax(60000, 0.15, 10) == 5000
    assert calculate_tax(60000, 0.15, 18) == 5000
    assert calculate_tax(60000, 0.15, 19) == 9000
    assert calculate_tax(60000, 0.15, 65) == 9000
    assert calculate_tax(60000, 0.15, 66) == 8000
 
 
test_calculate_tax()