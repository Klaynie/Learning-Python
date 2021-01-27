import numpy as np
import os

script_dir = os.path.dirname(__file__)
file_name = 'recipes.csv'
abs_file_path = os.path.join(script_dir, file_name)

cupcakes = np.array([2, 0.75, 2, 1, 0.5])

recipes = np.genfromtxt(abs_file_path, delimiter=',')
print(recipes)

eggs = recipes[:, 2]
print(eggs)

one_egg = recipes[(eggs == 1)]
print(one_egg)

cookies = recipes[2, :]
print(cookies)

double_batch = cupcakes * 2
print(double_batch)

grocery_list = cookies + double_batch
print(grocery_list)