# DiffieRivestHellmanCipher [Cryptography]

## Description

Ever wondered how secret key exchange takes place?

`Attachments` :

1. [note.txt](./img/note.txt)
1. [note2.pdf](./img/note2.pdf)
1. [ciphertext.txt](./img/ciphertext.txt)

## Solution

`0CTF{Sh4r3d_s3cr3t_1s_n0t_4_s3cr3t_4nym0r3}`

## But How?

### Diffie-Hellman Key Exchange

We are given with the follwing text:

```plaintext
user 1 and user 2 get public keys as P=33 and G=8. User 1 selects private key as 3 and user 2 selects private key as 2. 
I guess this has something to do with key-exchange algorithm. 
What is the shared secret?
```

The shared secret can be calculated using the Diffie-Hellman Key Exchange algorithm, using the public keys `P` and `G` and the `private keys` of the users.

There are many online tools available to run the algorithm for you. The computed answer is `25`.

### The PDF

The PDF seems to be password protected and trying to open it with the shared secret as the password works. Inside it says

```plaintext
you got the shared secret? well done!!
The key to decrypt the flag is the square of the secret value!!
```

### Decrypting The Cipher

But which Cipher does it use? Well, the name of the challenge is `DiffieRivestHellmanCipher`, so it must be using the `Rivest Cipher`. Now we just have to figure out which one i.e. RC2,3,4,5 or 6.

Since there were no clue given, we can try all of them. Starting of with `RC2`, we can use any online tool to give the cipher along with the key to decrypt it.

> So, is the key '625'? Well, not exactly. And there were no other hint or clue.
>
> So, I began to try all possible ways to write '625' :
>
> 1. sixtwofive
> 2. six-two-five
> 3. six_two_five
> 4. sixhundredtwentyfive
> 5. six-hundred-twenty-five
> 6. six_hundred_twenty_five
> 7. `sixtwentyfive` -------> And this was the key
