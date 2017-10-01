#
# Solution to Project Euler problem 21, amicable numbers.
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
