import secrets
import hashlib
import hmac

def generate_salt():
    """
    Generate a random salt.

    Returns:
        str: Randomly generated salt.
    """
    return secrets.token_hex(16)

def hash_password(password, salt):
    """
    Hash password and salt using SHA-256 algorithm.

    Args:
        password (str): Password to be hashed.
        salt (str): Salt to be used in hashing.

    Returns:
        str: Hashed password.
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()

def verify_hashed_password(password, salt, hash_value):
    """
    Verify hashed password.

    Args:
        password (str): Password to be verified.
        salt (str): Salt used in hashing.
        hash_value (str): Hashed password to be verified.

    Returns:
        bool: True if password is verified, False otherwise.
    """
    return hmac.compare_digest(hash_password(password, salt), hash_value)
