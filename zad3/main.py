from password_manager import PasswordManager
from database import DatabaseManager
# Example usage:
password_manager = PasswordManager()

# Store and verify password using the first method
password_manager.store_password("password123")
print("Password manager", password_manager.verify_password("password123"))

# Store and verify password using the second method
password_manager.store_password_pbkdf2("password123")
print("Password pbkdf2", password_manager.verify_password_pbkdf2("password123"))

# Print passwords
db = DatabaseManager()
passwords = db.get_passwords()
print(passwords)
db.close_connection()