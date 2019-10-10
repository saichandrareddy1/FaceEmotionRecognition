from face_emotion_recognition import video_capture


def graph_de(graph):
    
    angry= []
    sad = []
    disgust = []
    fear = []
    happy = []
    surprise = []
    neutral = []


    for i in range(len(graph)):
        if graph[i] == 'angry':
            angry.append(graph[i])
        elif graph[i] == 'disgust':
            digust.append(graph[i])
        elif graph[i] == 'fear':
            fear.append(graph[i])
        elif graph[i] == 'happy':
            happy.append(graph[i])
        elif graph[i] == 'sad':
            sad.append(graph[i])
        elif graph[i] == 'surprise':
            surprise.append(graph[i])
        elif graph[i] == 'neutral':
            neutral.append(graph[i])
        else:
            pass


    return angry, disgust, fear, happy, sad, surprise, neutral



