import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib import patches


class ProjectileQuestion:
    def __init__(self, y_offset, initial_speed, theta):
        self.y_offset = y_offset
        self.initial_speed = initial_speed
        self.theta = theta
        self.x_pos = []
        self.y_pos = []

    def calculate_projectile(self):
        increment = 0.001
        theta = np.radians(self.theta)
        x_speed = self.initial_speed * np.cos(theta)
        y_speed = self.initial_speed * np.sin(theta)
        time = 0
        self.x_pos.append(0)

        self.y_pos.append(self.y_offset)  # Adding the offset in the first slot of the position array

        time += increment
        x_pos_temp = x_speed * time  # Calculating first x value so while loop doesn't fail instantly
        y_pos_temp = (y_speed * time) + (
            0.5 * -9.8 * time ** 2) + self.y_offset

        self.x_pos.append(x_pos_temp)
        self.y_pos.append(y_pos_temp)

        while y_pos_temp > 0:
            y_pos_temp = (y_speed * time) + (0.5 * -9.8 * time ** 2 + self.y_offset)
            self.x_pos.append(x_speed * time)
            self.y_pos.append((y_speed * time) + (0.5 * -9.8 * time ** 2) + self.y_offset)
            time += increment

    def find_theta(self):
        self.calculate_projectile()
        x_distance = max(self.x_pos)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(self.x_pos, self.y_pos)
        plt.annotate(s="", xy=(-1, self.y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, -1), xytext=(max(self.x_pos), -1), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, self.y_offset), xytext=(self.calculate_point(0, self.y_offset, np.radians(self.theta), 10)),
                     arrowprops=dict(arrowstyle='<-'))
        plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
        plt.plot([0, 0], [0, self.y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([-0, -1], [self.y_offset, self.y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([0, self.x_pos[self.y_pos.index(max(self.y_pos))]], [self.y_offset, self.y_offset], color='k', linestyle='--', linewidth=2)
        plt.annotate(s="", xy=(self.x_pos[self.y_pos.index(max(self.y_pos))], max(self.y_pos)),
                     xytext=(self.x_pos[self.y_pos.index(max(self.y_pos))], self.y_offset), arrowprops=dict(arrowstyle='<->'))
        plt.text(-max(self.x_pos) * 0.08, self.y_offset / 2, str(self.y_offset), style='normal')
        plt.text(max(self.x_pos) / 2, -max(self.x_pos) * 0.05, str(max(self.x_pos)), style='normal')
        plt.text(self.x_pos[self.y_pos.index(max(self.y_pos))] + 1, ((max(self.y_pos) - self.y_offset) / 2) + self.y_offset,
                 str(max(self.y_pos) - self.y_offset),
                 style='normal')
        plt.text(0, self.initial_speed * 0.1 + self.y_offset, str(self.initial_speed), style='normal')

        plt.axis([-5, x_distance, -5, max(self.y_pos) + 5])
        plt.axis('off')
        plt.text(0 + self.initial_speed * 0.09, self.y_offset + self.initial_speed * 0.02, r'\textbf{\ensuremath{\theta}')
        arc = patches.Arc((0, self.y_offset), 10, 10,
                          angle=0, theta1=360, theta2=self.theta, linewidth=1)
        ax.add_patch(arc)
        print("Answer:", self.theta)
        plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
        im = Image.open('test.png')
        size = np.asarray(im.size)
        # noinspection PyAugmentAssignment
        size = size / 1.4
        size.tolist()
        im.thumbnail(size)
        im.save('smaller.png')

    def find_xdistance(self):
        self.calculate_projectile()
        x_distance = max(self.x_pos)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(self.x_pos, self.y_pos)
        plt.annotate(s="", xy=(-1, self.y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, -1), xytext=(max(self.x_pos), -1), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, self.y_offset), xytext=(self.calculate_point(0, self.y_offset, np.radians(self.theta), 10)),
                     arrowprops=dict(arrowstyle='<-'))
        plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
        plt.plot([0, 0], [0, self.y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([-0, -1], [self.y_offset, self.y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([0, self.x_pos[self.y_pos.index(max(self.y_pos))]], [self.y_offset, self.y_offset], color='k',
                 linestyle='--', linewidth=2)
        plt.annotate(s="", xy=(self.x_pos[self.y_pos.index(max(self.y_pos))], max(self.y_pos)),
                     xytext=(self.x_pos[self.y_pos.index(max(self.y_pos))], self.y_offset),
                     arrowprops=dict(arrowstyle='<->'))
        plt.text(-max(self.x_pos) * 0.08, self.y_offset / 2, str(self.y_offset), style='normal')
        plt.text(max(self.x_pos) / 2, -max(self.x_pos) * 0.05, "x", style='normal')
        plt.text(self.x_pos[self.y_pos.index(max(self.y_pos))] + 1,
                 ((max(self.y_pos) - self.y_offset) / 2) + self.y_offset,
                 str(max(self.y_pos) - self.y_offset),
                 style='normal')
        plt.text(0, self.initial_speed * 0.1 + self.y_offset, str(self.initial_speed), style='normal')

        plt.axis([-5, x_distance, -5, max(self.y_pos) + 5])
        plt.axis('off')
        plt.text(0 + self.initial_speed * 0.09, self.y_offset + self.initial_speed * 0.02,
                 str(self.theta))
        arc = patches.Arc((0, self.y_offset), 10, 10,
                          angle=0, theta1=360, theta2=self.theta, linewidth=1)
        ax.add_patch(arc)
        plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
        im = Image.open('test.png')
        size = np.asarray(im.size)
        # noinspection PyAugmentAssignment
        size = size / 1.4
        size.tolist()
        im.thumbnail(size)
        im.save('smaller.png')
        print("Answer:", self.answer_xdistance())

    def find_max_height(self):
        self.calculate_projectile()
        x_distance = max(self.x_pos)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(self.x_pos, self.y_pos)
        plt.annotate(s="", xy=(-1, self.y_offset), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, -1), xytext=(max(self.x_pos), -1), arrowprops=dict(arrowstyle='<->'))
        plt.annotate(s="", xy=(0, self.y_offset),
                     xytext=(self.calculate_point(0, self.y_offset, np.radians(self.theta), 10)),
                     arrowprops=dict(arrowstyle='<-'))
        plt.plot([0, x_distance], [0, 0], color='k', linestyle='-', linewidth=2)
        plt.plot([0, 0], [0, self.y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([-0, -1], [self.y_offset, self.y_offset], color='k', linestyle='-', linewidth=2)
        plt.plot([0, self.x_pos[self.y_pos.index(max(self.y_pos))]], [self.y_offset, self.y_offset], color='k',
                 linestyle='--', linewidth=2)
        plt.annotate(s="", xy=(self.x_pos[self.y_pos.index(max(self.y_pos))], max(self.y_pos)),
                     xytext=(self.x_pos[self.y_pos.index(max(self.y_pos))], self.y_offset),
                     arrowprops=dict(arrowstyle='<->'))
        plt.text(-max(self.x_pos) * 0.08, self.y_offset / 2, str(self.y_offset), style='normal')
        plt.text(max(self.x_pos) / 2, -max(self.x_pos) * 0.05, str(max(self.x_pos)), style='normal')
        plt.text(self.x_pos[self.y_pos.index(max(self.y_pos))] + 1,
                 ((max(self.y_pos) - self.y_offset) / 2) + self.y_offset,
                 "x",
                 style='normal')
        plt.text(0, self.initial_speed * 0.1 + self.y_offset, str(self.initial_speed), style='normal')

        plt.axis([-5, x_distance, -5, max(self.y_pos) + 5])
        plt.axis('off')
        plt.text(0 + self.initial_speed * 0.09, self.y_offset + self.initial_speed * 0.02,
                 str(self.theta))
        arc = patches.Arc((0, self.y_offset), 10, 10,
                          angle=0, theta1=360, theta2=self.theta, linewidth=1)
        ax.add_patch(arc)
        plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
        im = Image.open('test.png')
        size = np.asarray(im.size)
        # noinspection PyAugmentAssignment
        size = size / 1.4
        size.tolist()
        im.thumbnail(size)
        im.save('smaller.png')
        print("Answer:", self.answer_max_height())

    @staticmethod
    def calculate_point(start_x, start_y, angle, length):
        endpoint = [start_x + (length * np.cos(angle)), start_y + (length * np.sin(angle))]
        return endpoint

    def answer_theta(self):
        return self.theta

    def answer_xdistance(self):
        return max(self.x_pos)

    def answer_max_height(self):
        return max(self.y_pos)

if __name__ == "__main__":
    ProjectileQuestion(12, 20, 40).find_max_height()
