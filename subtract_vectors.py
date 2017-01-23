def subtract_vectors(vect1, vect2):
    """
    This function subtracts two vectors (represented by lists) to three decimal places

    >>> subtract_vectors([7.119, 8.215], [-8.223, 0.878])
    [15.342, 7.337]
    """

    for i in xrange(len(vect1)):
        temp = vect1[i]
        vect1[i] = temp - vect2[i]

    return vect1