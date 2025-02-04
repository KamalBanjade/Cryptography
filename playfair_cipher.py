def generate_playfair_matrix(key):
    # Initialize a 5x5 matrix with empty strings
    matrix = [['' for _ in range(5)] for _ in range(5)]

    # Remove duplicate letters from the key and convert to uppercase
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))

    # Define the alphabet, excluding 'J' (since 'I' and 'J' are usually combined in Playfair)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Fill the matrix with the key
    key_index = 0
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
            else:
                # Fill the remaining spaces with the rest of the alphabet
                while alphabet:
                    letter = alphabet[0]
                    alphabet = alphabet[1:]
                    if letter not in key:
                        matrix[i][j] = letter
                        break
    return matrix


def prepare_input(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(filter(str.isalpha, text.upper()))

    # Replace 'J' with 'I' (since 'I' and 'J' are usually combined in Playfair)
    text = text.replace('J', 'I')

    # Insert 'X' between double letters
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
        i += 1

    # If the length of the text is odd, add an 'X' to make it even
    if len(text) % 2 != 0:
        text += 'X'

    return text


def find_position(matrix, char):
    # Find the position of a character in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None  # Character not found (should not happen for valid input)


def process_text(text, key, encrypting=True):
    # Generate the Playfair matrix
    matrix = generate_playfair_matrix(key)

    # Prepare the input text for encryption or decryption
    text = prepare_input(text) if encrypting else text

    processed_text = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        # Case 1: Both characters are in the same row
        if row1 == row2:
            shift = 1 if encrypting else -1
            processed_text += matrix[row1][(col1 + shift) % 5]
            processed_text += matrix[row2][(col2 + shift) % 5]

        # Case 2: Both characters are in the same column
        elif col1 == col2:
            shift = 1 if encrypting else -1
            processed_text += matrix[(row1 + shift) % 5][col1]
            processed_text += matrix[(row2 + shift) % 5][col2]

        # Case 3: Characters form a rectangle
        else:
            processed_text += matrix[row1][col2]
            processed_text += matrix[row2][col1]

    return processed_text


def encrypt(text, key):
    return process_text(text, key, encrypting=True)


def decrypt(text, key):
    return process_text(text, key, encrypting=False)


def remove_padding_x(text):
    cleaned_text = ""
    i = 0
    while i < len(text):
        if text[i] != 'X':
            cleaned_text += text[i]
        elif i > 0 and i < len(text) - 1 and text[i - 1] == text[i + 1]:
            pass  # Ignore padding 'X' between double letters
        else:
            pass  # Ignore padding 'X' added to make the text length even
        i += 1
    return cleaned_text


# Main Program
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key)
print("\nPlaintext:", plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text (with padding):", decrypted_text)

# Remove any extra 'X' characters added during encryption
cleaned_decrypted_text = remove_padding_x(decrypted_text)
print("Decrypted Text (cleaned):", cleaned_decrypted_text)
