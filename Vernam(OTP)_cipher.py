import random

def generate_key(length):
    key = ''
    for i in range(length):
        key += random.choice('01')
        # key += random.choice(string.ascii_uppercase)
        # key += random.choice(string.ascii_lowercase)
    return key

def vernam_encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext


def vernam_decrypt(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i]))
    return plaintext


plain_text = input('Enter plain text: ')
key = input('Enter key: ')
print(f"plaintext: {plain_text}")
cipher_text = vernam_encrypt(plain_text, key)
print(f"Encrypted ciphertext: {cipher_text}")
decrypted_text = vernam_decrypt(cipher_text, key)
print(f"Decrypted ciphertext: {decrypted_text}")
