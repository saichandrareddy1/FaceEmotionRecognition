import numpy as np
import matplotlib.pyplot as plt

#plt.axis([0, 10, 0, 1])
x_ = []
y_ = []
for i in range(100):
    y = np.random.random()
    y_.append(y)
    x_.append(i)
    plt.plot(x_, y_, c = 'r')
    plt.pause(0.05)

plt.show()
