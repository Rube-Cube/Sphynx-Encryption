from traceback import print_exc
from typing import Optional

from constants import PRIMES, KEY_LENGTH_EXCEPTION
primes = sorted(PRIMES)

'''
this function takes an input string,
breaks it into strings of prime number lengths,
then uses a custom hash to form a longer string
'''
def prime_hash(key: Optional[str] = ""):
    if not key:
        raise Exception("no key entered")
    largest_prime = primes[-1]
    if not largest_prime:
        raise Exception("primes not found")
    if len(key) > largest_prime:
        raise Exception(KEY_LENGTH_EXCEPTION)

    '''ok now the real work begins'''

    '''create list of strings starting with the original key, followed by slices of prime lengths'''
    key_slices = []
    for prime in primes:
        if len(key) > prime:
            key_slices.append(key[0:prime])
        if len(key) < prime:
            key_slices.append(key)
            break
    return key_slices