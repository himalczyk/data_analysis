import openpyxl

theFile = openpyxl.load_workbook('report_files/matalan_p1.xlsx')
print(theFile.sheetnames)
currentSheet = theFile['Page 1']
print(currentSheet['B4'].value)