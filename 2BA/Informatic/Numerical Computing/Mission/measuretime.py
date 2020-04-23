# measuretime.py
# Author: Mitrovic Nikola
# Version: April 23, 2020

import timeit, sys
import numpy as np  
import matplotlib.pyplot as plt         
from time import sleep 

REPEATS = 1000
SETUP = '''
import numpy as np           
from random import randint   
from __main__ import py_multiply, np_multiply, square_matrix, random_array, np_min, py_min
'''

# Generate square n dimensional matrix using array
def square_matrix(n):
    return np.ndarray((n, n), dtype=int)

def random_array(n):
    return np.ndarray((n), dtype=int)

# Generate square n dimensional matrix filled with null value 
# using array and convert it to Python list
def empty_square_matrix(n):
    return np.zeros((n, n)).tolist()

# Explicit multiplication by manipulating Python lists with loops
def py_multiply(a, b):
    result = np.zeros((len(a), len(a))).tolist()
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Direct multiplication with the ndarray or matrix object
def np_multiply(a, b):
    return np.matmul(a, b)

# Find minimum value of list of number with python method min()
def py_min(a):
    return min(a)

# Find minimum value of 1D array with numpy method
def np_min(a):
    return np.amin(a)

# Measure execution time of function defined by code variable
def timer(setup, code):
    t = timeit.Timer(setup=setup, stmt=code)
    result = t.timeit(REPEATS) / REPEATS * 1000
    return result

# Testing matrix product methods
def matrix_test(n):
    data1 = []
    data2 = []
    for i in range(2, n+1):
        list_multiply = '''p = square_matrix({}).tolist(); py_multiply(p, p)'''.format(str(i))
        array_multiply = '''p = square_matrix({}); np_multiply(p, p)'''.format(str(i))
        time1 = timer(SETUP, list_multiply)
        time2 = timer(SETUP, array_multiply)
        data1.append([i, time1])
        data2.append([i, time2])
    return np.asarray(data1), np.asarray(data2)

# Testing minimum methods
def minimum_test(n):
    data1 = []
    data2 = []
    for i in range(1, n) :
        array_min = '''a = random_array({}); np_min(a)'''.format(str(i))
        list_min = '''a = random_array({}); b = a.tolist(); py_min(b)'''.format(str(i))
        time1 = timer(SETUP, list_min)
        time2 = timer(SETUP, array_min)
        data1.append([i, time1])
        data2.append([i, time2])
        '''sys.stdout.write('\r')
        status = i/n * 100
        pad = int(status+1)
        sys.stdout.write("[%-100s] %d%%" % ('='*pad, pad))
        sys.stdout.flush()
        sleep(0.000000000000000000000000000000000000000000000000000000000001)'''
    return np.asarray(data1), np.asarray(data2)

# Plot all data
def plot(t1, t2):
    # Compute test and store the data into array
    dataset1, dataset2 = matrix_test(t1)
    dataset3, dataset4 = minimum_test(t2)

    # Set up plot settings (axe, label, subplot, legend ...)
    fig, axs = plt.subplots(2)
    axs[0].set_title('Matrix Product Processing Time Comparison', fontweight='bold')
    axs[0].set_xlabel('Matrix Dimension', fontsize='12')
    axs[0].set_ylabel('Time [ms]', fontsize='12')
    axs[0].grid()
    axs[1].set_title('Minimum Value Processing Time Comparison', fontweight='bold')
    axs[1].set_xlabel('Python List/1D Array Size', fontsize='12')
    axs[1].set_ylabel('Time [ms]', fontsize='12')
    axs[1].grid()
    axs[0].plot(dataset1[:, 0], dataset1[:, 1], 'r')
    axs[0].plot(dataset2[:, 0], dataset2[:, 1], 'b')
    axs[0].legend(['Python List Method', 'Numpy Array Method'])
    axs[1].plot(dataset3[:, 0], dataset3[:, 1], 'r')
    axs[1].plot(dataset4[:, 0], dataset4[:, 1], 'b')
    axs[1].legend(['Python List Method', 'Numpy Array Method'])
    fig.tight_layout(pad=2.0)
    plt.show()

plot(10, 500)