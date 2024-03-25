import unittest
from password_manager import PasswordManager

class TestPasswordManager(unittest.TestCase):
    """Unit tests for PasswordManager class."""

    def setUp(self):
        """
        Set up test environment.

        Create a PasswordManager instance for testing.
        """
        self.password_manager = PasswordManager(':memory:') 

    def tearDown(self):
        """
        Clean up after the test.

        Close the connection to the database.
        """
        self.password_manager.db_manager.close_connection()

    def test_store_and_verify_password(self):
        """
        Test storing and verifying password.

        Verify that passwords stored using both custom method and pbkdf2_hmac are successfully verified.
        """
        password = "password123"

        # Test storing and verifying password using a custom method
        self.password_manager.store_password(password)
        self.assertTrue(self.password_manager.verify_password(password))

        # Test storing and verifying password using pbkdf2_hmac
        self.password_manager.store_password_pbkdf2(password)
        self.assertTrue(self.password_manager.verify_password_pbkdf2(password))

if __name__ == '__main__':
    unittest.main()
