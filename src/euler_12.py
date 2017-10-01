#
# Solution to Project Euler problem 12, highly divisible triangular
# number.
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

def count_factors(number):
    """ Count the factors of the specified number.

    Argumnets:
        number -- number.

    """
    factors = 0

    for n in xrange(1, long(math.floor(math.sqrt(number)))):
        if number % n == 0:
            factors += 2

    return factors
            
def main():
    """ Finds the first triangle number to have over 500 divisors.

    """
    n = 1
    t = 1

    while count_factors(t) < 500:
        n += 1
        t += n

    print 'Answer: %d' % t
        
if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
