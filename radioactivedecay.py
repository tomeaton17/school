import matplotlib.pyplot as plt
import numpy as np

n0 = 50000000  # Initial number of particles in sample
decayConstant = 0.000000000000000001  # Decay constant of the sample
tMax = 1 / decayConstant * 10  # Maximum time to run program
deltaT = 0.01 * 1 / decayConstant  # Length of time between each calculation
xValues = np.arange(0, tMax, deltaT)  # Populates the array with time values from 0 to tMax with increment deltaT.
yValues = []  # Initialising yValues array

yValues = n0 * (
    np.exp(-decayConstant * xValues))  # Go through all yValues and calculate the particles remaining at that time

print(len(xValues), len(yValues))
xValues = np.asarray(xValues)
yValues = np.asarray(yValues)
plt.plot(xValues, yValues)  # Calling matplotlib to plot x and y values
plt.axis([0, tMax * 0.8, 0, n0])
plt.show()  # Printing graph to screen
