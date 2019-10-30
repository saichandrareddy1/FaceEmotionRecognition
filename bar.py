import matplotlib.pyplot as plt
import numpy as np
def bar(angry, disgust, fear, happy, sad, surprise, neutral):

    total = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

    height = [len(angry), len(disgust), len(fear),
          len(happy), len(sad), len(surprise), len(neutral)]

    index = np.arange(len(total))
    plt.bar(index, height, width=0.8, bottom=None, align='center', data=None)
    plt.xlabel("Emotions")
    plt.ylabel("No of times repeated")
    plt.xticks(index, total, fontsize=10, rotation=30)
    plt.savefig("bar.png")
    plt.show()
