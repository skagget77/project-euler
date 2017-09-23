# Project Euler problem 20, factorial digit sum.
# http://projecteuler.net/problem=20

import math
import timeit

def main():
    """ Prints the sum of the digits in the number 100! """
    n, d = math.factorial(100), 0

    for c in str(n):
        d += int(c)
    
    print 'Answer: %s' % d

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
