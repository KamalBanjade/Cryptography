def rail_fence_encrypt(plaintext, rails, key):
    rail_matrix = [['' for _ in range(len(plaintext))] for _ in range(rails)]

    rail = 0
    direction = 1
    for i, char in enumerate(plaintext):
        rail_matrix[rail][i] = char
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    print("Rail Matrix:")
    for row in rail_matrix:
        print(row)

    ciphertext = ''
    for i in range(rails):
        rail_index = key.index(i + 1)
        for char in rail_matrix[rail_index]:
            if char:
                ciphertext += char
    return ciphertext


def rail_fence_decrypt(ciphertext, rails, key):
    rail_matrix = [['' for _ in range(len(ciphertext))] for _ in range(rails)]

    rail_lengths = [0] * rails
    rail = 0
    direction = 1
    for _ in range(len(ciphertext)):
        rail_lengths[rail] += 1
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for i in range(rails):
        rail_index = key.index(i + 1)
        for j in range(rail_lengths[rail_index]):
            rail_matrix[rail_index][j] = ciphertext[index]
            index += 1

    plaintext = ''
    rail = 0
    direction = 1
    for _ in range(len(ciphertext)):
        plaintext += rail_matrix[rail][0]
        rail_matrix[rail] = rail_matrix[rail][1:]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return plaintext

plaintext = input('Enter plaintext: ')
rails = int(input('Enter number of rails: '))
key = list(map(int, input('Enter key as a list of integers (e.g., 2 1 3): ').split()))

encrypted = rail_fence_encrypt(plaintext, rails, key)
decrypted = rail_fence_decrypt(encrypted, rails, key)

print("Plaintext: ", plaintext)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)