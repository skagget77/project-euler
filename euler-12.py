# Project Euler problem 12, highly divisible triangular number.
# http://projecteuler.net/problem=12

import math
import timeit

def count_factors(number):
    """ Count the factors of the specified number.

    Argumnets:
        number -- number.

    """
    factors = 0

    for n in xrange(1, long(math.floor(math.sqrt(number)))):
        if number % n == 0:
            factors += 2

    return factors
            
def main():
    """ Finds the first triangle number to have over 500 divisors.

    """
    n = 1
    t = 1

    while count_factors(t) < 500:
        n += 1
        t += n

    print 'Answer: %d' % t
        
if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
