# Rivest Salted Adleman

## Description

"Bob told me original q was eksored with some secret value `1` 2 `9` or 1 thru 9 something like that.... ughhh I am so confused...."

## Flag

```
0CTF{4sa_1s_l0v3}
```

## Solution

From observation this seems like a fairly simple RSA challenge.

The description states that `q` is XORed with some secret key and we only have access to this `salted_q`. `p` is given as it is.

So, the only challenge is figuring out the key. Again the description text helps us in limiting the possibility to a few set of keys which are `{1, 2, 3, 4, 5, 6, 7, 8, 9, 123456789}`. That last one tooks some while to figure out what it meant by "1 tru 9".

It is simple RSA decryption afterwards.

The solution can be found in `solve.py`.

The output after running this gives:

```
$ python solve.py 
0CTF{4sa_1s_l0v3}
```

## References

## Attachments

- [ciphertext](https://drive.google.com/file/d/1XN-8-Ctcck3STSo4OxLsoqrPpZ__fkcl/view)
- [note](https://drive.google.com/file/d/1t68CpbeggRyXjddrcxwv23xG4Bbu5L59/view)
