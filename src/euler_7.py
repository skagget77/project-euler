#
# Solution to Project Euler problem 7, 10001st prime.
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

import timeit

def is_prime(primes, n):
    """ Returns true if the specified number is a prime number. The
        number is determined to be prime if it cannot be divided by any
        of the previously seen primes.

    Arguments:
        prime -- previously seen prime numbers.
        n -- number.

    """
    for p in primes:
        if n % p == 0:
            return False
    return True

def main():
    """ Prints the 10001st prime number. """
    primes, n = [], 2

    while len(primes) < 10001:
        if is_prime(primes, n):
            primes.append(n)
        n += 1

    print 'Answer: %d' % primes[-1]
  

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
