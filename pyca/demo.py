import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 1. AES-GCM: enkripsi + deteksi pemalsuan
aes = AESGCM(AESGCM.generate_key(bit_length=256))
nonce = os.urandom(12)
ct = aes.encrypt(nonce, b"halo kripto", b"header")
print(aes.decrypt(nonce, ct, b"header"))
bad = bytearray(ct)
bad[0] ^= 1
try:
    aes.decrypt(nonce, bytes(bad), b"header")
except Exception as e:
    print("tamper terdeteksi:", type(e).__name__)

# 2. RSA-2048 dengan padding OAEP
priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
oaep = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),
                    algorithm=hashes.SHA256(), label=None)
c = priv.public_key().encrypt(b"rahasia", oaep)
print(priv.decrypt(c, oaep))
