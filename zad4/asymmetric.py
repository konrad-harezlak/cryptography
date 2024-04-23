from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from typing import Dict
from fastapi import HTTPException

asymmetric_public_key = None
asymmetric_private_key = None

def generate_asymmetric_keys() -> Dict[str, str]:
    """
    Generates new asymmetric public and private keys and returns them in HEX format.
    """
    global asymmetric_public_key, asymmetric_private_key
    asymmetric_private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    asymmetric_public_key = asymmetric_private_key.public_key()
    public_key_pem = asymmetric_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    private_key_pem = asymmetric_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()
    return {"public_key": public_key_pem, "private_key": private_key_pem}

def set_asymmetric_keys(keys: Dict[str, str]) -> None:
    """
    Sets the asymmetric public and private keys on the server.
    """
    global asymmetric_public_key, asymmetric_private_key
    public_key = serialization.load_pem_public_key(keys["public_key"].encode(), backend=default_backend())
    private_key = serialization.load_pem_private_key(keys["private_key"].encode(), password=None, backend=default_backend())
    asymmetric_public_key = public_key
    asymmetric_private_key = private_key

def asymmetric_encrypt(message: str) -> str:
    """
    Encrypts the message using the currently set public key.
    """
    global asymmetric_public_key
    if asymmetric_public_key is None:
        raise HTTPException(status_code=400, detail="Asymmetric key not set")
    encrypted_message = asymmetric_public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message.hex()

def asymmetric_decrypt(encrypted_message: str, message: str) -> str:
    """
    Decrypts the encrypted message using the currently set private key.
    """
    global asymmetric_private_key
    if asymmetric_private_key is None:
        raise HTTPException(status_code=400, detail="Asymmetric key not set")
    decrypted_message = asymmetric_private_key.decrypt(
        bytes.fromhex(encrypted_message),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()


def asymmetric_sign(message: str) -> str:
    """
    Signs the message using the currently set private key and returns the signature.
    """
    global asymmetric_private_key
    if asymmetric_private_key is None:
        raise HTTPException(status_code=400, detail="Asymmetric key not set")
    signature = asymmetric_private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature.hex()

def asymmetric_verify(signed_message: str, message: str) -> bool:
    """
    Verifies if the message was signed using the currently set public key.
    """
    global asymmetric_public_key
    if asymmetric_public_key is None:
        raise HTTPException(status_code=400, detail="Asymmetric key not set")
    signature = bytes.fromhex(signed_message)
    try:
        asymmetric_public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False
