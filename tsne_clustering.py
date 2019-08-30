# Importing Modules
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd



names = ['del', 'mut', 'ins', 'reads', 'call']
dataset =  pd.read_csv('~/Ras/Data/output_3.csv', names=names)
dataset = dataset[:-55000]
call = list(dataset.pop('call'))

# Defining Model
model = TSNE(learning_rate=100)

# Fitting Model
transformed = model.fit_transform(dataset)

# Plotting 2d t-Sne
x_axis = transformed[:, 0]
y_axis = transformed[:, 1]

plt.scatter(x_axis, y_axis, c=call)
plt.show()