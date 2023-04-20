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
        self.assertEqual(len(generatePassword([5, 10, 15])), 3)
        self.assertEqual(len(passwords), 3)
        for password in passwords:
            self.assertGreaterEqual(len(password), 3)

if __name__ == '__main__':
    unittest.main()
