# One Liner

## Description

I love shortcuts

```py
flag = "ƃŰŶŉůļźŞŷŭŪƄŰŘŰŧŖŔŦĦŨĬƀźōşŋůĲňĳźĖőƃũťũŸŪĞ"
flag = [~(c^i)*(-int(1/(5**0.5) * ((1 + 5**0.5)**1 / 2 - (1 - 5**0.5)**1 / 2))) + len(flag) * 6 + 15 for i, c in enumerate([ord(a) for a in flag[::-int(1/(5**0.5) * ((1 + 5**0.5)**1 / 2 - (1 - 5**0.5)**1 / 2))]])]
print(tostr(flag))

#  0CTF{___R___E__D___A___C____T_____E____D______}
```

Author: @av1na5h

Flag Format: 0CTF{}

## Flag

```
0CTF{@_j0k3_0r_@_cl3v3r_@nd_funny_r3m@rk}
```

## Solution

We can format the slightly obfuscated code to get a better look.

```py
flag = "ƃŰŶŉůļźŞŷŭŪƄŰŘŰŧŖŔŦĦŨĬƀźōşŋůĲňĳźĖőƃũťũŸŪĞ"
flag = [
    ~(c ^ i) * (-int(1 / (5**0.5) * ((1 + 5**0.5) ** 1 / 2 - (1 - 5**0.5) ** 1 / 2)))
    + len(flag) * 6
    + 15
    for i, c in enumerate(
        [
            ord(a)
            for a in flag[
                :: -int(1 / (5**0.5) * ((1 + 5**0.5) ** 1 / 2 - (1 - 5**0.5) ** 1 / 2))
            ]
        ]
    )
]
print(tostr(flag))

#  0CTF{___R___E__D___A___C____T_____E____D______}
```

The `-int(1 / (5**0.5) * ((1 + 5**0.5) ** 1 / 2 - (1 - 5**0.5) ** 1 / 2))` expression is used twice and it is a compile-time constant that evaluates to `-1`. So we can safely replace it with this value. This gives:

```py
flag = "ƃŰŶŉůļźŞŷŭŪƄŰŘŰŧŖŔŦĦŨĬƀźōşŋůĲňĳźĖőƃũťũŸŪĞ"
flag = [
    ~(c ^ i) * -1 + len(flag) * 6 + 15
    for i, c in enumerate([ord(a) for a in flag[::-1]])
]
print(tostr(flag))

#  0CTF{___R___E__D___A___C____T_____E____D______}
```

This seems to be doing some operations including the variables `char`, `index of the char`, `length of the flag string`.

The operations are XOR char ordinal with the index -> ones' complement -> negation -> add len(flag) * 6 + 15.

We can reverse those operations in exactly the same order (subtract len(flag) * 6 + 15 -> negation -> ones' complement -> XOR char ordinal with the index) like:

```py
flag = "ƃŰŶŉůļźŞŷŭŪƄŰŘŰŧŖŔŦĦŨĬƀźōşŋůĲňĳźĖőƃũťũŸŪĞ"
flag = [(~(-1 * (c - 15 - 6 * len(flag))) ^ i) for i, c in enumerate(map(ord, flag))]
print("".join(map(chr, flag))[::-1])
```

The output after running this gives:

```
$ python solve.py 
0CTF{@_j0k3_0r_@_cl3v3r_@nd_funny_r3m@rk}
```

## References

## Attachments
