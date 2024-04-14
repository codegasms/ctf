flag = "ƃŰŶŉůļźŞŷŭŪƄŰŘŰŧŖŔŦĦŨĬƀźōşŋůĲňĳźĖőƃũťũŸŪĞ"
flag = [(~(-1 * (c - (6 * len(flag) + 15))) ^ i) for i, c in enumerate(map(ord, flag))]
print("".join(map(chr, flag))[::-1])
