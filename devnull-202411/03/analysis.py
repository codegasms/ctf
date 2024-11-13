from main import decrypt1

with open("encrypted.txt") as f:
    encrypted_text_from_file = f.read()

for r in (2, 3, 4, 6, 8, 9, 12, 16, 18, 24):
    plaintext1 = decrypt1(encrypted_text_from_file, "a" * r)
    chunk_length = len(plaintext1) // r
    for i in range(0, len(plaintext1), chunk_length):
        print(repr(plaintext1[i : i + chunk_length]))

    print(f"\nShowing for key length = {r}")
    input("Hit ENTER to show the next iteration\n")
