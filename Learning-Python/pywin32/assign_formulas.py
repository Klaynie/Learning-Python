import pandas as pd
import os
from pathlib import Path
import win32com.client as win32

win32c = win32.constants

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

# Deactivate ScreenUpdating
excel.ScreenUpdating = False

column_insert = "F"

# Insert Header
wb.Sheets(sheetname).Range(f"{column_insert}1").Value = "Total"
# Apply formating to Header
wb.Sheets(sheetname).Range("E1").Copy()
wb.Sheets(sheetname).Range(f"{column_insert}1").PasteSpecial(Paste=win32c.xlPasteFormats)

# Add Formulars
wb.Sheets(sheetname).Range(f"{column_insert}2").Formula = "=D2*E2"
wb.Sheets(sheetname).Range(f"{column_insert}2:{column_insert}1001").FillDown()

# Create your own function
column1 = "A"
column2 = "B"
operation = "+" # math operation to perform between 2 columns
def math_op(column1, column2, operation):
    wb.Sheets(sheetname).Range(f"{column_insert}2").Formula = f"={column1}2{operation}{column2}2"

# math_op(column1, column2, operation)

# Activate ScreenUpdating
excel.ScreenUpdating = True