#
# Solution to Project Euler problem 3, largest prime factor.
# Copyright (C) 2017  Johan Andersson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import math
import timeit

def is_prime(primes, n):
    """ Returns true if n is a prime number, false otherwise. n is
        determined to be a prime if it cannot be divided by any of the
        previously found primes.

    Arguments:
        primes -- prime numbers found.
        n -- number.
        
    """
    for p in primes:
        if n % p == 0:
            return False
    return True

def find_primes(n):
    """ Finds all prime numbers in the range [2,n].

    Arguments:
        n -- upper limit of range.
        
    """
    primes = []
    
    for p in xrange(2, n + 1):
        if is_prime(primes, p):
            primes.append(p)            
    return primes

def find_factor(n):
    """ Finds the largest prime factor of n.

    Arguments:
        n -- number.
        
    """
    max_factor = int(math.sqrt(n))
    
    for p in reversed(find_primes(max_factor)):
        if n % p == 0:
            return p
    return None
    
def main():
    """ Prints the largest prime factor found for the number
        600851475143.

    """
    print 'Answer: %s' % find_factor(600851475143);

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
