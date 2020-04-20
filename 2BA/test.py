import datetime as dt 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

a = np.array(['2007-07-13', '2007-07-14', '2007-07-15'], dtype='datetime64')
b = np.array([2, 4, 5], dtype='int')

print(a)
print(b)

fig, ax = plt.subplots()
ax.set_xlabel('Time [MM-DD]', fontsize='12')
ax.set_ylabel('Deaths', fontsize='12')
ax.set_title('Total COVID-19 Deaths in Belgium 2020', fontsize='16', fontweight='bold')
ax.grid()

plt.plot(a, b, 'o-r', linewidth=2)
plt.show()