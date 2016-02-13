# Project Euler problem 9, special Pythagorean triplet.
# http://projecteuler.net/problem=9

import timeit

def find_triplet():
    """ Finds the Pythagorean triplet and exit early.

    Raises:
        RuntimeError -- when no triplet is found.

    """
    for c in xrange(3, 998):
        for b in xrange(2, c):
            for a in xrange(1, b):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a * b * c
    raise RuntimeError
    

def main():
    """ Finds the first and only Pythagorean triplet who's sum is
        1000.

    """
    try:
        print 'Answer: %d' % find_triplet()
    except:
        print 'No answer found'

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
