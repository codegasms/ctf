# 7. Git Challenge

## Flag

```
ENIGMA{c0mm1t_0r_d13_try1ng_8548f6c834f4a9e55e6553b12ab92dbd}
```

## Solution

There are a few commits in the repo. Doing `git checkout HEAD~` to check the parent commit of `main` shows some part of the flag in `main.py`. Doing it one more time gives away the starting part too.
