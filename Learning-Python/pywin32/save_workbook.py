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
excel.Visible = False 
# open Excel Workbook   
wb = excel.Workbooks.Open(filename)

# insert a new row by shifting the original row down
wb.Sheets(sheetname).Rows("2:4").Insert(win32c.xlShiftDown)


f_name_new = 'example_new.xlsx' # Excel File name
subfoler = 'new'
filename_new = os.path.join(f_path, subfoler, f_name_new)
# Save workbook with new filename
wb.SaveAs(Filename=filename_new)
# Close workbook
wb.Close(SaveChanges=False)