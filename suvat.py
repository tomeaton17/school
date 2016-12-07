import matplotlib.pyplot as plt
import numpy as np


def generate():
    increment = 0.0001  # Time increment used when calculating values
    initialSpeed = 10
    theta = np.radians(70)  # Angle that the direction of launch makes to the horizontal

    xSpeed = initialSpeed * np.cos(theta)  # Using trig to calculate xspeed. Assumes there is no air resistance
    ySpeed = initialSpeed * np.sin(theta)

    xOffset = 0  # Initial x position. Can be changed to add an offset which can be in a question
    yOffset = 0  # Initial y position. Can be changed to add an offset which can be in a question

    xPos = []  # X position array
    yPos = []  # Y position array
    time = 0  # Initial time

    xPos.append(xOffset)  # Adding the offset in the first slot of the position array
    yPos.append(yOffset)  # Adding the offset in the first slot of the position array

    time += increment
    xPosTemp = xSpeed * time  # Calculating first x value so while loop doesn't fail instantly
    yPosTemp = (ySpeed * time) + (
        0.5 * -9.8 * time ** 2)  # Using SUVAT to calculate first y value. This is so that the while loop doesn't fail instantly

    xPos.append(xPosTemp)
    yPos.append(yPosTemp)

    while (yPosTemp > 0):
        xPosTemp = xSpeed * time
        yPosTemp = (ySpeed * time) + (0.5 * -9.8 * time ** 2)
        xPos.append(xSpeed * time)
        yPos.append((ySpeed * time) + (0.5 * -9.8 * time ** 2))
        time += increment

    plt.plot(xPos, yPos)
    plt.axis([0, xPos[len(xPos) - 1], 0, max(yPos) + max(yPos) * .2])
    plt.xlabel("X displacement")
    plt.ylabel("Y displacement")
    index = yPos.index(max(yPos))
    xValue = xPos[int(index)]
    plt.annotate("Maximum height: " + str(max(yPos)), (xValue, max(yPos)),
             (xValue - 0.2 * max(xPos), max(yPos) + max(yPos) * .1), arrowprops=dict(arrowstyle="->"))
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    generate()
