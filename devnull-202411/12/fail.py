import wave
import sys
import itertools as it

ENDIANNESS = "little"


def stitch(num: int, mask: int):
    """Get the mask of the num and stitch those bits together."""
    acc = 0
    for i in range(mask.bit_length() - 1, -1, -1):
        if mask >> i & 1:
            acc <<= 1
            acc |= num >> i & 1
    return acc


assert stitch(0b10001, 0b11000) == 0b10


with wave.open("KSI.wav") as f:
    params = f.getparams()
    frames = f.readframes(params.nchannels * params.nframes)

print(f"{params = }")


mask = 0b0000_0000_0000_0011
bits_per_frame = mask.bit_count()
assert bits_per_frame == 2

acc = 0

for i, f in enumerate(it.batched(frames, params.sampwidth)):
    acc_len = i * bits_per_frame
    if acc_len % 80000 == 0:
        # print(i)
        sys.stdout.buffer.write(acc.to_bytes((acc.bit_length() + 7) // 8, "big"))
        acc = 0

    frame = int.from_bytes(f, ENDIANNESS)
    acc <<= bits_per_frame
    acc |= frame & mask
    # acc |= stitch(frame, mask)

"""
eq, ne = [], []

for ch1, ch2 in it.batched(it.batched(frames, params.sampwidth), params.nchannels):
    if ch1 != ch2:
        ne.append((ch1, ch2))
        # print("NE")
    else:
        eq.append((ch1, ch2))
        # print("EQ")

print(len(eq))
print(len(ne))
# print(acc.to_bytes((acc.bit_length() + 7) // 8, "big"))
"""
