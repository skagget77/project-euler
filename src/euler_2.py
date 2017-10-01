#
# Solution to Project Euler problem 2, even fibonacci numbers.
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

def fibonacci_sequence(stop):
    """ Generates numbers from the Fibonacci sequence between 1 and
        stop.

    Arguments:
        stop -- largest Fibonacci number to generate.
        
    """
    a, b = 0, 1

    while a + b < stop:
        yield a + b
        a, b = b, a + b
    

def main():
    """ Prints the sum of all even Fibonacci numbers smaller than 4
        million.

    """
    fibsum = 0

    for n in fibonacci_sequence(4000000):
        if n % 2 == 0:
            fibsum += n

    print 'Answer: %s' % fibsum

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
