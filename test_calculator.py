import unittest
from calculator import generatePassword, replaceWithNumber, replaceWithUppercaseLetter

class TestCalculator(unittest.TestCase):

    def test_replace_with_number(self):
        password = "password"
        result = replaceWithNumber(password)
        self.assertNotEqual(password, result)

    def test_replace_with_uppercase_letter(self):
        password = "password"
        result = replaceWithUppercaseLetter(password)
        self.assertNotEqual(password, result)

    def test_generate_password(self):
        minLength = 3
        maxLength = 12
        passwords = generatePassword([5, 10, 15], minLength, maxLength)
        self.assertEqual(len(passwords), 3)
        for password in passwords:
            self.assertGreaterEqual(len(password), minLength)
            self.assertLessEqual(len(password), maxLength)

if __name__ == '__main__':
    unittest.main()
