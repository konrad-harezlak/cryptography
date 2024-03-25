import hashlib
import hmac
from database import DatabaseManager
from hash_utils import generate_salt, hash_password, verify_hashed_password

class PasswordManager:
    """Class for managing passwords."""

    def __init__(self, db_name=None):
        """
        Initialize PasswordManager.

        Args:
            db_name (str): Name of the SQLite database.
        """
        self.db_manager = DatabaseManager(db_name)
        self.db_manager.create_table()

    def store_password(self, password):
        """
        Store password using a custom method.

        Args:
            password (str): Password to be stored.
        """
        salt = generate_salt()
        hash_value = hash_password(password, salt)
        self.db_manager.insert_password(hash_value, salt)

    def verify_password(self, password):
        """
        Verify password using a custom method.

        Args:
            password (str): Password to be verified.

        Returns:
            bool: True if password is verified, False otherwise.
        """
        stored_passwords = self.db_manager.get_passwords()
        for stored_password in stored_passwords:
            hash_value, salt = stored_password
            if verify_hashed_password(password, salt, hash_value):
                return True
        return False

    def store_password_pbkdf2(self, password):
        """
        Store password using pbkdf2_hmac.

        Args:
            password (str): Password to be stored.
        """
        salt = generate_salt()
        hash_value = self.pbkdf2_hash_password(password, salt)
        self.db_manager.insert_password(hash_value, salt)

    def verify_password_pbkdf2(self, password):
        """
        Verify password using pbkdf2_hmac.

        Args:
            password (str): Password to be verified.

        Returns:
            bool: True if password is verified, False otherwise.
        """
        stored_passwords = self.db_manager.get_passwords()
        for stored_password in stored_passwords:
            hash_value, salt = stored_password
            if self.pbkdf2_verify_hashed_password(password, salt, hash_value):
                return True
        return False

    def pbkdf2_hash_password(self, password, salt):
        """
        Hash password and salt using pbkdf2_hmac.

        Args:
            password (str): Password to be hashed.
            salt (str): Salt to be used in hashing.

        Returns:
            str: Hashed password.
        """
        return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

    def pbkdf2_verify_hashed_password(self, password, salt, hash_value):
        """
        Verify hashed password using pbkdf2_hmac.

        Args:
            password (str): Password to be verified.
            salt (str): Salt used in hashing.
            hash_value (str): Hashed password to be verified.

        Returns:
            bool: True if password is verified, False otherwise.
        """
        return hmac.compare_digest(self.pbkdf2_hash_password(password, salt), hash_value)
