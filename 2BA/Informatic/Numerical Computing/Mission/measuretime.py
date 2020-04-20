# measuretime.py
# Author: Sébastien Combéfis
# Version: April 15, 2020

import timeit
import numpy as np           
from random import randint            

def square_matrix(n):
    shape = (n, n)
    return np.ndarray(shape)

a = square_matrix(5)


# Explicit multiplication by manipulating Python lists with loops
def py_multiply(a, b):
    pass

# Direct multiplication with the ndarray or matrix object
def np_multiply(a, b):
    m, n = a.shape
    shape = (m, n)
    result = np.ndarray(shape)
    for i in range(m):
        for j in range(n):
            result[m, n] = a[m] * b[]



REPEATS = 1000

# # Measure execution time of py_multiply
# t = timeit.Timer('py_multiply(p, p)', '''from __main__ import py_multiply
# p = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]''')
# result = t.timeit(REPEATS) / REPEATS * 1000
# print(result, 'ms')

# # Measure execution time of np_multiply
# t = timeit.Timer('np_multiply(p, p)', '''import numpy as np
# from __main__ import np_multiply
# p = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])''')
# result = t.timeit(REPEATS) / REPEATS * 1000
# print(result, 'ms')