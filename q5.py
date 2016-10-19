
"""
Question 5

Give a polynomial-time reduction from 3DM to SAT.

In other words, given a 3DM problem T (a set of triples), we must convert it into
an equivalent SAT problem P, i.e. a formula P in conjuctive normal form that is
satisfiable if and only if there exists a solution S for the problem T.

TASK 1: Implement the 'translate3DMtoSAT' function, whose skeleton is given below.
TASK 2: Prove that your function works in polynomial time.
"""

from sat import *

from generate import generateSetOfTriples

n = 5
T = generateSetOfTriples(n, 12)

print
print 'Problem set T:'
print T


def translate3DMtoSAT(n, T):
    """
    :param n: the size of the set A
    :param T: a set of triples of elements of A
    :return: an instance P of the CNF class, that is satisfiable IFF T is solvable

    Basic Idea:
    Create a variable x_t for each triple t in T.
    P will be built using the variables x_t.
    The idea is that:
      x_t == True means t is in the solution set S
      x_t == False means t is not in the solution set S

    What must be expressed by the formula P?

    In short, P must say "S is a solution of T."
    But what does this involve?


    """
    # First let's enumerate the elements of T by converting it into a list.
    T = list(T)
    # Now create a variable for each element of T.
    m = len(T)
    X = [Var(i) for i in range(m)]
    # And create the positive and negative literals for these variables.
    pos = [Lit(x, 1) for x in X]
    neg = [Lit(x, -1) for x in X]
    # We'll build a list of clauses as we go.
    clauses = []

    # (1) We must ensure that in the solution set S, no two triples overlap.
    #
    # IDEA: Find all pairs (t1, t2) of triples that do overlap.
    # Then we can express the absence of overlaps by adding the clause (~x_t1 v ~x_t2)
    # for each such pair.
    pass  # TODO

    # (2) We must ensure that each a in A appears as the /first/ element of some triple.
    #
    # IDEA: For each a in A, find all triples t1, t2, ..., tk in which a occurs as the first element.
    # Then S must have one of these triples in it.
    # So P should contain the clause (x_t1 v x_t2 v ... v x_tk).
    pass  # TODO

    # (3) We must ensure that each a in A appears as the /second/ element of some triple.
    pass # TODO

    # (4) We must ensure that each a in A appears as the /third/ element of some triple.
    pass # TODO

    # Finally, conjoin the clauses and return the CNF.
    P = CNF(clauses)
    return P


P = translate3DMtoSAT(n, T)

print
print 'Equivalent CNF P:'
print P
