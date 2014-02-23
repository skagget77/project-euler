# Project Euler problem 10, summation of primes.
# http://projecteuler.net/problem=10

import timeit

def primes(stop):
    """ Generates prime numbers between 2 and stop using the sieve of
        Eratosthenes.

    Arguments:
        stop -- largest prime number generated.

    """
    s = range(2, stop, 1)

    # Sift primes.
    for n in s:
        if n:
            for i in xrange(2 * n - 2, stop - 2, n):
                s[i] = None

    for n in s:
        if n:
            yield n

def main():
    """ Prints the sum of all prime numbers smaller than 2 million.

    """
    print 'Answer: %d' % sum(sieve(2000000))

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration

