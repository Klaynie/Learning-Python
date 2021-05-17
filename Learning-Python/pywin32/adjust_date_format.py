import pandas as pd
import os
from pathlib import Path
import win32com.client as win32
import openpyxl

f_path = os.path.dirname(__file__)  # file in current working directory
f_name = 'example.xlsx' # Excel File name
filename = os.path.join(f_path, f_name)

document = openpyxl.load_workbook(filename)  # Opens excel document
sheet = document.active

for cell in sheet["A"]:
    cell.number_format = "YYYY-MM-DD"