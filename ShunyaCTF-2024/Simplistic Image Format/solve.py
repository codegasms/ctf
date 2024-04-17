import lzma
from PIL import Image


with open("flag.SIF", "rb") as f:
    data = f.read()

xz_index = data.index(b"\xfd7zXZ")
metadata = data[7:xz_index]

width = int.from_bytes(metadata[:4], "big")
height = int.from_bytes(metadata[4:8], "big")

# Get the mode like L, P, RGB, RGBA.
mode = metadata[8:].decode()

print(width, height, mode)

# P messes up for some reason.
if mode == "P":
    mode = "L"

# Get the xz data ignoring the 6 bytes of b"THEEND" at the end of the file.
pixels_xz = data[xz_index:-6]
pixels_raw = lzma.decompress(pixels_xz)
assert len(pixels_raw) == width * height * len(mode)

with Image.frombytes(mode, (width, height), pixels_raw) as img:
    img.save("flag.png")
