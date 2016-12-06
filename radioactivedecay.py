import matplotlib.pyplot as plt
import numpy as np


def generate():
    n0 = 500  # Initial number of particles in sample
    decayConstant = 0.1  # Decay constant of the sample
    tMax = 1 / decayConstant * 10  # Maximum time to run program. Calculated so that as the decay constant gets smaller deltaT gets bigger
    deltaT = 0.01 * 1 / decayConstant  # Length of time between each calculation. Calculated so that as the decay constant gets smaller deltaT gets bigger
    xValues = np.arange(0, tMax, deltaT)  # Populates the array with time values from 0 to tMax with increment deltaT.
    yValues = []  # Initialising yValues array

    yValues = n0 * (
    np.exp(-decayConstant * xValues))  # Go through all yValues and calculate the particles remaining at that time

    plt.xlabel("Time (s)")  # Adds label to x axis
    plt.ylabel("Number of particles")  # Adds label to y axis
    plt.grid(True)  # Enables display of grid on graph
    plt.plot(xValues, yValues)  # Calling matplotlib to plot x and y values

    plt.axis([0, tMax * 0.8, 0, n0])  # Sets the range of the axes, so that the x axis scales with the run time
    plt.show()  # Printing graph to screen


if __name__ == '__main__':
    generate()
