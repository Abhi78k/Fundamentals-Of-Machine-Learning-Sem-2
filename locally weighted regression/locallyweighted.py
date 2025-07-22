import numpy as np
import matplotlib.pyplot as plt 

# manually creating a non linear dataset using sine wave and normal function
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

learningRate = 0.001

