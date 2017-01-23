def add_vectors(vect1, vect2):
    """
    This function adds two vectors (represented by lists) to three decimal places

    >>> add_vectors([8.218, -9.341], [-1.129, 2.111])
    [7.089, -7.230]
    """

    for i in xrange(len(vect1)):
        temp = vect1[i]
        vect1[i] = temp + vect2[i]
        vect1[i] = round(vect1[i], 3)

    return vect1
