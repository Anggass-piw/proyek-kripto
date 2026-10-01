from math import gcd
from sympy import randprime

e1, e2 = 17, 65537
while True:
    p = randprime(2**127, 2**128)
    q = randprime(2**127, 2**128)
    phi = (p - 1) * (q - 1)
    if p != q and gcd(e1, phi) == 1 and gcd(e2, phi) == 1:
        break
n = p * q
m = int.from_bytes(b"rahasia", "big")
c1, c2 = pow(m, e1, n), pow(m, e2, n)

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

_, a, b = egcd(e1, e2)
r = (pow(c1, a, n) * pow(c2, b, n)) % n
print(r.to_bytes((r.bit_length() + 7) // 8, "big"))
