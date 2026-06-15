primes = [2, 3, 5, 7, 11, 13, 17, 23]

'''

this function takes an input string,
breaks it into strings of prime number lengths,
then adds them together to form a longer string
'''
def prime_hash(text: str):
    if len(text) > primes[-1]:
        raise Exception("too long.\nseriously?\nwhat are you trying to encrypt?\nThe Library of Babel?")
    greatest_so_far = int('-inf')
    for prime in primes:
        if prime > greatest_so_far and greatest_so_far < len(text):
            greatest_so_far = prime
