c = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

def score(t):
    return sum(chr(x) in "etaoin shrdlu" for x in t.lower())

k = max(range(256), key=lambda k: score(bytes(b ^ k for b in c)))
print(k, bytes(b ^ k for b in c))
