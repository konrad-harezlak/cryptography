from fastapi import FastAPI
from typing import Dict
from symmetric import generate_symmetric_key, set_symmetric_key, encode_message_with_symmetric_key, decode_message_with_symmetric_key
from asymmetric import generate_asymmetric_keys, set_asymmetric_keys, asymmetric_sign, asymmetric_verify, asymmetric_encrypt, asymmetric_decrypt
import uvicorn

app = FastAPI()

@app.get("/symmetric/key")
def get_symmetric_key():
    return {"symmetric_key": generate_symmetric_key()}

@app.post("/symmetric/key")
def set_symmetric_key_endpoint(key: str):
    set_symmetric_key(key)

@app.post("/symmetric/encode")
def symmetric_encode(message: str):
    return {"encoded_message": encode_message_with_symmetric_key(message)}

@app.post("/symmetric/decode")
def symmetric_decode(encoded_message: str):
    return {"decoded_message": decode_message_with_symmetric_key(encoded_message)}

@app.get("/asymmetric/key")
def get_asymmetric_key():
    return generate_asymmetric_keys()

@app.post("/asymmetric/key")
def set_asymmetric_key(keys: Dict[str, str]):
    set_asymmetric_keys(keys)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
