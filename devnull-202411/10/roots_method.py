roots = [69, 147, 220, 291, 368, 433, 556, 658, 707, 817, 914, 990, 1085, 1183, 1231, 1314, 1367, 1462, 1561, 1637, 1745, 1796, 1893, 2007, 2058, 2126, 2251]
flag = ""
prev = 0

for i, x in enumerate(roots):
    flag += chr(x - prev)
    prev = roots[i]

print(flag)