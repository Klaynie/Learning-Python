import os
import csv

script_dir = os.path.dirname(__file__)
file_name = 'cool_csv.csv'
abs_file_path = os.path.join(script_dir, file_name)

with open(abs_file_path, newline='') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row['Cool Fact'])