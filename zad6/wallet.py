import hashlib
import json
import binascii
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def generate_signature(self, message):
        return binascii.hexlify(self.private_key.sign(message.encode())).decode()

    def verify_signature(self, signature, message, public_key):
        return public_key.verify(binascii.unhexlify(signature), message.encode())
