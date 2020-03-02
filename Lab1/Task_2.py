import numpy as np
x = np.array([[11,12,13,14,15],
         [21,22,23,24,25],
         [31,32,33,34,35],
         [41,42,43,44,45]])
x[1,:] = 0
print("Second row with zeros: ")
print(x)
print("Reshaped array: ")
print(x.reshape(5,4))