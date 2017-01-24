from math import sqrt

def caluculate_magnitude(vect):
    """
    This function calulates the magnitude of a vector of n coordinates

    >>> caluculate_magnitude([-0.221,7.437])
    7.440282924728065

    >>> caluculate_magnitude([8.813,-1.331,-6.247])
    10.884187567292289

    """
    total = 0
    for i in xrange(len(vect)):
        total += (vect[i] * vect[i])
    return sqrt(total)