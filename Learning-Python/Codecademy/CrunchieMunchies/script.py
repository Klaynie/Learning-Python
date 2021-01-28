import numpy as np
import os

script_dir = os.path.dirname(__file__)
file_name = 'cereal.csv'
abs_file_path = os.path.join(script_dir, file_name)

calorie_stats = np.genfromtxt(abs_file_path, delimiter=',')

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

nth_percentile = -1
for i in range(1, 100, 1):
    if float(np.percentile(calorie_stats, i)) < 60:
        nth_percentile = np.percentile(calorie_stats, i)

print(nth_percentile)

percentage = np.mean(calorie_stats > 60)
print(percentage)

calorie_std = np.std(calorie_stats)
print(calorie_std)
