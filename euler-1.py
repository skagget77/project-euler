# Project Euler problem 1, multiples of 3 and 5.
# http://projecteuler.net/problem=1

import timeit

def main():
    """ Prints the sum of all multiples of 3 and 5 for numbers below
        1000.

    """
    multiples = []
    
    for n in xrange(1000):
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)

    print 'Answer: %s' % sum(multiples)

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
