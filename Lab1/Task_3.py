import numpy as np
heights = np.array([72,75,72,73,74,72,78,75,72,74])
weights = np.array([195,219,225,212,202,185,200,209,200,195])
heights = heights*0.0254
weights = weights*0.453
print("Heights in meters: ", heights)
print("Weights in kilograms: ", weights)
bmis = weights / pow(heights,2)
print("BMI's: ", bmis)
print("BMI's < 27: ", bmis[bmis < 27])