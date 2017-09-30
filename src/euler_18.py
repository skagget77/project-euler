# Project Euler problem 18, maximum path sum 1.
# http://projecteuler.net/problem=18

import timeit

class Node:
    """ Each node instance has a weight and link to the heaviest path below
        going down to the bottom of the triangle.

    """
    def __init__(self, weight):
        """ Initializes a node instance with the specified weight.

        Arguments:
            weight -- Node weight.

        """
        self._weight = weight
        self._link = None

    def path_weight(self):
        """ Returns the weight of this node and the path below. """
        weight = self._weight
        node = self._link

        while node:
            weight += node._weight
            node = node._link

        return weight

    def link_max(self, left, right):
        """ Links this node to either left or right depending on which of the
            two nodes has the heavier path.

        Arguments:
            left -- Left node.
            right -- Right node.

        """
        if left.path_weight() > right.path_weight():
            self._link = left
        else:
            self._link = right

def read_triangle(filename):
    """ Reads a triangle from the named file.

    Arguments:
        filename -- File name.

    """
    triangle = []

    with open(filename) as rows:
        for row in rows:
            nodes = []

            for col in row.strip().split(' '):
                nodes.append(Node(int(col)))

            triangle.append(nodes)

    return triangle

def find_path_sum(triangle):
    """ Finds the path with the highest sum in the given triangle.

    Arguments:
        triangle -- Triangle.

    """
    # Start from the bottom of the triangle and move up towards the root.
    for row in xrange(len(triangle) - 1, 0, -1):
        for col in xrange(len(triangle[row]) - 1):
            # Parent, left and right.
            triangle[row - 1][col].link_max(triangle[row][col],
                                            triangle[row][col + 1])

    # Follow the path from the root down.
    return triangle[0][0].path_weight()

def main():
    """ Find the maximum sum from top to bottom of the triangle in the named
        file.

    """
    print 'Answer: %d' % find_path_sum(read_triangle('euler-18.input'))

if __name__ == '__main__':
    duration = timeit.timeit(main, number=1)
    print 'Duration: %.3fs' % duration
