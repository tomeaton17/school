import matplotlib.pyplot as plt
import numpy as np


def y_displacement(y_offset, initial_speed, theta):
    increment = 0.001
    theta = np.radians(theta)
    x_speed = initial_speed * np.cos(theta)
    y_speed = initial_speed * np.sin(theta)
    x_pos = []
    y_pos = []
    time = 0
    x_pos.append(0)

    y_pos.append(y_offset)  # Adding the offset in the first slot of the position array

    time += increment
    x_pos_temp = x_speed * time  # Calculating first x value so while loop doesn't fail instantly
    y_pos_temp = (y_speed * time) + (
        0.5 * -9.8 * time ** 2) + y_offset

    x_pos.append(x_pos_temp)
    y_pos.append(y_pos_temp)

    while y_pos_temp > 0:
        y_pos_temp = (y_speed * time) + (0.5 * -9.8 * time ** 2 + 12)
        x_pos.append(x_speed * time)
        y_pos.append((y_speed * time) + (0.5 * -9.8 * time ** 2) + 12)
        time += increment
    x_distance = max(x_pos)
    print(x_pos)
    print(y_pos)
    plt.plot(x_pos, y_pos)
    plt.annotate(s="", xy=(-1, y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
    plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
    plt.plot([0, 0], [0, y_offset], color='k', linestyle='-', linewidth=2)
    plt.text(-3, y_offset / 2, str(y_offset), style='normal')
    plt.axis([-5, x_distance, 0, 30])
    plt.axis('off')
    plt.show()

y_displacement(12, 20, 45)
