#
# Solution to Project Euler problem 9, special Pythagorean triplet.
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
