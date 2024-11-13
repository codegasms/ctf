# 5. EnigmasOrigin

## Flag

```
ENIGMA{0r1giN_0f_3N1GM4}
```

## Solution

The original challenge had the problem that the flag that was encrypted was too long and so the intended solution did not work.

After getting the new values:

```
n = 103805634552377307340975059685101156977551733461056876355507089800229924640064014138267791875318149345634740763575673979991819014964446415505372251293888861031929442007781059010889724977253624216086442025183181157463661838779892334251775663309103173737456991687046799675461756638965663330282714035731741912263
e = 3
ct = 4907569463567163286534620045778382788471193494073411855199998738500658001107047939686935892008454054704529623035112662897277333364306366391675908317839492077936418953775461
```

the solution seemed obvious that it was due to a very small plaintext. In the equation `c = m^3 % n`, if `m` is very small then `m^3` remains smaller than `n` and thus solution would be just to take integer cude root of `c`.

This solution is provided in the `main.py`. Running it prints the flag.

Additionally, `rsa_cbrt.jl` contains my Julia script for bruteforcing the solution in case `m^3 = nk + c` for some small `k` bellow `1e9`. It failed.
