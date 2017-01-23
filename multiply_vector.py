def multiply_vectors(num, vect):
    """
    This function multiplies a vector (represented as a list) by a decimal number

    >>> multiply_vectors(7.41, [1.671, -1.012, -0.318])
    [12.382, -7.499, -2.356]
    """

    for i in xrange(len(vect)):
        temp = vect[i]
        vect[i] = temp * num
        vect[i] = round(vect[i], 3)

    return vect