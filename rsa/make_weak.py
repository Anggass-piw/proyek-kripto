from math import gcd
from sympy import randprime

e = 65537
while True:
    p = randprime(2**40, 2**41)
    q = randprime(2**40, 2**41)
    if p != q and gcd(e, (p - 1) * (q - 1)) == 1:
        break
n = p * q
m = int.from_bytes(b"halo", "big")
print(n, e, pow(m, e, n))
