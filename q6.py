
"""
Question 6

Give a polynomial-time reduction from 3DM to 4DM.

In other words, given a 3DM problem T (a set of triples) over a set A, we must generate
a set U of quadruples (a 4DM problem) over the same set A, such that U has a solution
if and only if T does.

TASK 1: Implement the 'translate3DMto4DM' function, whose skeleton is given below.
TASK 2: Prove that your function works in polynomial time.
"""

from util import generateSetOfTriples

n = 5
T = generateSetOfTriples(n, 12)

print
print 'Problem set T:'
print T


def translate3DMto4DM(n, T):
    """
    :param n: the size of the set A
    :param T: a set of triples of elements of A
    :return: a set of quadruples U of elements of A, that has a 4DM solution IFF T has a 3DM solution
    """
    U = set()

    # No hints this time...
    pass  # TODO

    return U


U = translate3DMto4DM(n, T)

print
print 'Equivalent 4DM problem U:'
print U
