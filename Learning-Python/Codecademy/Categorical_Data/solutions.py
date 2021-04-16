import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_name = 'film_permits.csv'
abs_file_path = os.path.join(script_dir, file_name)

# Read CSV
film_permits = pd.read_csv(abs_file_path)

# Look first few rows
print(film_permits.head()) 

# Nominal Vars
nominalvars = ['EventType', 'Borough', 'Category', 'SubCategoryName']

# Ordinal Vars - We might consider an Id like 'EventID' an ordinal variable in some situations

# Borough with the most permits for pilot episodes
print(film_permits[film_permits.SubCategoryName == 'Pilot'].Borough.value_counts())

# Summarize the Top Categories
print(film_permits.Category.value_counts())

# Summarize the Top Subcategories
print(film_permits.SubCategoryName.value_counts())
