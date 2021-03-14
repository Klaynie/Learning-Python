import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios, optimal_portfolio
import codecademylib3_seaborn
import numpy as np

# 1. Load the stock data


# 2. Find the quarterly return for each period


# 3. Find the expected returns


# 4. Find the covariance


# 5. Find a set of random portfolios


# 6. Plot the set of random portfolios


# 7. Calculate the set of portfolios on the EF


# 8. Plot the set of portfolios on the EF


# Compare the set of portfolios on the EF to the
try:
    single_asset_std = np.sqrt(np.diagonal(cov_quarterly))
    plt.scatter(single_asset_std, expected_returns,
                marker='X', color='red', s=200)
except:
    pass
plt.show()
