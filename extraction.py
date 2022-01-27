import openpyxl
from config import filename

theFile = openpyxl.load_workbook(f'report_files/{filename}.xlsx')
print(theFile.sheetnames)
currentSheet = theFile['Page 1']
print(currentSheet['B4'].value)