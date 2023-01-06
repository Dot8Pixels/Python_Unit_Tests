# The following area() function is given, which returns the area of a rectangle with additional argument validation:



# def area(width, height):
#     """The function returns the area of the rectangle."""
 
#     if not (isinstance(width, int) and isinstance(height, int)):
#         raise TypeError(
#             'The width and height must be of type int.'
#         )
#     if not (width > 0 and height > 0):
#         raise ValueError(
#             'The width and height must be positive.'
#         )
#     return width * height


# Assert the following function call:

# area('5', '4')

# with a value of 20.



# Expected Action: Raising TypeError.


def area(width, height):
    """The function returns the area of the rectangle."""
 
    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError(
            'The width and height must be of type int.'
        )
 
    if not (width > 0 and height > 0):
        raise ValueError(
            'The width and height must be positive.'
        )
 
    return width * height
 
 
assert area('5', '4') == 20