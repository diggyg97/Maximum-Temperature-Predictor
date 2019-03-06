import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('/Users/digvijayghotane/Desktop/Projects/Temp-Predict/dataset.csv').dropna()

for i in range(1,17):
    x = a.iloc[:,0]
    y = a.iloc[:,i]
    y = plt.plot(x,y,'rx',)
    plt.xlabel(a.columns[i])
    plt.ylabel('Temp')
    plt.show(y)