def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def euler_phi(m):
    count = 0
    for i in range(1,m+1):
        if gcd(i,m) == 1:
            count += 1
    return count

m=240
print(f"Euler's phi function of ({m}) is = {euler_phi(m)}")

