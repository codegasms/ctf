from Crypto.Cipher import AES


ciphertext = open("ciphertext.txt").read().split("=")[-1].strip()
ciphertext = bytes.fromhex(ciphertext)

iv = (0x000102030405060708090A0B0C0D0E0F).to_bytes(16, "big")
key = b"yougotthekeynjoy"

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
