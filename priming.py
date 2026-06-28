from math import lcm
from functools import reduce

from constants import PRIMES, KEY_LENGTH_EXCEPTION
primes = sorted(PRIMES)
'''
this function takes an input string,
breaks it into strings of prime number lengths,
then uses a custom hash to form a longer string
'''
def prime_hash(key: str = ""):
    '''exception handling'''
    if not key:
        raise Exception("no key entered")
    largest_prime = primes[-1]
    if not largest_prime:
        raise Exception("primes not found")
    if len(key) > largest_prime:
        raise Exception(KEY_LENGTH_EXCEPTION)

    '''actual code'''
    key_slices = slice_string(key, primes)
    primed_key = str(reduce(priming_helper, key_slices))
    return primed_key

'''create list of strings of provided lengths, followed by the full string'''
def slice_string(input_string: str, lengths: list[int]) -> list[str]:
    slices = []
    for length in lengths:
        if len(input_string) > length:
            slices.append(input_string[0:length])
        if len(input_string) < length:
            slices.append(input_string)
            break
    return slices

'''
not sure how to describe this other than it loops over both strings for 
the least common multiple of their respective lengths. thus producing a 
new string where each character has been hashed by every other character
'''
from encrypt_decrypt import encrypt_char
from constants import PLACEHOLDER_HASHING_MODULUS
def priming_helper(string1: str, string2: str) -> str:
    hashed = ""
    #debug print
    #print(f"hashing {string1} by {string2}")
    #print(lcm(len(string1),len(string2)))
    for char in range(0, lcm(len(string1), len(string2))):
        hashed += encrypt_char(string1[char%len(string1)], string2[char%len(string2)])
    return hashed

#debug print
#print(prime_hash("now longer"))