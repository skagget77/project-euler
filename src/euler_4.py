# Project Euler problem 4, largest palindrome product.
# http://projecteuler.net/problem=4

import timeit

def is_palindrome(n):
    """ Returns true if the string representation of n match it's
        reverse, false otherwise.

    Arguments:
        n -- number.
        
    """
    s = str(n)
    return s == s[::-1]

def main():
    """ Print the largest palindrome found in the product between two
        3 digit numbers.
        
    """
    palindromes = []

    for p in xrange(999):
        for q in xrange(999):
            n = p * q
            if is_palindrome(n):
                palindromes.append(n)

    print 'Answer: %d' % max(palindromes)

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
