import matplotlib.pyplot as plt
import numpy as np

initialParticles = 4000  # Number of initial particles
exponent = 4
decayConstant = 9.63 * 10 ** -exponent  # Decay constant of sample
increment = 0.1  # Time increment used to populate x array
constant = 100000 * exponent

xArray = np.arange(0, increment * constant, increment)
yArray = []

for i in range(0, int((increment * constant) / increment), 1):
    yArray.append(initialParticles * np.exp(-1 * decayConstant * i * 0.1))

plt.plot(xArray, yArray)
plt.axis([0, increment * constant, 0, initialParticles])
plt.xlabel("Time (s)")
plt.ylabel("Number of particles remaining")
plt.show()
