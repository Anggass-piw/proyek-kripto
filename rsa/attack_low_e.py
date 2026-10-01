from sympy import randprime, integer_nthroot

p = randprime(2**199, 2**200)
q = randprime(2**199, 2**200)
n = p * q
m = int.from_bytes(b"flag{kubus}", "big")
c = pow(m, 3, n)  # e=3, m^3 < n jadi tidak "terbungkus" modulus

r, _ = integer_nthroot(c, 3)
print(r.to_bytes((r.bit_length() + 7) // 8, "big"))
