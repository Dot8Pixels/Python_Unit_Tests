# An implementation of the StringListOnly class is given:



# class StringListOnly(list):
 
#     def append(self, string):
#         if not isinstance(string, str):
#             raise TypeError(
#                 'Only object of type str can be added to the list.'
#             )
#         super().append(string)


# Only objects of type str can be added to the list of type StringListOnly using the append() method.

# Using the unittest framework create a TestStringListOnly class that inherits from the unittest.TestCase class that implements two test methods:

# test_append_string()

# checks if we can add an object of the str type to the StringListOnly instance using the append() method. Use the assertIn() method for this purpose.


# test_append_not_string_should_raise_error()

# checks if TypeError is raised when trying to add an instance of type list. To do this, use the assertRaises() method.

# checks if TypeError is raised when trying to add an instance of type bool. To do this, use the assertRaises() method.



# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


import unittest
 
 
class StringListOnly(list):
 
    def append(self, string):
        if not isinstance(string, str):
            raise TypeError(
                'Only object of type str can be added to the list.'
            )
        super().append(string)
 
 
class TestStringListOnly(unittest.TestCase):
 
    def test_append_string(self):
        slo = StringListOnly()
        string = 'big_data'
        slo.append(string)
        self.assertIn(string, slo)
 
    def test_append_not_string_should_raise_error(self):
        slo = StringListOnly()
        not_string_1 = ['big_data']
        not_string_2 = True
        self.assertRaises(TypeError, slo.append, not_string_1)
        self.assertRaises(TypeError, slo.append, not_string_2)


if __name__ in '__main__':
    unittest.main()
