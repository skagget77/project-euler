#
# Solution to Project Euler problem 10, summation of primes.
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

def primes(stop):
    """ Generates prime numbers between 2 and stop using the sieve of
        Eratosthenes.

    Arguments:
        stop -- largest prime number generated.

    """
    s = range(2, stop, 1)

    # Sift primes.
    for n in s:
        if n:
            for i in xrange(2 * n - 2, stop - 2, n):
                s[i] = None

    for n in s:
        if n:
            yield n

def main():
    """ Prints the sum of all prime numbers smaller than 2 million.

    """
    print 'Answer: %d' % sum(primes(2000000))

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration

