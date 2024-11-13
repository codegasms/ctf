# 11. TheInvisibleMen

## Flag

```
ENIGMA{c2a4ebfd3d010764ec98fce00ec9cc30_50}
```

## Setup

```console
$ mkdir hazard
$ unzip TheInvisibleMen_e7be80d0ab78474aba4854b66cdac8cc.zip -d hazard
```

## Solution 1

The solution 1 is in `main.py`. Find the file named as the `U+feff` Unicode character. It contains base64 encoded string. Decoding that gives the "deciphered" message. Doing as the challenge description says and adding `count = 50` to the flag gives us the solution.

## Solution 2

```console
# Get the content of the said file
$ fd -t f '\ufeff' hazard -X cat
IEVOSUdNQXtjMmE0ZWJmZDNkMDEwNzY0ZWM5OGZjZTAwZWM5Y2MzMH0gY+KAjGZ2RlhaVA==

# Base64 decode the content
$ fd -t f '\ufeff' hazard -X cat | base64 -d
 ENIGMA{c2a4ebfd3d010764ec98fce00ec9cc30} c‌fvFXZT

# Count the characters in the file
$ fd -t f '\ufeff' hazard -X cat | base64 -d | wc -m
50

# Get only the flag
$ fd -t f '\ufeff' hazard -X cat | base64 -d | grep -Po 'ENIGMA{.+}'
ENIGMA{c2a4ebfd3d010764ec98fce00ec9cc30}

# Get the flag part without the trailing '}'
$ fd -t f '\ufeff' hazard -X cat | base64 -d | grep -Po 'ENIGMA{.+}' | cut -d '}' -f 1
ENIGMA{c2a4ebfd3d010764ec98fce00ec9cc30

# Place the count in the flag
$ fd -t f '\ufeff' hazard -X cat | base64 -d | grep -Po 'ENIGMA{.+}' | cut -d '}' -f 1 | xargs printf '%s_50}\n'
ENIGMA{c2a4ebfd3d010764ec98fce00ec9cc30_50}
```
