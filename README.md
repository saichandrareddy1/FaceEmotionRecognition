# FaceEmotionRecognition
Here we use to do face emotion recognition with the help of keras and opencv you can find code and preprocessing techniques


It is fully develpoed for Face Emotion recognition with help of the computer vision and CNN

# How to Use it?
To use this code just we need to install some packages from pypi library

## Download repo or clone the repo
    
    git clone https://github.com/saichandrareddy1/FaceEmotionRecognition.git 

The above thing is buy using HTTPS we are going to clone the data into the ubuntu 
    
for windows download the repo or by using wget we can get it, if it not present install it by using https://builtvisible.com/download-your-website-with-wget/

    wget https://github.com/saichandrareddy1/FaceEmotionRecognition.git

# Prerequisites **

    1.We need Python 3.x idle or Anaconda
    2.Need all the libraries 
      1.numpy
      2.matplotlib
      3.seaborn
      4.pandas
      5.opencv
      6.keras backend tensorflow

# How to install all the prerequisites

Just run the below command mostly this is for the python idle or Anaconda 

    sudo apt install python3-pip  # if no pip is present
    
    sudo pip3 install -r requirements.txt
    or
    pip3 install -r requirements.txt

## Manual installation for Anaconda

In anaconda numpy, matplotlib, pandas are pre-installed or if it not installed in your envirolment use below commands

    conda install -c conda-forge numpy
    conda install -c conda-forge matplotlib
    conda install -c conda-forge seaborn
    conda install -c anaconda pandas
    conda install -c conda-forge opencv
    
    #GPU TENSORFLOW installation
    conda install -c anaconda tensorflow-gpu
    conda install -c anaconda keras-gpu
    
    #CPU 
    conda install -c anaconda tensorflow
    conda install -c anaconda keras
    
## Manual installation using pip command on CMD windows or Ubuntu

### ================WINDOWS===================
       
     pip3 install numpy
     pip3 install pandas 
     pip3 install matplotlib.pyplot
     pip3 install seaborn
     pip3 install python3-opencv
     
     #GPU
     pip3 install tensorflow-gpu
     pip3 install keras
     
     #CPU
     pip3 install tensorflow
     pip3 install keras
     
### ====================UBUNTU==============================
    
    sudo apt install python3-pip
    sudo pip3 install numpy
    sudo pip3 install pandas
    sudo pip3 install matplotlib
    sudo pip3 install seaborn
    sudo pip3 install opencv
    
    #GPU
    sudo pip3 install tensorflow-gpu
    sudo pip3 install keras
    
    #CPU
    sudo pip3 install keras
    sudo pip3 install tensorflow
    
Regarding using Sudo apt did you get any errors please try to use sudo apt-get command

If you get any errors while installation please report on the issues 
 
# How play with the model and the preprocessing code

Here if you are intered you can uodate the preprocessing code and the model also

# Working of the model

you can get the data from the this link https://drive.google.com/open?id=1sN0TtZ3LGTh2M15Zy-xB0tl1gGtfxtNT

# Model file 

you can model.hdf5 file from this link https://drive.google.com/open?id=1q29tJlE81i7dAToResbGMjszkLQE1V5j

# Running the model 

just open your CMD or Terminal
run this command
    
    python3 app.py
    
 after running the command you can see all the files like
 
    1.csv_data.csv
    2.foo.png
    3.bar.png
    
 # Final results
 
 ### Video
 
 [![video](video.png?raw=true "video")](https://youtu.be/06SNADSY0VM)
 
 ### after running you can see Live Graphs
 
 ![Live Graphs](figure.png?raw=true "Ploting")
 
 ### Pie Charts In detail 
 
 ![Pie](foo.png?raw=true "Pie Charts")
 
### Bar Graphs 

![Bar](bar.png?raw=true "Bar Graphs")
 
# Authors 
    1. Sai Chandra Reddy
    Email:- vsaichandrareddy@gmail.com
    2. Nayeem
    Email - sunnynayeem@gmail.com
    3. Mastan
    Email - chinnak1456@gmail.com
    4. Lokesh
    Email - lokeshkrishnavls@gmail.com
    5. Harish
    Email - jayaharishpilladi@gmail.com
    
# Mentor
    Dr. Parminder Singh
    Associate Professor from Lovely Professional University, Phagwara, punjab, INDIA
    Email:- parminder.16479@lpu.co.in
    
## Security Policy

## Supported Versions

This project is supported for the 

| Version           | Supported          |
| ----------------- | ------------------ |
| python 3.6        | :white_check_mark: |
| python 3.7        | :white_check_mark: |
| python 3.8        | :x:                |
| tensorflow < 2.0  | :white_check_mark: |
| tensorflow > 2.0  | :x:                |
| keras 2.3.0+      | :white_check_mark: |
| keras 2.3.0 <     | Not_checked        |



## Tesing of the os


| Tested            | Supported          |
| ----------------- | ------------------ |
| Ubuntu 18.04      | :white_check_mark: |
| windows 10        | :white_check_mark: |
| MacOS             | :x:                |
| Pop_os 18.04      | :white_check_mark: |
| RedHat            | Not_checked        |

## Reporting a Vulnerability

If you see any Vulnerability in code or while runnig time please push me a request or inform on ISSUES

## LICENSE

This repo is under GPL license if need to know more please check LICENSE.md


