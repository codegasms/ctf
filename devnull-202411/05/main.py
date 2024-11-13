n = 103805634552377307340975059685101156977551733461056876355507089800229924640064014138267791875318149345634740763575673979991819014964446415505372251293888861031929442007781059010889724977253624216086442025183181157463661838779892334251775663309103173737456991687046799675461756638965663330282714035731741912263
e = 3

# Old ciphertext
# ct = 36807405291227829946722625904846752484641543510616104153586462283445090666591458305243924348909195407301698490761768562279763256605817231339966516342326012142249280697475863856344306765521107962078223560717666866408244063806543074014844830136774239011450556740550932043244293525749137470268637092169849694895

ct = 4907569463567163286534620045778382788471193494073411855199998738500658001107047939686935892008454054704529623035112662897277333364306366391675908317839492077936418953775461


def icbrt(n: int) -> int:
    """Find largest no. x such that x^3 <= n using binary search."""
    lo, hi = -1, n + 1
    while lo + 1 < hi:
        mi = (lo + hi) // 2
        if mi * mi * mi <= n:
            lo = mi
        else:
            hi = mi
    return lo


x = icbrt(ct)
assert abs(x**3 - ct) == 0
print(x.to_bytes((x.bit_length() + 7) // 8, "big").decode())

# Ignore below this line. It contains tests for the old ciphertext.
exit()

print(e.bit_length(), ct.bit_length(), n.bit_length())


"""
c = ct

for _ in range(1000000):
    cbrt = icbrt(c)
    if cbrt**3 == c:
        print(c, cbrt)
    c += n
"""


print(f"{ct:0256x}")
print(f"{n:0256x}")

for pad_len in range(5, 100):
    pad = "+" * pad_len
    flag = f"ENIGMA{{{pad}}}"
    # print(flag)

    encrypted_flag = pow(int.from_bytes(flag.encode(), "big"), e, n)
    es = f"{encrypted_flag:0256x}"
    cs = f"{ct:0256x}"

    print(pad_len)
    print(es)
    print(cs)
    print()

    """
    for i in range(len(es)):
        if es[i] != cs[i]:
            break
    print(i)
    """
