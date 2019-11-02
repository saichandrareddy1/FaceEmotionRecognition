import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import cv2
import numpy as np
from keras.models import load_model
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time


def video_capture():

    fig = plt.figure(figsize=(15,15))

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    
    global results, real_values

    results = []
    real_values = []
    model = load_model("model.hdf5")

    #model.summary()
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    video_capture = cv2.VideoCapture(0)

    video_capture.set(cv2.CAP_PROP_FPS, 300)
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
    out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                          10, (frame_width, frame_height))


    graph = []

    target = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    font = cv2.FONT_HERSHEY_SIMPLEX

    xar_a = []
    yar_a = []
    xar_h = []
    yar_h = []
    xar_s = []
    yar_s = []
    xar_n = []
    yar_n = []
    
    i = 0
 
    while True:

        global real_value, result
        
        result = None
        real_value = 0
        
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 5)
            face_crop = frame[y:y + h, x:x + w]
            face_crop = cv2.resize(face_crop, (48, 48))
            face_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
            face_crop = face_crop.astype('float32') / 255
            face_crop = np.asarray(face_crop)
            face_crop = face_crop.reshape(1, 1, face_crop.shape[0], face_crop.shape[1])
            value = model.predict(face_crop)


            val = np.argmax(value)
            real_value = value[0][val]
            real_values.append(real_value)
            
            result = target[val]
            
            results.append(result)
            
            cv2.putText(frame, result, (x, y), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

            text = "{} :- {}".format(result, real_value)
            cv2.putText(frame, text, (x, y), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
            graph.append(result)


        cv2.imshow('Video', frame)
        out.write(frame)

        if result == 'angry':
            xar_a.append(i)
            yar_a.append(real_value)
        elif result == 'happy':
            xar_h.append(i)
            yar_h.append(real_value)
        elif result == 'sad':
            xar_s.append(i)
            yar_s.append(real_value)
        elif result == 'neutral':
            xar_n.append(i)
            yar_n.append(real_value)
        else:
            pass

        #Angry
        ax1.clear()
        ax1.plot(xar_a, yar_a, c = 'r')
        #ax1.set_xlabel("number iteration or Frames")
        ax1.set_ylabel("accuracy score")
        ax1.set_title("Angry", fontsize = 10)

        #Happy
        ax2.clear()
        ax2.plot(xar_h, yar_h, c = 'k')
        #ax2.set_xlabel("number iteration or Frames")
        #ax2.set_ylabel("accuracy score")
        ax2.set_title("Happy", fontsize = 10)

        #Sad
        ax3.clear()
        ax3.plot(xar_s, yar_s, c = 'b')
        ax3.set_xlabel("number iteration or Frames")
        ax3.set_ylabel("accuracy score")
        ax3.set_title("Sad", fontsize = 10)
       
        #Neutral
        ax4.clear()
        ax4.plot(xar_n, yar_n, c = 'y')
        ax4.set_xlabel("number iteration or Frames")
        #ax4.set_ylabel("accuracy score")
        ax4.set_title("Neutral", fontsize = 10)
        plt.pause(0.05)

        
        
        i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            break


        data = pd.DataFrame(
        {'Emotion':results,
         'value' : real_values}
        )

        data.to_csv("csv_data.csv")

    
    video_capture.release()
    cv2.destroyAllWindows()

    plt.show()
    fig.savefig("figure.png")
    #print(results)
    #print(real_values)

    return graph




#video_capture()



