from graph_de import graph_de
from pie_plotting import pie_plotting
from face_emotion_recognition import video_capture 

if __name__ == "__main__":

    graph = video_capture()

    angry, disgust, fear, happy, sad, surprise, neutral = graph_de(graph)

    pie_plotting(angry, disgust, fear, happy, sad, surprise, neutral, 'foo.png')
    
