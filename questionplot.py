import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np


def y_displacement(y_offset, initial_speed, theta, find_theta, find_xdistance, find_max_height):
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

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    if find_theta:
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(x_pos, y_pos)
        plt.annotate(s="", xy=(-1, y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, -1), xytext=(max(x_pos), -1), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, y_offset), xytext=(calculate_point(0, 12, theta, 10)),
                     arrowprops=dict(arrowstyle='<-'))
        plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
        plt.plot([0, 0], [0, y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([-0, -1], [y_offset, y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([0, x_pos[y_pos.index(max(y_pos))]], [y_offset, y_offset], color='k', linestyle='--', linewidth=2)
        plt.annotate(s="", xy=(x_pos[y_pos.index(max(y_pos))], max(y_pos)),
                     xytext=(x_pos[y_pos.index(max(y_pos))], y_offset), arrowprops=dict(arrowstyle='<->'))
        plt.text(-max(x_pos) * 0.08, y_offset / 2, str(y_offset), style='normal')
        plt.text(max(x_pos) / 2, -max(x_pos) * 0.05, str(max(x_pos)), style='normal')
        plt.text(x_pos[y_pos.index(max(y_pos))] + 1, ((max(y_pos) - y_offset) / 2) + y_offset,
                 str(max(y_pos) - y_offset),
                 style='normal')
        plt.text(0, initial_speed * 0.1 + y_offset, str(initial_speed), style='normal')

        plt.axis([-5, x_distance, -5, max(y_pos) + 5])
        plt.axis('off')
        plt.text(0 + initial_speed * 0.09, y_offset + initial_speed * 0.02, r'\textbf{\ensuremath{\theta}')
        arc = patches.Arc((0, y_offset), 7, 7,
                          angle=0, theta1=360, theta2=30, linewidth=1)
        ax.add_patch(arc)
        plt.show()

    elif find_xdistance:
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(x_pos, y_pos)
        plt.annotate(s="", xy=(-1, y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, -1), xytext=(max(x_pos), -1), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, y_offset), xytext=(calculate_point(0, 12, theta, 10)),
                     arrowprops=dict(arrowstyle='<-'))
        plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
        plt.plot([0, 0], [0, y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([-0, -1], [y_offset, y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([0, x_pos[y_pos.index(max(y_pos))]], [y_offset, y_offset], color='k', linestyle='--', linewidth=2)
        plt.annotate(s="", xy=(x_pos[y_pos.index(max(y_pos))], max(y_pos)),
                     xytext=(x_pos[y_pos.index(max(y_pos))], y_offset), arrowprops=dict(arrowstyle='<->'))
        plt.text(-max(x_pos) * 0.08, y_offset / 2, str(y_offset), style='normal')
        plt.text(max(x_pos) / 2, -max(x_pos) * 0.05, "x", style='normal')
        plt.text(x_pos[y_pos.index(max(y_pos))] + 1, ((max(y_pos) - y_offset) / 2) + y_offset,
                 str(max(y_pos) - y_offset),
                 style='normal')
        plt.text(0, initial_speed * 0.1 + y_offset, str(initial_speed), style='normal')

        plt.axis([-5, x_distance, -5, max(y_pos) + 5])
        plt.axis('off')
        plt.text(0 + initial_speed * 0.09, y_offset + initial_speed * 0.02, str(np.degrees(theta)))
        arc = patches.Arc((0, y_offset), 7, 7,
                          angle=0, theta1=360, theta2=30, linewidth=1)
        ax.add_patch(arc)
        plt.show()
    elif find_max_height:
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(x_pos, y_pos)
        plt.annotate(s="", xy=(-1, y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, -1), xytext=(max(x_pos), -1), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, y_offset), xytext=(calculate_point(0, 12, theta, 10)),
                     arrowprops=dict(arrowstyle='<-'))
        plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
        plt.plot([0, 0], [0, y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([-0, -1], [y_offset, y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([0, x_pos[y_pos.index(max(y_pos))]], [y_offset, y_offset], color='k', linestyle='--', linewidth=2)
        plt.annotate(s="", xy=(x_pos[y_pos.index(max(y_pos))], max(y_pos)),
                     xytext=(x_pos[y_pos.index(max(y_pos))], y_offset), arrowprops=dict(arrowstyle='<->'))
        plt.text(-max(x_pos) * 0.08, y_offset / 2, str(y_offset), style='normal')
        plt.text(max(x_pos) / 2, -max(x_pos) * 0.05, str(max(x_pos)), style='normal')
        plt.text(x_pos[y_pos.index(max(y_pos))] + 1, ((max(y_pos) - y_offset) / 2) + y_offset,
                 "x",
                 style='normal')
        plt.text(0, initial_speed * 0.1 + y_offset, str(initial_speed), style='normal')

        plt.axis([-5, x_distance, -5, max(y_pos) + 5])
        plt.axis('off')
        plt.text(0 + initial_speed * 0.09, y_offset + initial_speed * 0.02, str(np.degrees(theta)))
        arc = patches.Arc((0, y_offset), 7, 7,
                          angle=0, theta1=360, theta2=30, linewidth=1)
        ax.add_patch(arc)
        plt.show()
        print(x_pos, y_pos)

def calculate_point(start_x, start_y, angle, length):
    endpoint = [start_x + (length * np.cos(angle)), start_y + (length * np.sin(angle))]
    return endpoint


y_displacement(12, 20, 30, 0, 0, 1)
