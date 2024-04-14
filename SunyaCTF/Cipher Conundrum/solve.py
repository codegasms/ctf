import base64

def main():
    flag_unicode = base64.b64decode(open("cipher.txt").read().strip()).decode()
    flag_ascii = "".join(chr(ord(x) & 0x7F) for x in flag_unicode)

    for key in range(128):
        plain = ''.join(chr(ord(x) ^ key) for x in flag_ascii)
        if "0ctf" in plain or "0CTF" in plain:
            print(plain)

main()
