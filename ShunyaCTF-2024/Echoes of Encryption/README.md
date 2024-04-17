# Echoes of Encryption

## Description

In December 2022, my friend Alok's device was hacked. Upon investigation, he discovered that the breach was due to a vulnerability in the Nvidia SMC which had been recently discovered and published for research purposes on the same day he was hacked.

PS- In the end, only numbers matter to grow a plant from a seed!!

Flag Format: 0CTF{}

## Flag

```
0CTF{alw4y5_r3ad_7he_d3scr!pti0n_c4r3fully}
```

## Solution

Analyzing `encrypt.py`, we get that it is a simple XOR cipher with a randomly generated key. Thus, this challenge is reduced to finding the seed for the RNG.

The challenge description tells about some vulnerability. On searching it we can get a few correct results.

I randomly tried using the CVE number as the seed and it worked.

The output after running this gives:

```
$ python solve.py 
0CTF{alw4y5_r3ad_7he_d3scr!pti0n_c4r3fully}
```

## References

## Attachments

- [Echoes.zip](https://drive.google.com/drive/folders/1qmn66ZFtidXNxgXHZ0-w8kfaNbkCHsWO)
