# Project Euler problem 14, longest Collatz sequence.
# http://projecteuler.net/problem=14

import timeit

def collatz(n):
    """ Returns the length of the Collatz sequence for the given
        number.

    Arguments:
        n -- number.

    """
    i = 1
    
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        i += 1
        
    return i
            
def main():
    """ Prints the number smaller than 1000000 that generates the
        longest Collatz sequence.

    """
    longest_seq = (0, 0)
    
    for n in xrange(1, 1000000):    
        longest_seq = max(longest_seq, (collatz(n), n))
            
    print 'Answer: %d' % longest_seq[1]

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
