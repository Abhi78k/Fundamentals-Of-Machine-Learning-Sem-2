# using sklearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('House Price India.csv',nrows=2100)

X = data['Area of the house(excluding basement)'].values.reshape(-1, 1) 
y = data['Price'].values

model = LinearRegression()

model.fit(X, y)

theta_0 = model.intercept_
theta_1 = model.coef_[0]

y_pred = model.predict(X)
print(model.predict([[2000]]))
plt.figure(figsize=(10, 5))
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, y_pred, color="red", label="Fitted Line (sklearn)")
plt.xlabel("Area of the house (excluding basement)")
plt.ylabel("Price")
plt.title("Linear Regression Using sklearn")
plt.legend()
plt.show()


print(f"Intercept (theta_0): {theta_0}")
print(f"Slope (theta_1): {theta_1}")
