import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('experiencesalarydata.csv')
print(df.columns)

x = df[['Experience']] #double brackets for 2d array
y = df['Salary']

# x = np.array([1,2,3,4,5]).reshape(-1,1) 
# sklearn needs a 2d array because scikit expects features to be in columns and samples in rows
# i.e. if there is a table between experience and salary, each row which is one person is a sample and column is a feature.
# why not reshape salary? it is not a feature in this case, it is the output value we are trying to predict.

# y = np.array([10000,15000,20000,25000,30000])

model = LinearRegression()
model.fit(x,y)

m = model.coef_[0]
# model.coef_ gives an array of the leraned slopes (one per feature) and [0] extracts the only value here (only one feature - experience) 
# which is the slope m

c = model.intercept_


print(f"Slope: {m}")
print(f"Intercept: {c}")

xprediction = np.array([[10]])
# again we put the value to be predicted in a 2d array

predictedSalary = model.predict(xprediction)[0]
# the function returns a 1 element array so [0] access the value 

print(f"Predicted salary for 10 years of experience: {predictedSalary:.2f}")

# plotting:

plt.scatter(x,y,color='blue',label='Data points')
# mark the given data points

plt.plot(x,model.predict(x),color='red',label='Regression Line')

plt.scatter(10,predictedSalary,color='green',label='Predicted value')

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.legend()
# shows the key of the graph

plt.show()
# plot window display