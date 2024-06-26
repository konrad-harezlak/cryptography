import png
import base64
from encryption import encrypt_message, decrypt_message

PROMPT = """
Welcome to basic steganography. Please choose:

1. To encode a message into an image
2. To decode an image into a message
q. to exit
"""

ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"


def encode_message_as_bytestring(message, key):
    encrypted_message = encrypt_message(message, key)
    b64 = encrypted_message.encode("utf8")
    bytes_ = base64.encodebytes(b64)
    bytestring = "".join(["{:08b}".format(x) for x in bytes_])
    bytestring += ENDOFMESSAGE
    return bytestring


def get_pixels_from_image(fname):
    img = png.Reader(fname).read()
    pixels = list(img[2])  # Convert to list to allow modification
    return pixels


def encode_pixels_with_message(pixels, bytestring):
    '''modifies pixels to encode the contents from bytestring'''

    enc_pixels = []
    string_i = 0
    for row in pixels:
        enc_row = []
        for i, char in enumerate(row):
            if string_i >= len(bytestring):
                pixel = row[i]
            else:
                if row[i] % 2 != int(bytestring[string_i]):
                    if row[i] == 0:
                        pixel = 1
                    else:
                        pixel = row[i] - 1
                else:
                    pixel = row[i]
            enc_row.append(pixel)
            string_i += 1

        enc_pixels.append(enc_row)
    return enc_pixels


def write_pixels_to_image(pixels, fname):
    print("Pixels dimensions:", len(pixels), "x", len(pixels[0]))
    png.from_array(pixels, 'RGB').save(fname)


def decode_pixels(pixels, key):
    try:
        bytestring = []
        for row in pixels:
            for c in row:
                bytestring.append(str(c % 2))
        bytestring = ''.join(bytestring)
        message = decode_message_from_bytestring(bytestring, key)
        return message
    except ValueError:
        return "Invalid decryption key"


def decode_message_from_bytestring(bytestring, key):
    try:
        bytestring = bytestring.split(ENDOFMESSAGE)[0]
        message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
        message = base64.decodebytes(message).decode("utf8")
        decrypted_message = decrypt_message(message, key)
        return decrypted_message
    except ValueError:
        return "Invalid decryption key"


def main():
    print(PROMPT)
    user_inp = ""
    while user_inp not in ("1", "2", "q"):
        user_inp = input("Your choice: ")

    if user_inp == "1":
        in_image = input("Please enter filename of existing PNG image: ")
        in_message = input("Please enter the message to encode: ")
        key = int(input("Please enter the encryption key (an integer): "))

        print("-ENCODING-")
        pixels = get_pixels_from_image(in_image)
        bytestring = encode_message_as_bytestring(in_message, key)
        epixels = encode_pixels_with_message(pixels, bytestring)
        write_pixels_to_image(epixels, in_image + "-enc.png")

    elif user_inp == "2":
        in_image = input("Please enter the filename of an existing PNG image: ")
        key = int(input("Please enter the decryption key (an integer): "))

        print("-DECODING-")
        pixels = get_pixels_from_image(in_image)
        print(decode_pixels(pixels, key))


if __name__ == "__main__":
    main()
