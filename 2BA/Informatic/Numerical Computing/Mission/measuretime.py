# measuretime.py
# Author: Mitrovic Nikola
# Version: April 20, 2020

import timeit
import numpy as np  
import matplotlib.pyplot as plt         
from random import randint     

REPEATS = 1000
SETUP = '''
import numpy as np           
from random import randint   
from __main__ import py_multiply, np_multiply, square_matrix
'''

# Generate square n dimensional matrix using array
def square_matrix(n):
    return np.random.randint(100, size=(n, n))

# Generate square n dimensional matrix filled with null value 
# using array and convert it to Python list
def empty_square_matrix(n):
    return np.zeros((n, n)).tolist()

# Explicit multiplication by manipulating Python lists with loops
def py_multiply(a, b):
    result = empty_square_matrix(len(a))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Direct multiplication with the ndarray or matrix object
def np_multiply(a, b):
    return np.matmul(a, b)

# Measure execution time of function defined by code variable
def timer(setup, code):
    t = timeit.Timer(setup=setup, stmt=code)
    result = t.timeit(REPEATS) / REPEATS * 1000
    return result

def plot(n):
    data1 = []
    data2 = []
    for i in range(2, n+2):
        list_multiply = '''p = square_matrix({}).tolist(); py_multiply(p, p)'''.format(str(i))
        array_multiply = '''p = square_matrix({}); np_multiply(p, p)'''.format(str(i))
        time1 = timer(SETUP, list_multiply)
        time2 = timer(SETUP, array_multiply)
        data1.append([i, time1])
        data2.append([i, time2])
    dataset1 = np.asarray(data1)
    dataset2 = np.asarray(data2)

    _, ax = plt.subplots()
    ax.set_title('Matrix Product Processing Time Comparison')
    ax.set_xlabel('Matrix Dimension', fontsize='12')
    ax.set_ylabel('Time [ms]', fontsize='12')
    ax.grid()
    plt.plot(dataset1[:, 0], dataset1[:, 1], 'r')
    plt.plot(dataset2[:, 0], dataset2[:, 1], 'b')
    plt.legend(['Python List Method', 'Numpy Array Method'])
    plt.show()

plot(10)