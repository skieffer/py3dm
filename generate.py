
import random

def generateSetOfTriples(sizeOfA, numTriples):
    """
    Generate a set of triples of positive integers

    :param sizeOfA: the size n of the set A = {1, 2, ..., n}
    :param numTriples: how many triples you want
    :return: some set T of triples over A

    WARNING: If you make the arguments too large, this could take a long time!
    """
    X = set()
    while len(X) < numTriples:
        a = random.randint(1, sizeOfA)
        b = random.randint(1, sizeOfA)
        c = random.randint(1, sizeOfA)
        X.add((a, b, c))
    return X
