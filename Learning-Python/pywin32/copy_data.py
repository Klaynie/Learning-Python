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

sheetname2 = 'new sheet'
# Add new sheet
wb.Sheets.Add(After = wb.Sheets(wb.Sheets.Count)).Name = sheetname2
# Copy and paste data
wb.Sheets(sheetname).Range("A1:E10").Copy(Destination = wb.Sheets(sheetname2).Range("F1"))

# copy paste FORMAT only, which include font colour, fill colour, and border
# wb2.Sheets(sheetname).Range("A:D").Copy()
# wb.Sheets(sheetname).Range("A1").PasteSpecial(Paste=win32c.xlPasteFormats)