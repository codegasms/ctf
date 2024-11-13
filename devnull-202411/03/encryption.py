import string
from itertools import cycle


def encrypt1(text: str, key: str) -> str:
    num_columns = len(key)
    text_padded = text.ljust((len(text) + num_columns - 1) // num_columns * num_columns)
    columns = ["" for _ in range(num_columns)]

    for i, char in enumerate(text_padded):
        columns[i % num_columns] += char

    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = "".join(columns[i] for i in key_order)
    return encrypted_text


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


def encrypt3(text: str, substitution_alphabet: dict) -> str:
    return "".join(substitution_alphabet.get(char, char) for char in text)


def encrypt(text: str, key: str) -> str:
    alphabet = list(string.ascii_lowercase)
    shuffled_key = sorted(set(key), key=key.index)
    remaining_chars = [char for char in alphabet if char not in shuffled_key]
    substitution_order = shuffled_key + remaining_chars
    substitution_alphabet = dict(zip(alphabet, substitution_order))

    level_1_encryption = encrypt1(text.lower(), key)
    level_2_encryption = encrypt2(level_1_encryption, key)
    return encrypt3(level_2_encryption, substitution_alphabet)


if __name__ == "__main__":
    key = "securekey"
    key = key.lower()
    plaintext = (
        "WAh, you've found your way here—impressive. "
        "If you're truly here to seek the flag, "
        "then your efforts have earned you a reward. "
        "Here is what you came for: ENIGMA{RANDOM_FLAG}"
    )
    encrypted_text = encrypt(plaintext, key)

    with open("encrypted.txt", "w") as f:
        f.write(encrypted_text)
