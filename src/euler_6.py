# Project Euler problem 6, sum square difference.
# http://projecteuler.net/problem=6

import timeit

def main():
    """ Prints the difference between the square of the sum and the sum
        of the squares.

    """
    a, b = 0, 0
    
    for n in xrange(1, 101):
        a += n
        b += n ** 2

    print 'Answer %d' % (a ** 2 - b)

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
