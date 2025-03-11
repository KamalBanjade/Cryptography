def extended_gcd(a,b):
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

def mod_inv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for {a} mod {m}")
    return x % m

a = 12
m = 67
print(f"The Multiplicative inverse of {a} mod {m} is {mod_inv(a, m)}")
