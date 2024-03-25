from password_manager import PasswordManager
from database import DatabaseManager
# Example usage:
password_manager = PasswordManager()
password1 = input("Enter password: ")
password2 = input("Enter password again: ")

if(password1==password2):
    # Store and verify password using the first method
    password_manager.store_password(password1)
    print("Password manager", password_manager.verify_password(password1))

    # Store and verify password using the second method
    password_manager.store_password_pbkdf2(password1)
    print("Password pbkdf2", password_manager.verify_password_pbkdf2(password1))
else:
    print("Passwords do not match!")


# Print passwords
db = DatabaseManager()
passwords = db.get_passwords()
print(passwords)
db.close_connection()