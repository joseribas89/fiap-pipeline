import unittest
from calculator import generatePassword


class TestCalculator(unittest.TestCase):
    def test_generate_password(self):
        # Testando se as senhas geradas têm o comprimento correto
        self.assertEqual(len(generatePassword([5, 10, 15])), 3)

        # Testando se as senhas geradas contêm apenas letras minúsculas e números
        for password in generatePassword([5, 10, 15]):
            self.assertTrue(password.isalnum() and password.islower())

        # Testando se as senhas geradas contêm pelo menos um número e uma letra maiúscula
        for password in generatePassword([5, 10, 15]):
            has_number = any(char.isdigit() for char in password)
            has_uppercase = any(char.isupper() for char in password)
            self.assertTrue(has_number and has_uppercase)


if __name__ == '__main__':
    unittest.main()
