# AESthetic challenge

## Description

"I have got these two creepy audio files. I guess they have something to tell us. What could be the message?"

## Flag

```
0CTF{d4sh_und3rsc0r3_d0t!}
```

## Solution

We can analyze the two wave files in Audacity and get a Morse code like pattern.

Using an online decoder (https://morsecode.world/international/decoder/audio-decoder-adaptive.html) gives the following data from both the files.

aud1_IV.wav: `0 X 0 0 0 1 0 2 0 3 0 4 0 5 0 6 0 7 0 8 0 9 0 A 0 B 0 C 0 D 0 E 0 F`
aud2_k.wav : `Y O U G O T T H E K E Y N J O Y`

It took me a while to realize that Morse code is not case sensitive so the key can be any of lowercase or uppercase.

Since this challenge is named `AESthetic` and it has a file named `IV` and a key, it is a safe assumption that the cipher text can be decrypted using a mode which requires an IV. Trying a common one of those modes CBC gives the flag.

The solution can be found in `solve.py`.

The output after running this gives:

```
$ python solve.py 
b'0CTF{d4sh_und3rsc0r3_d0t!}\x06\x06\x06\x06\x06\x06'
```

## References

## Attachments

- [aud1_IV.wav](https://drive.google.com/file/d/1Nr6zAfUViMFw3T6bKz1YainnaxNIVtvM/view)
- [aud2_k.wav](https://drive.google.com/file/d/1FFWWgpg3SdmbfmSBP0HLcwyToPZHbjDJ/view)
- [ciphertext.txt](https://drive.google.com/file/d/1k60GuNO8vLyp14yQwEMqg_Cs-YWom-jW/view)
