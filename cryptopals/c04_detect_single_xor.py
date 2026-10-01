import os

FREQ = {"e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0, "n": 6.7,
        " ": 13.0, "s": 6.3, "h": 6.1, "r": 6.0, "d": 4.3, "l": 4.0, "u": 2.8}

def score(t):
    s = 0
    for b in t:
        ch = chr(b).lower()
        if ch in FREQ:
            s += FREQ[ch]
        elif not (32 <= b < 127 or b == 10):
            s -= 20
    return s

path = os.path.join(os.path.dirname(__file__), "data", "4.txt")
best = (-10**9, None, None)
for line in open(path):
    c = bytes.fromhex(line.strip())
    for k in range(256):
        p = bytes(b ^ k for b in c)
        s = score(p)
        if s > best[0]:
            best = (s, k, p)
print(best[1], best[2])
