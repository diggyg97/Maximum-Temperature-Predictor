import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 

a = pd.read_csv('/Users/digvijayghotane/Desktop/Projects/Temp-Predict/dataset.csv').dropna()

#For year input where x is the year input between 1901 to 9999.
while True:
    x = input("\nOf which year do you want to know the maximum temperature? Please input a year: ")
    if x.isdigit():
        x=int(x)
        if 1901<=x<=9999:
            break
        else:
            print("\nError! Please enter a year between 1901-9999. Please understand the further away you go into the future, the less accurate the prediction will be.")
    else:
        print("\nError! Please enter a valid input year, that is, a four digit integer.")

#For month input where y is the integer input corresponding to the column integral value assigned at the dataset and the month.
while True:
    y = input("\nFor which time period do you want to predict the value?\n\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n13. Annual\n14. January-February\n15. March-May\n16. June-September\n17. October-December\n\nPlease input the corresponding integer: ")
    if y.isdigit():
        y=int(y)
        if 1<=y<=17:
            break
        else:
            print("\nError! Please enter a digit corresponding to the time period/months as printed.")
    else:
        print("\nError! Please enter an integer between 1-17, inclusive.")

#For already existing values.
for i in range(0,117):
    if x == a.iloc[i][0]:
        print("\nThe maximum temperature in the year",x,"for",a.columns[y],"is",a.iloc[i][y])