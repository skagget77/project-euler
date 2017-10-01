#
# Solution to Project Euler problem 14, longest Collatz sequence.
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
