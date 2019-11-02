import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import random
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

class animati(object):

    def __init__(self, angry, happy, sad, neutral, text):
        self.angry = angry
        self.happy = happy
        self.sad = sad
        self.neutral = neutral


    def data(self):

        data = pd.read_csv("csv_data.csv")


        
        
    def animate(self, j):
        print(j)
        xar_a = []
        yar_a = []
        xar_h = []
        yar_h = []
        xar_s = []
        yar_S = []
        xar_n = []
        yar_n = []
        for i in range(j):
            if self.result == 'angry':
                yar_a.append(float(self.real_value))
                xar_a.append(int(i))
            elif self.result == 'sad':
                yar_s.append(float(self.real_value))
                xar_s.append(int(i))
            elif self.result == 'happy':
                yar_h.append(float(self.real_value))
                xar_h.append(int(i))
            elif self.result == 'neutral':
                yar_n.append(float(self.real_value))
                xar_n.append(int(i))
    
        ax1.clear()
        ax1.plot(xar_a,yar_a, c='b')
        ax2.clear()
        ax2.plot(xar_s,yar_s, c='y')
        ax3.clear()
        ax3.plot(xar_h,yar_h, c='r')
        ax4.clear()
        ax4.plot(xar_n,yar_n, c='k')
        
        plt.savefig("Live.png")

angry = 10
happy = 10
sad = 10
neutral = 10
text = 10

animat = animati(angry, happy, sad, neutral, text)
ani = animation.FuncAnimation(fig, animat.animate, interval=10)
plt.show()
