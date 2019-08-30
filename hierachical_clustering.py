from sklearn import datasets
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd


names = ['del', 'mut', 'ins', 'reads', 'call']
dataset =  pd.read_csv('~/Ras/Data/output_2.csv', names=names)

call = list(dataset.pop('call'))
array = dataset.values
mergings = linkage(array, method='complete')

dendrogram(mergings,
           labels=call,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()