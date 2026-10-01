from sympy import mod_inverse

p, q, e = 61, 53, 17
n = p * q
d = mod_inverse(e, (p - 1) * (q - 1))
m = 42
c = pow(m, e, n)
print("cipher:", c)
print("plain :", pow(c, d, n))
