text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"
out = bytes(b ^ key[i % len(key)] for i, b in enumerate(text))
print(out.hex())
