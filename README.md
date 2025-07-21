# **1.Gradient Descent Algorithm**
## Dataset used - [kaggle dataset](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/house-prices-india)

## (a) Batch Gradient Descent from Scratch:
- 2 features used - Area of the house (excluding the basement) and Price.
- 2200 rows of data used and 10 iterations performed.
- Refer to the file `Sbatchgradientdescent.py` for the full code.
- Data has been normalised to avoid any errors due to large values of price.
- Graph plotted using matplotlib.pyplot shown below:
- MSE value after 100 iterations = 104216.281

## (b) Stochastic Batch Gradient Descent from Scratch:
- 2 features used - Area of the house (excluding the basement) and Price.
- 2200 rows of data used and 10 iterations performed.
- Refer to the file `stochasticbatchgradientdescent.py` for the full code.
- Data has been normalised to avoid any errors due to large values of price.
- Graph plotted using matplotlib.pyplot shown below:
- MSE value after 100 iterations = 103843.936

## (c) Batch Gradient Descent using SKLearn:
- 2 features used - Area of the house (excluding the basement) and Price.
- 2200 rows of data used.
- Refer to the file `batchgradientdescent.py` for the full code.
- Graph plotted using matplotlib.pyplot shown below:
