import numpy as np
playersdata = np.array([[75,75,74,69,71,74,73,73,76,74,74,70,72,77,74,70,76,75,73,75],
               [245,240,215,185,175,199,200,215,200,205,206,186,188,220,210,195,244,195,200,200],
               [30.17,31.36,30.99,32.24,27.61,28.2,28.85,24.21,22.02,24.97,26.78,32.51,30.95,33.09,32.74,30.69,36.51,26.03,23.45,24.94]])
print(playersdata.dtype)
print("Information about 4th player:")
print("Height: ", playersdata[0][3], "inches, weight: ", playersdata[1][3], " pounds, ", playersdata[2][3], " years old")
print("Weights of players", playersdata[1,:])
dmi4 = playersdata[1][3] / pow(playersdata[0][3],2)
dmi6 = playersdata[1][5] / pow(playersdata[0][5],2)
if(dmi4>dmi6):
    print("DMI 4 > DMI 6")
if (dmi4 < dmi6):
    print("DMI 4 < DMI 6")
print("Weights and heights of 2nd and 3rd players: ")
print(playersdata[0:2, 1:3])
print("Shapes: ", playersdata.shape, ", number of elements: ", playersdata.size, ", data type: ", playersdata.dtype)