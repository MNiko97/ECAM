import datetime as dt 
import numpy as np

data = [[2020, 3, 24, 85], [2020, 3, 25, 66], [2020, 3, 26, 450]]
shape = (len(data), 4)
array = np.ndarray(shape)
array[:] = data
print(array)