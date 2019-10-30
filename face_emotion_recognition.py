import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import cv2
import numpy as np
from keras.models import load_model

import matplotlib.pyplot as plt



def video_capture():
    global result1, text
    result1 = []
    text = []
    model = load_model("model.hdf5")

    #model.summary()


    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    video_capture = cv2.VideoCapture(0)


    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
    out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                          10, (frame_width, frame_height))


    graph = []

    target = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        
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

            
            for i in range(len(target)):
                #print("{} :- {}".format(target[i], value[0][i]))

                tex = "{} :- {}".format(target[i], value[0][i])
                #print(tex)
                text.append(value[0][i])
                result1.append(target[i])

            val = np.argmax(value)
            result = target[val]
            #print(result)
            cv2.putText(frame, result, (x, y), font, 1, (255, 0, 0), 1, cv2.LINE_AA)


            # cv2.putText(frame, text, (x, y), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
            graph.append(result)

        cv2.imshow('Video', frame)
        out.write(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #print("text:-", text)
        #print("result:-", result1)

        data = pd.DataFrame(
        {'Emotion':result1,
         'value' : text}
        )

        data.to_csv("csv_data.csv")

        

    video_capture.release()
    cv2.destroyAllWindows()

    return graph, result1, text

#video_capture()
