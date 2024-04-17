# Simplistic Image Format

## Description

Some prefer jpg, some prefer png, I prefer hating myself and spending 2 days on making my own image format.

Author: @av1na5h

Flag Format: 0CTF{}

## Flag

```
0ctf{c0mpr355ion_1s_h@rd}
```

## Solution

The online web service seems to be a file uploading service that converts any common image format to a custom SIF format.

The description on the website says:

```
Simplistic Image Format
Done are the days of complicated image formats, introducing, the SIF format, custom made in simple python. Supports compression(LZMA for now), and grayscale, RGB, RGBA formats.
```

Testing this with custom images, one of which is `white.png` results in an `image.sif` file (renamed to `white.sif`).

We can see the hexdump of this file as:

```
$ hexyl white.sif 
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
│00000000│ 53 49 46 32 30 32 34 00 ┊ 00 00 2a 00 00 00 45 52 │SIF2024⋄┊⋄⋄*⋄⋄⋄ER│
│00000010│ 47 42 fd 37 7a 58 5a 00 ┊ 00 04 e6 d6 b4 46 02 00 │GB×7zXZ⋄┊⋄•×××F•⋄│
│00000020│ 21 01 16 00 00 00 74 2f ┊ e5 a3 e0 21 f5 00 28 5d │!••⋄⋄⋄t/┊×××!×⋄(]│
│00000030│ 00 7f ef fb bf fe a3 b1 ┊ 5e e5 f8 3f b2 aa 26 55 │⋄•××××××┊^××?××&U│
│00000040│ f8 68 70 41 70 15 0f 8d ┊ fd 1e 4c 1b 8a 42 b7 19 │×hpAp••×┊×•L•×B×•│
│00000050│ f4 69 18 71 aa c4 a4 9b ┊ 00 00 39 e9 a1 36 a4 ad │×i•q××××┊⋄⋄9××6××│
│00000060│ c4 d0 00 01 44 f6 43 00 ┊ 00 00 89 ce 49 19 b1 c4 │××⋄•D×C⋄┊⋄⋄××I•××│
│00000070│ 67 fb 02 00 00 00 00 04 ┊ 59 5a 54 48 45 45 4e 44 │g×•⋄⋄⋄⋄•┊YZTHEEND│
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
```

Getting the info of the original `white.png` file:

```
$ file white.png 
white.png: PNG image data, 42 x 69, 8-bit/color RGB, non-interlaced
```

The format seems to be something like:
```
b"SIF2024" | 4 byte big-endian image width | 4 byte big-endian image height | image mode (P, RGB, RGBA) | b"\xfd7zXZ" | ... | b"YZ" | b"THEEND"
```

We can match the width and the height in the SIF file with the original file.

The mode naming convention seems to line up with the Pillow Python imaging library.

As the website mentions (LZMA) and we can see a magic byte like thing `b"\xfd7zXZ"`. We can assume that this file embeds a `.xz` file inside it.

After testing with custom `.xz` files, we can see that `YZ` marks the end of the file. So, we can ignore the `b"THEEND"` part at the end.

I wrote a Python script to extract the `.xz` file but one can use `binwalk` too.

After decompressing the `.xz` file, we can get a raw image pixels data. We can simply transform this into a PPM file to view the image.

This entire process is covered in the `solve.py` script.

The output after running this gives a `flag.png` file which contains the flag.

## References

## Attachments

- [Flag.SIF](https://drive.google.com/file/d/14HG_oegDpm5EumRmz_H_WJnp91rcW1qW/view)
