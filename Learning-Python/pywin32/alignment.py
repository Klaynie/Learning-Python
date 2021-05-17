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
# Set row height to 80
wb.Sheets(sheetname).Rows(1).RowHeight = 80
# Adjust cell horizontal alignment. There are three types of alignment, which are xlLeft, xlCenter and xlRight.
wb.Worksheets(sheetname).Rows("1:1").HorizontalAlignment = win32c.xlCenter
wb.Worksheets(sheetname).Rows("1:1").VerticalAlignment = win32c.xlCenter