import unittest
from calculator import generatePassword

class TestCalculator(unittest.TestCase):

    def test_generate_password(self):
        passwords = generatePassword(10, 5, 15)
        self.assertEqual(len(passwords), 3, 15)
        for password in passwords:
            self.assertGreaterEqual(len(password), 5)
            self.assertLessEqual(len(password), 15)
            self.assertTrue(any(char.isdigit() for char in password))
            self.assertTrue(any(char.isupper() for char in password))

if __name__ == '__main__':
    unittest.main()
