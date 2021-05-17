import pandas as pd
import os
from pathlib import Path
import win32com.client as win32

f_path = os.path.dirname(__file__)  # file in current working directory
f_name = 'example.xlsx' # Excel File name
filename = os.path.join(f_path, f_name)
sheetname = 'example' # change to the name of the worksheet

# create Excel object
excel = win32.gencache.EnsureDispatch('Excel.Application')
# excel can be visible or not
excel.Visible = True 
# open Excel Workbook   
wb = excel.Workbooks.Open(filename)
# create filter in Excel Worksheet
wb.Sheets(sheetname).Range("A1").AutoFilter(Field = 2, Criteria1="Female", VisibleDropDown=True)
# AutoFit columns
wb.Sheets(sheetname).Columns("A:D").AutoFit()