import matplotlib.pyplot as plt
import numpy as np


def generate():
    n0 = 500  # Initial number of particles in sample
    decay_constant = 0.1  # Decay constant of the sample
    t_max = 1 / decay_constant * 10  # Maximum time to run program. As decay constant gets smaller deltaT gets bigger
    delta_t = 0.01 * 1 / decay_constant  # Time between each calculation. As decay constant gets smaller deltaT increase
    x_values = np.arange(0, t_max, delta_t)  # Populates the array with time values from 0 to tMax with increment deltaT

    y_values = n0 * (
                      np.exp(-decay_constant * x_values))
    # Go through all yValues and calculate the particles remaining at that time

    plt.xlabel("Time (s)")  # Adds label to x axis
    plt.ylabel("Number of particles")  # Adds label to y axis
    plt.grid(True)  # Enables display of grid on graph
    plt.plot(x_values, y_values)  # Calling matplotlib to plot x and y values

    plt.axis([0, t_max * 0.8, 0, n0])  # Sets the range of the axes, so that the x axis scales with the run time
    plt.show()  # Printing graph to screen


if __name__ == '__main__':
    generate()
