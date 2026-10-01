from sympy import factorint, mod_inverse

n, e = 3233, 17
c = pow(42, e, n)  # anggap ini ciphertext hasil sadapan
p, q = factorint(n).keys()
d = mod_inverse(e, (p - 1) * (q - 1))
print("plain:", pow(c, d, n))
