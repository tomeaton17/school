import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def generate():
    increment = 0.0001  # Time increment used when calculating values
    initial_speed = 10
    theta = np.radians(70)  # Angle that the direction of launch makes to the horizontal

    x_speed = initial_speed * np.cos(theta)  # Using trig to calculate x_speed. Assumes there is no air resistance
    y_speed = initial_speed * np.sin(theta)

    x_offset = 0  # Initial x position. Can be changed to add an offset which can be in a question
    y_offset = 0  # Initial y position. Can be changed to add an offset which can be in a question

    x_pos = []  # X position array
    y_pos = []  # Y position array
    time = 0  # Initial time

    x_pos.append(x_offset)  # Adding the offset in the first slot of the position array
    y_pos.append(y_offset)  # Adding the offset in the first slot of the position array

    time += increment
    x_pos_temp = x_speed * time  # Calculating first x value so while loop doesn't fail instantly
    y_pos_temp = (y_speed * time) + (
        0.5 * -9.8 * time ** 2)  # Using SUVAT to calculate first y value. This is so that the while loop doesn't fail

    x_pos.append(x_pos_temp)
    y_pos.append(y_pos_temp)

    while y_pos_temp > 0:
        x_pos_temp = x_speed * time
        y_pos_temp = (y_speed * time) + (0.5 * -9.8 * time ** 2)
        x_pos.append(x_speed * time)
        y_pos.append((y_speed * time) + (0.5 * -9.8 * time ** 2))
        time += increment

    plt.plot(x_pos, y_pos)
    plt.axis([0, x_pos[len(x_pos) - 1], 0, max(y_pos) + max(y_pos) * .2])
    plt.xlabel("X displacement")
    plt.ylabel("Y displacement")
    index = y_pos.index(max(y_pos))
    x_value = x_pos[int(index)]
    plt.annotate("Maximum height: " + str(max(y_pos)), (x_value, max(y_pos)),
                (x_value - 0.2 * max(x_pos), max(y_pos) + max(y_pos) * .1), arrowprops=dict(arrowstyle="->"))
    plt.grid(True)
    plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
    im = Image.open('test.png')
    size = np.asarray(im.size)
    size /= 1.4
    size.tolist()
    im.thumbnail(size)
    im.save('smaller.png')


if __name__ == '__main__':
    generate()
