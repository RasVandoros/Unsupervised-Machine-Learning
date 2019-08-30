import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('output_2.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 5, sigma = 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 1000)

# Visualizing the results
from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's', 'v']
colors = ['r', 'g', 'y']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
       ) 



# Finding the frauds
mappings = som.win_map(X)
#for key in mappings:
#    print(key)

#whites = []
#blacks = []
#for row_index, row in enumerate(som.distance_map().T):
#    for column_index, value in enumerate(row):
#        if value > 0.9:
#            whites.append((column_index, row_index))
#
#for el in whites:
#    maps= mappings[el]
#    if maps: 
#        print(el)
#        maps = sc.inverse_transform(maps)
#        print(maps[0,0])
    
show()
