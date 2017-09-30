# Project Euler problem 21, amicable numbers.
# http://projecteuler.net/problem=21

import timeit

def divisors_sum(n):
    """ Returns the sum of all proper divisors to the given number.

    Arguments:
        n -- number.

    """
    d = 0

    for k in xrange(1, n / 2 + 1):
        if n % k == 0:
            d += k

    return d

def main():
    """ Prints the sum of all amicable numbers under 10000. """
    amicable_sum = 0

    # 1 has no proper divisors.
    for n in xrange(2, 10000):
        d = divisors_sum(n)
        
        if n != d and n == divisors_sum(d):
            amicable_sum += n
            
    print 'Answer: %d' % amicable_sum


if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
