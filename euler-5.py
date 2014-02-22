# Project Euler problem 5, smallest multiple.
# http://projecteuler.net/problem=5

import math
import timeit

def is_divisible(N, n):
    """ Returns true if n is divisible by all numbers in the range
        [1,N], false otherwise.

    Arguments:
        N -- upper limit of range.
        n -- number.
        
    """
    for r in xrange(2, N + 1):
        if n % r != 0:
            return False
    return True

def find(N):
    """ Returns the smallest number divisible by all numbers in the
        range [1,N].

    Arguments:
        N -- upper limit of range.

    Note:
        This function will probably fail for big N on 32-bit CPython
        implementations. 

    """
    p = math.factorial(N)

    for n in xrange(1, p):
        if is_divisible(N, n):
            return n

def main():
    """ Prints the smallest number that can be evenly divided by all
        numbers in the range [1,20].

    """
    print 'Answer: %d' % find(20)

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
