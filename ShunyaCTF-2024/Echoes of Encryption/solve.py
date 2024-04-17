import random
import string


def encrypt_string(input_string, seed):
    random.seed(seed)

    allowed_chars = string.ascii_letters + string.digits
    key = "".join(random.choices(allowed_chars, k=len(input_string)))
    plain = ""
    for i in range(len(input_string)):
        plain += chr(ord(input_string[i]) ^ ord(key[i]))
    return plain


# https://nvd.nist.gov/vuln/detail/CVE-2022-42269
seed_value = 2022_42269
input_string = bytes.fromhex(open("cipher").read().strip()).decode()
encrypted = encrypt_string(input_string, seed_value)
print(encrypted)
