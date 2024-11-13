# 10. PolynomialTrolynomial

## Solution 1

The `question.py` script seems to be calculating the prefix sum array of ASCII repr of the flag string. It then checks if each element of that prefix sum array is a root of the given polynomial or not. It must be to be a correct flag. The script `roots_method.py` contains that solution.

## Solution 2

The second solution would be to iteratively find the roots of the polynomial. This can be done in `O(128 * |flag|)`. This is inside the `main.py` script, `solve` function.
