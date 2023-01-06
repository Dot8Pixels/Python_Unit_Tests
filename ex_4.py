# The implementation of the max_min_diff() function is given:



# def max_min_diff(numbers):
#     return max(numbers) - min(numbers)


# Modify the implementation of the max_min_diff() function. By using the assert statement inside this function, add the ability to check the length of the numbers argument before returning the result. If the length of the numbers object is 0 raise the AssertionError with message:



# 'The numbers object cannot be empty.'


# Otherwise, it returns the correct result (the difference between the highest and lowest value for numbers).

# In case the module with the solution is run directly, call the max_min_diff() function passing an empty list.



# Tip: Use the conditional statement and the module's __name__ attribute for this:


if __name__ == '__main__':
    do_something()

def max_min_diff(numbers):
    assert len(numbers) != 0, 'The numbers object cannot be empty.'
    return max(numbers) - min(numbers)
 
 
if __name__ == '__main__':
    max_min_diff([])