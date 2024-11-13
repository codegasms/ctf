from PIL import Image
import sys


with Image.open("image_e7be80d0ab78474aba4854b66cdac8cc.png") as im:
    assert im.mode == "RGB"
    flag = 0

    for i, (r, g, b) in enumerate(im.getdata()):
        if i % 8000 == 0:
            sys.stdout.buffer.write(flag.to_bytes(i * 3 // 8, "big"))

        flag = (flag << 1 | (b & 1))
        flag = (flag << 1 | (g & 1))
        flag = (flag << 1 | (r & 1))
