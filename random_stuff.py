import numpy as np
import sompylib.som_structure as SOM
from matplotlib import pyplot as plt
import sys
msz0 = 50
msz1 = 50
cd = msz0*msz1*1*1
dlen = 100*1000*1*1*1#+224
dim = 3
Data = np.random.randint(0,2,size = (dlen,dim))
# Data = np.random.rand(dlen,dim)
