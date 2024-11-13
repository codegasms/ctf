# 3. Cipher Chase

## Flag

```
ENIGMA{d3crypt!_c0mp13t3_857b1d4891cf5c9171c2e117b46e4d0e}
```

## Solution

After writing the inverse functions of `encrypt1`, `encrypt2`, `encrypt3` and `encrypt`, I tested them on randomly generated data to verify if my implementation was correct. There was some confusion about whether the `key = "securekey"` part and the `plaintext` format were just placeholders, they were. It can be verified by the fact that the `encrypted.txt` file contains `\n` characters whereas it's no where to be seen in the `plaintext`.

`encrypt1` splits the `text` into columns and shuffles them according to the key. Before that it pads the text. The given ciphertext has length of `288` bytes, which means that the key length must be a factor of this number. And, it has a lot of factors `1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 72, 96, 144, 288`.

After trying some key lengths in the `analysis.py` file, `6` gives some interesting pattern:

```
"ie,j m nd'rc lvijwimxe ugkt qhrmkdp—ddkwzwj.sv \n"
" wz'ki zremxatqg qhomsm f dj xby,t lwp vbkjeh jx"
'tema gee mmvivcd rmnl  c.kzdjm \nxhhlkud tm toyu '
'fbdq men :rmjqdu{oz3mxvdn!0oy_813t_3451ac758p1s9'
'hh7119c2117h044qp6lm\n\nm}kkmq hpaev  tdnqdxh zhzr'
'zg ,km gctm kfhm pyaerp qwjk ertedx ohglk  m . s'
```

mainly the `:rmjqdu{oz3mxvdn!0oy_813t_3451ac758p1s9' 'hh7119c2117h044qp6lm\n\nm}` parts. This means the key is of length 6. Guessing from some other portions that it contains lowercase alphabets only, I started writing a bruteforce program in C++ to find the solution since the key space is `26^6 = 308915776` which is doable. Mid way through I realized that `enigma` has 6 letters too. Trying that gives the flag. Run `python main.py` to see the result. Submit after uppercasing `enigma`.
