import pandas as pd
import numpy as np



def csv_create(data_file):

##    data = pd.DataFrame(
##        {'Emotion':result,
##         'value' : text}
##        )
##
##    data.to_csv("csv_data.csv")



    data = pd.read_csv(data_file)

    uniq = data['Emotion'].value_counts()
    print(uniq)
    
