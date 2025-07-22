# stochastic batch gradient from scratch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n=2200

data = pd.read_csv('House Price India.csv',nrows=n)
x = data['Area of the house(excluding basement)']
y = data['Price']

x = np.array(x)
y = np.array(y)

# normalising the data to prevent features with large values dominating
# using min max scaling

xmin,ymin = x.min(),y.min()
xmax,ymax = x.max(),y.max()

x = (x-xmin)/(xmax-xmin)
y = (y-ymin)/(ymax-ymin)

iterations = 100
learningRate = 0.001
m=1.0
c=0.0

minimumSquareErrors = []

for _ in range(iterations):
  # pick a random index
  i = np.random.randint(0,n)
  xi = x[i]
  yi = y[i]
  
  ypred = m*xi+c 
  
  dm = -2*(yi-ypred)*xi 
  dc = -2*(yi-ypred) 
  
  # update the parameters
  m-=learningRate*dm 
  c-=learningRate*dc 
  
  # compute mse
  fullpred = m*x+c 
  mse = np.mean((y-fullpred)**2)
  minimumSquareErrors.append(mse)



# print([f"{mse:.6f}" for mse in minimumSquareErrors])
print(minimumSquareErrors[0],minimumSquareErrors[-1])

# denormalize prediction
def denormalize(o):
  return o * (ymax - ymin) + ymin

def normaliseInputX(o):
  return (o-xmin)/(xmax-xmin)

def prediction(x):
  return m*x+c

ypred = m*x+c

f = int(input("Enter the area you want to find the price for: "))
f = normaliseInputX(f)
p = prediction(f)

print(f"{denormalize(p):.2f} is the predicted value of the price!")
print(denormalize(0.007115621071066282))

plt.scatter(x,y)
plt.title('Stochastic Gradient Descent')
plt.xlabel('Area of house (excluding basement)')
plt.ylabel('Price')



plt.plot(x,ypred,color='yellow')
plt.scatter(f,p,color='red')
plt.text(f,p,'Required Point')
plt.show()