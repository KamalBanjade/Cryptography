def prime_factorization(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n = n // 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n = n // i
        i += 2
    if n > 1:
        factors[n] = 1
    return factors

def euler_phi(m):
    if m == 1:
        return 1
    factors = prime_factorization(m)
    result = m
    for prime in factors:
        result = result * (1 - 1/prime)
    return int(result)

m = 240
print(f"Euler's phi function of ({m}) is = {euler_phi(m)}")