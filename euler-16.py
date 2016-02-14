# Project Euler problem 16, power digit sum.
# http://projecteuler.net/problem=16

import timeit
            
def main():
    """ Prints the sum of all digits making up the number 2^1000.

    """
    sum = 0

    for digit in str(2**1000):
        sum += int(digit)

    print 'Answer: %d' % sum
        
if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
