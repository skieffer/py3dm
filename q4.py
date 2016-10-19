
"""
Question 4

For a 3DM problem T (a set of triples), any solution S would serve as a certificate.

We need to show how we can check in polynomial time that S is indeed a solution to
the given problem T.

TASK 1: Implement the 'checkSolution' function, whose skeleton is given below.
TASK 2: Prove that your function works in polynomial time.
"""

from generate import generateSetOfTriples

n = 5
T = generateSetOfTriples(n, 12)
S = generateSetOfTriples(n, n)

print
print 'Problem set T:'
print T

print
print 'Possible solution set S:'
print S

def checkSolution(n, T, S):
    """
    :param n: the size of the set A
    :param T: a set of triples of elements of A
    :param S: a possible solution, i.e. possible 3-dimensional matching for T
    :return: boolean, saying whether S actually is a solution

    Things to be checked:

    (1) S is of the right size
    (2) Every element of S is an element of T
    (3) No two elements of S overlap

    And all of this must be done in polynomial time -- no exponential algorithms!
    """

    # (1) S is of the right size
    pass  # TODO

    # (2) Every element of S is an element of T
    pass  # TODO

    # (3) No two elements of S overlap
    pass  # TODO


print
print 'S is a solution for T: %s' % checkSolution(n, T, S)