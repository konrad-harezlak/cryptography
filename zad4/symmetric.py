from cryptography.fernet import Fernet
from fastapi import HTTPException

symmetric_key = None

def generate_symmetric_key() -> str:
    """
    Generates a random symmetric key and returns it in HEX format.
    """
    key = Fernet.generate_key()
    return key.decode()

def set_symmetric_key(key: str) -> None:
    """
    Sets the symmetric key on the server.
    """
    global symmetric_key
    symmetric_key = key.encode()

def encode_message_with_symmetric_key(message: str) -> str:
    """
    Encrypts the message using the symmetric key.
    """
    if symmetric_key is None:
        raise HTTPException(status_code=400, detail="Symmetric key not set")
    cipher = Fernet(symmetric_key)
    encoded_message = cipher.encrypt(message.encode())
    return encoded_message.decode()

def decode_message_with_symmetric_key(encoded_message: str) -> str:
    """
    Decrypts the encoded message using the symmetric key.
    """
    if symmetric_key is None:
        raise HTTPException(status_code=400, detail="Symmetric key not set")
    cipher = Fernet(symmetric_key)
    decoded_message = cipher.decrypt(encoded_message.encode())
    return decoded_message.decode()
