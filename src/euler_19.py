#
# Solution to Project Euler problem 19, counting Sundays.
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

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(y):
    """ Returns true if the given year is a leap year, false otherwise.

    Arguments:
        y -- year.

    """
    return y % 400 == 0 if y % 100 == 0 else y % 4 == 0

def next_sunday(y, m, d):
    """ Returns the date of next Sunday.

    Arguments:
        y -- year.
        m -- month.
        d -- day

    """
    days = days_in_month[m - 1]

    # Adjust for leap year in february.
    if m == 2 and is_leap_year(y):
        days += 1

    # Step to next Sunday.
    d += 7

    # Handle overflow.
    if d > days:
        m += 1
        d %= days

        if m > 12:
            y += 1
            m = 1

    return y, m, d

def sundays(start, stop):
    """ Returns a generator iterating over all Sundays in the given
        interval. Each Sunday is returned as a date.

    Arguments:
        start -- start date, must be a Sunday.
        stop -- stop date.

    """
    while start < stop:
        yield start
        start = next_sunday(*start)

def find_next_sunday(start, stop):
    """ Returns the date of the first Sunday after the given interval.

    Arguments:
        start -- start date, must be a Sunday.
        stop -- stop date.

    """
    for start in sundays(start, stop):
        pass

    return next_sunday(*start)
    

def main():
    """ Prints how many Sundays fell on the first of the month during
        the twentieth century.

    """
    count = 0

    # 1900-01-01 was a Monday, find first Sunday outside the specified
    # date interval.
    start = find_next_sunday((1900, 1, 7), (1901, 1, 1))

    # Count Sundays.
    for date in sundays(start, (2000, 12, 31)):
        if date[2] == 1:
            count += 1
    
    print 'Answer: %d' % count


if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3f' % duration
