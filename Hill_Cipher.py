import numpy as np

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus
    return matrix_modulus_inv

def hill_cipher_encrypt(plaintext, key):
    n = len(key)
    plaintext = [ord(char) - ord('A') for char in plaintext.upper() if char.isalpha()]
    if len(plaintext) % n != 0:
        plaintext.extend([0] * (n - len(plaintext) % n))
    plaintext_matrix = np.array(plaintext).reshape(-1, n)
    ciphertext_matrix = np.dot(plaintext_matrix, key) % 26
    ciphertext = ''.join([chr(char + ord('A')) for row in ciphertext_matrix for char in row])
    return ciphertext

def hill_cipher_decrypt(ciphertext, key):
    n = len(key)
    key_inv = matrix_mod_inv(key, 26)
    ciphertext = [ord(char) - ord('A') for char in ciphertext.upper() if char.isalpha()]
    ciphertext_matrix = np.array(ciphertext).reshape(-1, n)
    plaintext_matrix = np.dot(ciphertext_matrix, key_inv) % 26
    plaintext = ''.join([chr(char + ord('A')) for row in plaintext_matrix for char in row])
    return plaintext

def get_key_matrix():
    n = int(input("Enter the dimension of the key matrix:  "))
    print(f"Enter the elements of the {n}x{n} key matrix row by row:")
    key = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("Invalid input: The matrix must be square.")
            return None
        key.append(row)
    key_matrix = np.array(key)

    # Calculate determinant
    det = int(np.round(np.linalg.det(key_matrix)))
    print(f"Determinant of the matrix: {det}")

    # Check if the determinant is invertible under modulus 26
    try:
        det_inv = pow(det, -1, 26)  # Modular inverse of determinant
    except ValueError:
        print("This matrix is not invertible under modulo 26. Please provide a valid key matrix.")
        return None

    # If determinant is invertible, proceed
    print("The matrix is valid for use as a key.")
    return key_matrix

# Main program
key = get_key_matrix()
if key is not None:
    plaintext = input("Enter the plaintext: ")
    ciphertext = hill_cipher_encrypt(plaintext, key)
    print("Encrypted Text: ", ciphertext)
    decrypted_text = hill_cipher_decrypt(ciphertext, key)
    print("Decrypted Text: ", decrypted_text)
