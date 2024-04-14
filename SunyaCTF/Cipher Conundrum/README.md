# Cipher Conundrum

## Description

Can you find what's going on!!!!!!!

Flag Format: 0CTF{}

## Flag

```
0CTF{5ome7im3s_i7_ne3d5_t0_b3_c0mpl3x}
```

## Solution

python solve.py | rg --text --ignore-case 0CTF

Analyzing the `encrypt.py` script, we can observe that it just XORs the flag with some key (unknown) and then dumps it in base64 encoding.

It is a fair assumption that the flag is ASCII only.

So, the line:

```
encrypted = ''.join([chr(ord(x) ^ int(key, 16)) for x in data])
```

gives a sequence of chars where each char differs by the key only in the last 7 bits (0 <= ord(x) < 128).

If we get back the chars after b64 decode then we can retain only the LSB 7 bits of each char and bruteforce all the possible keys in this range [0, 128).

Decode the cipher text to get all the chars:

```py
    flag_unicode = base64.b64decode(open("cipher.txt").read().strip()).decode()
```

Retain only the valid bits:

```py
    flag_ascii = "".join(chr(ord(x) & 0x7F) for x in flag_unicode)
```

Bruteforce the key and get the flag:

```py
    for key in range(128):
        plain = ''.join(chr(ord(x) ^ key) for x in flag_ascii)
        if "0ctf" in plain or "0CTF" in plain:
            print(plain)
```

This script is in `solve.py`.

The output after running this gives:

```
$ python solve.py 
0CTF{5ome7im3s_i7_ne3d5_t0_b3_c0mpl3x}
```

## References

## Attachments

- [Ciphers.zip](https://drive.google.com/drive/folders/1sx_qXRzu55VWtu-H647WOH2OFuiZaOVg)
