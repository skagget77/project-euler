# Project Euler problem 2, even fibonacci numbers.
# http://projecteuler.net/problem=2

import timeit

def fibonacci_sequence(stop):
    """ Generates numbers from the Fibonacci sequence between 1 and
        stop.

    Arguments:
        stop -- largest Fibonacci number to generate.
        
    """
    a, b = 0, 1

    while a + b < stop:
        yield a + b
        a, b = b, a + b
    

def main():
    """ Prints the sum of all even Fibonacci numbers smaller than 4
        million.

    """
    fibsum = 0

    for n in fibonacci_sequence(4000000):
        if n % 2 == 0:
            fibsum += n

    print 'Answer: %s' % fibsum

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
