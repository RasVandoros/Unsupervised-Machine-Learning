#dataset =  pd.read_csv('output_2.csv')

# Importing Modules
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names = ['del', 'mut', 'ins', 'reads', 'call']
dataset =  pd.read_csv('~/Ras/Data/backup.csv', names=names)
array = dataset.values
target = array[:,4]
feature_names = list(dataset.columns.values)

X = array[:, 0]
Y = array[:, 3]

label = {
    1: 'red', 
    2: 'blue', 
    3: 'green'
}
color_list = []
for c, value in enumerate(target):
        #target[c] = label[value]
        if value != 1 and value != 2 and value != 3: 
            print(c, value)
        else:
            color_list.append(label[value])
            
# Plotting
plt.scatter(X, Y, c=color_list)
plt.show()