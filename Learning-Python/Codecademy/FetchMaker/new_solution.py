# Import libraries
from scipy.stats import chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
from scipy.stats import binom_test
import numpy as np
import pandas as pd

# Import data
dogs = pd.read_csv('dog_data.csv')

# Inspect first few rows of data
print(dogs.head())

# Save the is_rescue column for whippets
whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']

# Calculate and print the number of whippet rescues
num_whippet_rescues = np.sum(whippet_rescue == 1)
print(num_whippet_rescues)

# Calculate and print the number of whippets
num_whippets = len(whippet_rescue)
print(num_whippets)

# Run a binomial test
pval = binom_test(num_whippet_rescues, num_whippets, .08)
print(pval)

# Save the weights of whippets, terriers, and pitbulls
wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

# Run an ANOVA
Fstat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Run Tukey's Range Test
output = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed)
print(output)

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

# Create a contingency table of color vs. breed
xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print(xtab)

# Run a Chi-Square Test
chi2, pval, dof, exp = chi2_contingency(xtab)
print(pval)