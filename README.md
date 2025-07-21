# **1. Simple Linear Regression Model**
- Used made up data to fit a line using SKLearn and perform predictions.
- 2 features used - Salary and Experience
- Graph plotted using matplotlib.pyplot shown below:
- <img width="640" height="480" alt="simplemodel" src="https://github.com/user-attachments/assets/b7bf25d9-ce52-400c-a9d3-0253173123c6" />
- <img width="497" height="62" alt="image" src="https://github.com/user-attachments/assets/44029c55-ad88-4574-962e-722dfc50b23d" />

# **2. Gradient Descent Algorithm**
## Dataset used - [kaggle dataset](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/house-prices-india)

## (a) Batch Gradient Descent from Scratch:
- 2 features used - Area of the house (excluding the basement) and Price.
- 2200 rows of data used and 10 iterations performed.
- Refer to the file `Sbatchgradientdescent.py` for the full code.
- Data has been normalised to avoid any errors due to large values of price.
- Graph plotted using matplotlib.pyplot shown below:
- <img width="640" height="480" alt="gradientdescent" src="https://github.com/user-attachments/assets/b89a3eb8-84a3-41fb-bdbe-b33bfb889e79" />
- MSE value after 100 iterations = 104216.281
- <img width="471" height="42" alt="gdip" src="https://github.com/user-attachments/assets/2409dc92-9e51-4c94-b2c2-4dc635418349" />

## (b) Stochastic Batch Gradient Descent from Scratch:
- 2 features used - Area of the house (excluding the basement) and Price.
- 2200 rows of data used and 10 iterations performed.
- Refer to the file `stochasticbatchgradientdescent.py` for the full code.
- Data has been normalised to avoid any errors due to large values of price.
- Graph plotted using matplotlib.pyplot shown below:
- <img width="640" height="480" alt="stochasticgradientdescent" src="https://github.com/user-attachments/assets/080a6bd7-5543-4b1e-b89d-ea5fa69b5e4d" />
- MSE value after 100 iterations = 103843.936
- <img width="477" height="46" alt="image" src="https://github.com/user-attachments/assets/4dacda8b-c601-40ba-aea2-edbf7cde53ac" />


## (c) Batch Gradient Descent using SKLearn:
- 2 features used - Area of the house (excluding the basement) and Price.
- 2200 rows of data used.
- Refer to the file `batchgradientdescent.py` for the full code.
- Graph plotted using matplotlib.pyplot shown below:
- <img width="1920" height="967" alt="sklearnbatchgradientdescent" src="https://github.com/user-attachments/assets/d1db083f-0612-48c8-aabd-99a7dd932246" />
- Predicted value for 2000 area comes out to be `599873.976`.
