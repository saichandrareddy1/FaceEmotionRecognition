import cv2
import os

path = os.path.abspath(r"D:\capstone  data\Resized\Ranveer Singh\\") ###OLD FOLDER PATH
def get_imlist(path):
  lis = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png')]
  return lis

def facecrop(c):
    global i
    i = 0
    for image in c:
        #print(image)
        facedata ="cascades\data\haarcascade_frontalface_alt.xml"
        cascade = cv2.CascadeClassifier(facedata)

       
        img = cv2.imread(image)
        #print("img v==========", img)

        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        print(i)
        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

            sub_face = img[y:y+h, x:x+w]
            fname, ext = os.path.splitext(image)
            print(fname, ext)
            cv2.imwrite(r"D:\capstone  data\cropped\Ranveer Singh\/"+str(i)+"_cropped_"+ext, sub_face)
            
        i =i+1

c = get_imlist(path)
#print(c)
facecrop(c)

