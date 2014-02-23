# Project Euler problem 7, 10001st prime.
# http://projecteuler.net/problem=7

import timeit

def is_prime(primes, n):
    """ Returns true if the specified number is a prime number. The
        number is determined to be prime if it cannot be divided by any
        of the previously seen primes.

    Arguments:
        prime -- previously seen prime numbers.
        n -- number.

    """
    for p in primes:
        if n % p == 0:
            return False
    return True

def main():
    """ Prints the 10001st prime number. """
    primes, n = [], 2

    while len(primes) < 10001:
        if is_prime(primes, n):
            primes.append(n)
        n += 1

    print 'Answer: %d' % primes[-1]
        

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
