import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a,p):
    if gcd(a,p) != 1:
        return None
    else:
        p0,p1 = p,0
        a0,a1 = 1,1
        while a>1:
            q = a//p
            a,p = p,a%p
            a1,p1 = p1,a1-q*p1
        return a1%p0
def elgamal_keygen(p):
    g = random.randint(2,p-1)
    x = random.randint(1,p-2)
    y = pow(g,x,p)
    return (p,g,y),x
def elgamal_encrypt(m,public_key):
    p,g,y = public_key
    k = random.randint(1,p-2)
    c1= pow(g,k,p)
    c2= (m*pow(y,k,p))%p
    return c1,c2
def elgamal_decrypt(c1,c2,private_key,p):
    s= pow(c1,private_key,p)
    m= (c2*modinv(s,p))%p
    return m

p= 467
public_key,private_key = elgamal_keygen(p)
m = 123
print("Original Message:",m)
ciphertext = elgamal_encrypt(m,public_key)
print("Ciphertext:",ciphertext)
decrypted_message = elgamal_decrypt(ciphertext[0],ciphertext[1],private_key,p)
print("Decrypted Message:",decrypted_message)

