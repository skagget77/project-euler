#
# Solution to Project Euler problem 4, largest palindrome product.
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
