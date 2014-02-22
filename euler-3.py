# Project Euler problem 3, largest prime factor.
# http://projecteuler.net/problem=3

import math
import timeit

def is_prime(primes, n):
    """ Returns true if n is a prime number, false otherwise. n is
        determined to be a prime if it cannot be divided by any of the
        previously found primes.

    Arguments:
        primes -- prime numbers found.
        n -- number.
        
    """
    for p in primes:
        if n % p == 0:
            return False
    return True

def find_primes(n):
    """ Finds all prime numbers in the range [2,n].

    Arguments:
        n -- upper limit of range.
        
    """
    primes = []
    
    for p in xrange(2, n + 1):
        if is_prime(primes, p):
            primes.append(p)            
    return primes

def find_factor(n):
    """ Finds the largest prime factor of n.

    Arguments:
        n -- number.
        
    """
    max_factor = int(math.sqrt(n))
    
    for p in reversed(find_primes(max_factor)):
        if n % p == 0:
            return p
    return None
    
def main():
    """ Prints the largest prime factor found for the number
        600851475143.

    """
    print 'Answer: %s' % find_factor(600851475143);

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
