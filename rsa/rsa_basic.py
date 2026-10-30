"""Contoh textbook RSA untuk edukasi saja.

Implementasi ini tidak memakai padding dan memakai bilangan yang sangat kecil.
Jangan gunakan untuk melindungi data nyata atau dalam sistem produksi.
"""

from sympy import mod_inverse

# Contoh RSA mentah (tanpa padding), sengaja memakai parameter kecil.
p, q, e = 61, 53, 17
n = p * q
d = mod_inverse(e, (p - 1) * (q - 1))
m = 42
c = pow(m, e, n)
print("cipher:", c)
print("plain :", pow(c, d, n))
