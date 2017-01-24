from magnitude import caluculate_magnitude

def normalize(vect):
    """
    This function normalizes a vector of an unspecified length

    >>> normalize([5.581,-2.136])
    [0.9339352140866403, -0.35744232526233]
    
    >>> normalize([1.996,3.108,-4.554])
    [0.3404012959433014, 0.5300437012984873, -0.7766470449528029]
    """
    vect_magnitude = caluculate_magnitude(vect)

    factor = 1/vect_magnitude

    for i in xrange(len(vect)):
        vect[i] = vect[i] * factor
    return vect
   