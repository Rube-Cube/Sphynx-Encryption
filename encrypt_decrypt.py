'''this file contains the main encryption/decryption functionality'''

from typing import Callable

from constants import PLACEHOLDER_HASHING_MODULUS
def hash_string(input_string: str, key: str, func: Callable) -> str:
    chars = list(input_string)
    key_chars = list(key)
    hashed = ""
    for i in range(0, len(chars)):
        #debug print
        #print(chars[i%len(chars)], " + ", key_chars[i%len(key_chars)], " -> ", func(chars[i%len(chars)], key_chars[i%len(key_chars)]))
        hashed += func(chars[i%len(chars)], key_chars[i%len(key_chars)])
    return hashed

def encrypt_char(char: str, key_char: str) -> str:
    return chr((ord(char) + ord(key_char)) % PLACEHOLDER_HASHING_MODULUS)

def decrypt_char(char: str, key_char: str) -> str:
    return chr((ord(char) - ord(key_char)) % PLACEHOLDER_HASHING_MODULUS)


#debug print
"""
message = "hello world"
key = "supersecret"
encrypted = hash_string(message, key, encrypt_char)
print(encrypted)
decrypted = hash_string(encrypted, key, decrypt_char)
print(decrypted)
"""