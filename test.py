import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

a = pd.read_csv('/Users/digvijayghotane/Desktop/Projects/Temp-Predict/dataset.csv')
plt.show(sns.distplot(a['YEAR'])

#For new years we follow a regression model.
if x>2017:
    T = a.iloc[:,y].values #Reading values from the temperature columns
    Y = a.iloc[:,0].values #Reading values from the year column
    Y_Train, Y_Test, T_Train, T_Test = train_test_split(Y,T,test_size = 0.3, random_state = 0)
    Y_Train = Y_Train.reshape(-1,1)
    Y_Test = Y_Test.reshape(-1,1)
    T_Train = T_Train.reshape(-1,1)
    T_Test = T_Test.reshape(-1,1)
    LR = LinearRegression()
    LR.fit(Y_Train,T_Train)
    o = LR.predict([[x]])
    #print(LR.score(T_Test,T_Predict))
    print(round(o[0,0],2))