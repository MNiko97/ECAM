import json, os, openpyxl

ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"
FILE = "list.xlsx"

wb = openpyxl.Workbook() 
sheet = wb.active 

with open(ROOT + 'data.json', 'r') as json_file :
    data = json.load(json_file)
    i = 1
    for key, value in data.items():
        if "ISBN ERROR: search mannualy" in value:
            sheet.cell(row = i, column = 1).value = int(value["ISBN ERROR: search mannualy"])
        else:
            sheet.cell(row = i, column = 1).value = int(value['isbn'])
        i+=1
    wb.save(ROOT + FILE) 