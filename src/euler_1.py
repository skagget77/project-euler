#
# Solution to Project Euler problem 1, multiples of 3 and 5.
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

def main():
    """ Prints the sum of all multiples of 3 and 5 for numbers below
        1000.

    """
    multiples = []
    
    for n in xrange(1000):
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)

    print 'Answer: %s' % sum(multiples)

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
