from datetime import date
from pathlib import Path
import openpyxl as oxl
import win32com.client as win32
import numpy as np
import pandas as pd
import random
import os

def create_test_excel_file(f_path: Path, f_name: str, sheet_name: str):
    
    filename = os.path.join(f_path, f_name)
    random.seed(365)
    np.random.seed(365)
    number_of_data_rows = 1000
    
    # create list of 31 dates
    dates = pd.bdate_range(date(2019, 9, 1), freq='1d', periods=31).tolist()
    # create the dataframe
    data = {'Date': [random.choice(dates) for _ in range(number_of_data_rows)],
            'Gender': [random.choice(['Female', 'Male']) for _ in range(number_of_data_rows)],
            'Products': [random.choice(['Shirts', 'Pants', 'Caps', 'Socks']) for _ in range(number_of_data_rows)],
            'Quantity': [np.random.randint(1, 11) for _ in range(number_of_data_rows)],
            'Price': np.random.normal(15, 5, size=(1, number_of_data_rows))[0]}
    # Save dataframe to Excel
    pd.DataFrame(data).to_excel(filename, index=False, sheet_name=sheet_name, float_format='%.2f')

# sheet name 
sheet_name = 'example'  # update with sheet name from your file
# file path
f_path = os.path.dirname(__file__)  # file in current working directory
# f_path = Path(r'c:\...\Documents')  # file located somewhere else
# excel file name
f_name = 'example.xlsx'
create_test_excel_file(f_path, f_name, sheet_name)