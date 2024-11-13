import string
from itertools import cycle
from collections import Counter
import random


def encrypt1(text: str, key: str) -> str:
    num_columns = len(key)
    text_padded = text.ljust((len(text) + num_columns - 1) // num_columns * num_columns)
    columns = ["" for _ in range(num_columns)]

    for i, char in enumerate(text_padded):
        columns[i % num_columns] += char

    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = "".join(columns[i] for i in key_order)
    return encrypted_text


def decrypt1(encrypted_text: str, key: str) -> str:
    num_columns = len(key)
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    assert len(encrypted_text) % num_columns == 0
    column_len = len(encrypted_text) // num_columns
    columns = [None] * num_columns

    for i, k in enumerate(key_order):
        columns[k] = encrypted_text[i * column_len : (i + 1) * column_len]
    text = "".join("".join(row) for row in zip(*columns))
    return text.rstrip(" ")


def encrypt2(text: str, key: str) -> str:
    encrypted_text = []
    for char, key_char in zip(text, cycle(key)):
        if char.isalpha():
            shift = ord(key_char.lower()) - ord("a")
            encrypted_char = chr(
                ((ord(char.lower()) - ord("a") + shift) % 26) + ord("a")
            )
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return "".join(encrypted_text)


def decrypt2(encrypted_text: str, key: str) -> str:
    text = []
    for encrypted_char, key_char in zip(encrypted_text, cycle(key)):
        if encrypted_char.isalpha():
            shift = ord(key_char.lower()) - ord("a")
            char = chr(
                ((ord(encrypted_char.lower()) - ord("a") - shift) % 26) + ord("a")
            )
            text.append(char)
        else:
            text.append(encrypted_char)
    return "".join(text)


def encrypt3(text: str, substitution_alphabet: dict) -> str:
    return "".join(substitution_alphabet.get(char, char) for char in text)


def encrypt(text: str, key: str) -> str:
    alphabet = list(string.ascii_lowercase)
    shuffled_key = sorted(set(key), key=key.index)
    remaining_chars = [char for char in alphabet if char not in shuffled_key]
    substitution_order = (
        shuffled_key + remaining_chars
    )  # implies only ASCII lowercase key
    substitution_alphabet = dict(zip(alphabet, substitution_order))

    level_1_encryption = encrypt1(text.lower(), key)
    level_2_encryption = encrypt2(level_1_encryption, key)
    return encrypt3(level_2_encryption, substitution_alphabet)


def decrypt(encrypted_text: str, key: str) -> str:
    alphabet = list(string.ascii_lowercase)
    shuffled_key = sorted(set(key), key=key.index)
    remaining_chars = [char for char in alphabet if char not in shuffled_key]
    substitution_order = shuffled_key + remaining_chars
    reverse_substitution_alphabet = dict(zip(substitution_order, alphabet))

    level_2_encryption = encrypt3(encrypted_text, reverse_substitution_alphabet)
    level_1_encryption = decrypt2(level_2_encryption, key)
    text = decrypt1(level_1_encryption, key)
    return text


def test():
    for _ in range(10_000):
        text = (
            "".join(
                random.choices(
                    string.ascii_letters + string.digits + " ", k=random.randint(1, 300)
                )
            )
            .lower()
            .rstrip()
        )
        key = "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 20)))

        assert decrypt1(encrypt1(text, key), key) == text
        assert decrypt2(encrypt2(text, key), key) == text

        alphabet = list(string.ascii_lowercase)
        shuffled_key = sorted(set(key), key=key.index)
        remaining_chars = [char for char in alphabet if char not in shuffled_key]
        substitution_order = shuffled_key + remaining_chars

        substitution_alphabet = dict(zip(alphabet, substitution_order))
        reverse_substitution_alphabet = dict(zip(substitution_order, alphabet))

        assert (
            encrypt3(
                encrypt3(text, substitution_alphabet), reverse_substitution_alphabet
            )
            == text
        )
        assert decrypt(encrypt(text, key), key) == text


if __name__ == "__main__":
    with open("encrypted.txt") as f:
        encrypted_flag = f.read()

    key = "enigma"
    flag = decrypt(encrypted_flag, key)
    print(flag)

# The old name == main section.
if False:
    # test()

    key = "securekey"
    key = "secureke\n"
    key = key.lower()

    plaintext = (
        "WAh, you've found your way here—impressive. "
        "If you're truly here to seek the flag, "
        "then your efforts have earned you a reward. "
        "Here is what you came for: ENIGMA{RANDOM_FLAG}"
    )

    with open("encrypted.txt") as f:
        encrypted_text_from_file = f.read()

    c1 = Counter(plaintext.lower())
    c2 = Counter(encrypted_text_from_file)
    print(c1)
    print(c2)
    exit()
    # print(decrypt(encrypted_text_from_file, "keysecure")); exit()

    for random_flag_len in range(5, 400):
        new_plaintext = plaintext.replace("RANDOM_FLAG", "A" * random_flag_len).lower()
        assert decrypt1(encrypt1(new_plaintext, key), key) == new_plaintext
        assert decrypt2(encrypt2(new_plaintext, key), key) == new_plaintext
        assert (
            decrypt1(decrypt2(encrypt2(encrypt1(new_plaintext, key), key), key), key)
            == new_plaintext
        )
        enc2 = encrypt2(encrypt1(new_plaintext, key), key)
        enc2 = encrypt(new_plaintext, key)
        assert "\n" in enc2
        print(random_flag_len, repr(enc2), end="\n\n")
        continue
        if len(enc2) != len(encrypted_text_from_file):
            continue
        print(random_flag_len, repr(enc2), end="\n\n")
        continue

        encrypted_text = encrypt(new_plaintext, key)
        diff = sum(
            a != b for a, b in zip(encrypted_text + "A" * 200, encrypted_text_from_file)
        )
        print(diff, random_flag_len)
        print(repr(new_plaintext))
        print(repr(encrypted_text))

    """
    with open("encrypted.txt", "w") as f:
        f.write(encrypted_text)
    """

    # print(decrypt(encrypted_text, key))
    # print(decrypt(encrypted_text_from_file, key))
