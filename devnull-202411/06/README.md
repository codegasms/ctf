# 6. FirstSteps

## Flag

```
ENIGMA{fd8abd1f770d242ee40a0e76d7b493552135a6cb4d53923f19659bab7dbce64f}
```

## Solution

```console
$ printf e7be80d0ab78474aba4854b66cdac8cc | sha256sum | cut -d ' ' -f 1 | xargs printf 'ENIGMA{%s}\n'
```
