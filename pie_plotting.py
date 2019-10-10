import matplotlib.pyplot as plt

def pie_plotting(angry, disgust, fear, happy, sad, surprise, neutral, filename):
    labels = 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'
    sizes = [len(angry), len(disgust), len(fear), len(happy), len(sad), len(surprise), len(neutral)]
    maxi = max(sizes)

    explode = []
    
    for i in range(len(sizes)):
        if sizes[i] == maxi:
            explode.append(0.1)
        else:
            explode.append(0)
            
    explode = tuple(explode)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig(filename)
    plt.show()
