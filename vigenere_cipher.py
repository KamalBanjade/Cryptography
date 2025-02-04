def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            plaintext += char
    return plaintext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = vigenere_cipher(plaintext, key)
print(f"Encrypted ciphertext: {ciphertext}")

decrypted_text = vigenere_decrypt(ciphertext, key)
print(f"Decrypted plaintext: {decrypted_text}")