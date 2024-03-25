from password_manager import PasswordManager
from database import DatabaseManager
# Example usage:
password_manager = PasswordManager()

while True:
    password1 = input("Enter password: ")
    password2 = input("Enter password again: ")

    if password1 == password2:
        if len(password1) == 0:
            print("Password cannot be empty!")
        else:
            password_manager.store_password_pbkdf2(password1)
            break
    else:
        print("Passwords do not match! Please try again.")


# Print passwords
db = DatabaseManager()
passwords = db.get_passwords()
print(passwords)
db.close_connection()
