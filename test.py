import geatpy as ea
import numpy as np

x1 = np.array([[1, 2], [3, 4]])
x2 = np.array(([5, 6], [7, 8]))
exIdx1 = np.where(2 * x1 + x2 > 1)
print(exIdx1)
print(type(exIdx1))
