import unittest
import string

def encrypt(message, shift_factor):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + shift_factor] if len(abc) > (abc.find(char) + shift_factor) else abc[0] for idx, char in enumerate(message)])
    print(encrypted_message)
    return encrypted_message

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.my_message = "I'm Batman !!! 123"
        self.shift_factor = 2

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_funcReturnSomething(self):
        self.assertIsNotNone(encrypt(self.my_message, self.shift_factor))

    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message, self.shift_factor)))

    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message, self.shift_factor))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message, self.shift_factor), str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + self.shift_factor] if len(abc) > (abc.find(char) + self.shift_factor) else abc[0] for idx, char in enumerate(self.my_message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message, self.shift_factor))

    def test_shift_factor_input_not_none(self):
        self.assertIsNotNone(self.shift_factor)

    def test_shift_factor_input_type(self):
        self.assertIsInstance(self.shift_factor, int)
        

if __name__ == "__main__":
    unittest.main()
