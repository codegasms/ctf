# 09. NumberplateMadness

## Flag

```
ENIGMA{LSB_ST3g_bF9laXZFbF9TRVZlbl83XwgDinDp8+zPHSBGj/NRmeWdKH0BnBtUensV/p5Z8xGdLGFPxDi5fjWYLTkhBuFkUQ==}
```

## Solution

Running `python main.py | strings -n 12 | uniq` prints out some suspicious looking text.

```
NDU0RTQ5NDc0RDQxN0I0QzUzNDI1RjUzNTQzMzY3NUY2MjQ2Mzk2QzYxNTg1QTQ2NjI0NjM5NTQ1MjU2NUE2QzYyNkMzODMzNTg3NzY3NDQ2OTZFNDQ3MDM4MkI3QTUwNDg1MzQyNDc2QTJGNEU1MjZENjU1NzY0NEI0ODMwNDI2RTQyNzQ1NTY1NkU3MzU2MkY3MDM1NUEzODc4NDc2NDRDNDc0NjUwNzg0NDY5MzU2NjZBNTc1OTRDNTQ2QjY4NDI3NTQ2NkI1NTUxM0QzRDdE
```

It looks like base64 encoded. Decoding it gives a hex string. Converting that into ASCII string gives out the flag.
