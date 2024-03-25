import itertools
import enchant

# Function to check if a letter is properly shifted after a given shift
def checkLetter(letter, shift):
    shiftedLetter = letter + shift
    if shiftedLetter > 90:
        shiftedLetter -= 26
    elif shiftedLetter < 65:
        shiftedLetter += 26
    return chr(shiftedLetter)

# Function to validate the sentence
def validateSent(sent):
    if sent != sent.upper():
        print("Enter everything in uppercase letters.")
        return False
    if not (check_sentence(sent)):
        print("That is not a word.")
        return False
    return True

# Function to check the sentence using the English language dictionary
def check_sentence(sentence):
    dictionary = enchant.Dict("en_US")
    words = sentence.split()
    for word in words:
        if not dictionary.check(word):
            return False
    return True

# Function to perform Caesar cipher
def cipherCezar(sent, shift):
    encryptedSentence = ""
    for letter in sent:
        shifted = checkLetter(ord(letter), shift)
        encryptedSentence += shifted
    return encryptedSentence

# Function to decipher Caesar cipher
def decipherCezar(encrypted, shift):
    decryptedSentence = ""
    for letter in encrypted:
        shifted = checkLetter(ord(letter), -shift)
        decryptedSentence += shifted
    return decryptedSentence

# Function to automatically decipher Caesar cipher
def automaticDecipherCezar(encrypted):
    decrypted = ""
    for i in range(0, 26):
        word = ""
        for letter in encrypted:
            word += checkLetter(ord(letter), i)
        if check_sentence(word):
            decrypted = word
    return decrypted

# Function to perform Vigenère cipher
def cipherVigenere(sent, key):
    encryptedSentence = ""
    i = 0
    for letter in sent:
        keyLetter = key[i % len(key)]
        shifted = chr((ord(letter) - ord("A") + ord(keyLetter)) % 26 + ord("A"))
        encryptedSentence += shifted
        i += 1
    return encryptedSentence

# Function to decipher Vigenère cipher
def decipherVigenere(encrypted, key):
    decryptedSentence = ""
    i = 0
    for letter in encrypted:
        keyLetter = key[i % len(key)]
        shifted = chr((ord(letter) - ord("A") - ord(keyLetter)) % 26 + ord("A"))
        decryptedSentence += shifted
        i += 1
    return decryptedSentence

# Function to automatically decipher Vigenère cipher
def automaticDecipherVigenere(encrypted):
    decrypted = []
    possible_keys = []
    keys = []

    for key_length in range(1, 4):
        keys += [''.join(key) for key in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=key_length)]
    for key in keys:
        decrypted_attempt = decipherVigenere(encrypted, key)
        if check_sentence(decrypted_attempt) and check_sentence(key):
            decrypted.append(decrypted_attempt)
            possible_keys.append(key)
            print("Key:", key)
            print("Decrypted sentence:", decrypted_attempt)
    return decrypted, possible_keys

# Function to run tests
def run_tests():
    test_checkLetter()
    test_validateSent()
    test_check_sentence()
    print("All tests passed!")

# Function to check if a letter is shifted properly
def test_checkLetter():
    assert checkLetter(ord('A'), 3) == 'D'
    assert checkLetter(ord('X'), 3) == 'A'
    assert checkLetter(ord('Z'), 3) == 'C'

# Function to validate the sentence
def test_validateSent():
    assert validateSent("HELLO") == True
    assert validateSent("Hello") == False
    assert validateSent("12345") == True

# Function to check if the sentence is valid
def test_check_sentence():
    assert check_sentence("HELLO WORLD") == True
    assert check_sentence("HELLO 123") == True

# Main function
def main():
    sent = input("Enter your example text (must be in UPPERCASE and contain normal words/sentence): ")
    while not validateSent(sent):
        sent = input("Enter your example text (must be in UPPERCASE and contain normal words/sentence): ")
    shift = 3
    key = "KEY"
    cezarSentence = cipherCezar(sent, shift)
    vigenereSentence = cipherVigenere(sent, key)
    print("Cezar sentence:", cezarSentence)
    print("Vigenere sentence:", vigenereSentence)
    cezarDecryptedSentence = decipherCezar(cezarSentence, shift)
    vigenereDecryptedSentence = decipherVigenere(vigenereSentence, key)
    print("Cezar decrypted sentence:", cezarDecryptedSentence)
    print("Vigenere decrypted sentence:", vigenereDecryptedSentence)
    print("Automatic Cezar decryptor:", automaticDecipherCezar(cezarSentence))
    print("Automatic Vigenere decryptor:", automaticDecipherVigenere(vigenereSentence))

# Run tests if this script is executed as the main program
if __name__ == "__main__":
    run_tests()
    main()
