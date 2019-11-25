from graph_de import graph_de
from pie_plotting import pie_plotting
from CSV_create import csv_create
from value_count import value_count
from face_emotion_recognition import video_capture
from bar import bar
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from confidence_gui import GUI_Confidence

if __name__ == "__main__":


    graph = video_capture()

    #csv = csv_create(result, text)

    angry, disgust, fear, happy, sad, surprise, neutral = graph_de(graph)

    pie_plotting(angry, disgust, fear, happy, sad, surprise, neutral, 'foo.png')


    result = value_count(angry, disgust, fear, happy, sad, surprise, neutral)
    bar(angry, disgust, fear, happy, sad, surprise, neutral)
    GUI_Confidence(result)
    
