#
# Solution to Project Euler problem 17, number letter counts.
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

# Maps from number to string of letters.
letters = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def to_letters(n):
    """ Returns the given number as a string of letters. Only work for numbers
        between 1 and 1000.

    Arguments:
        n -- Number.

    """
    s = ''

    if n < 1000:
        # Hundreds.
        q, r = divmod(n, 100)

        if q != 0:
            if r == 0:
                s += letters[q] + 'hundred'
            else:
                s += letters[q] + 'hundredand'

        # Tens and singular, special handling of 10 - 19.
        q, r = divmod(r, 10)

        if q == 1:
            s += letters[q * 10 + r]
        else:
            s += letters[q * 10] + letters[r]
    else:
        s = 'onethousand'

    return s

def main():
    """ Prints the length of the string containing the letters for all numbers
        between 1 and 1000.

    """
    s = ''

    for n in xrange(1, 1001):
        s += to_letters(n)

    print 'Answer: %d' % len(s)

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
