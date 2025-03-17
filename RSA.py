import random
from math import gcd

def is_prime(n):
    if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def generate_prime(length):
    p = random.getrandbits(length) | (1 << length - 1) | 1
    while not is_prime(p):
        p = random.getrandbits(length) | (1 << length - 1) | 1
    return p

def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_key_pair(length=8):
    p, q = generate_prime(length), generate_prime(length)
    while p == q: q = generate_prime(length)
    n, phi = p * q, (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1: e = random.randrange(1, phi)
    d = mod_inv(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, text): return [pow(ord(c), *public_key) for c in text]
def decrypt(private_key, cipher): return ''.join(chr(pow(c, *private_key)) for c in cipher)

# Usage
public, private = generate_key_pair()
print(f"Public: {public}\nPrivate: {private}")
msg = input("Message: ").strip()
enc = encrypt(public, msg)
dec = decrypt(private, enc)
print(f"Encrypted: {enc}\nDecrypted: {dec}")