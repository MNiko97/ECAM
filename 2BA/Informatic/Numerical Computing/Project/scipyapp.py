from scipy.stats import poisson
import matplotlib.pyplot as plt 
import numpy as np 
import os, openpyxl, wget

ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"
FILE = 'COVID19BE.xlsx'
SHEET = 'CASES_AGESEX'
URL= 'https://epistat.sciensano.be/Data/COVID19BE.xlsx'

'''if os.path.isfile(ROOT+FILE) :
    print("UDPDATING DATA ...")
    print('Removing file : ' + FILE)
    os.remove(ROOT+FILE)
    print("Downloading file : " + FILE)
    wget.download(URL, ROOT)
    print("\nDownload Completed Successfully  !")
else :
    print("Downloading file : " + FILE)
    wget.download(URL, ROOT)
    print("\nDownload Completed Successfully !")'''


# Opening COVID19 dataset in xlsx format
# Select sheet DEATH
print('Retrieving DATA from ' + FILE + ' ...')
book = openpyxl.load_workbook(ROOT+FILE)
sheet = book.get_sheet_by_name(SHEET)


max_row = sheet.max_row 
data = []
dtype = [('agegroup', 'U5'), ('gender', 'U1'), ('cases', int)]
print('start computing')
for i in range(2, max_row+1):
    agegroup = sheet.cell(row = i, column = 4).value
    gender = sheet.cell(row = i, column = 5).value
    cases = sheet.cell(row = i, column = 6).value
    
    if agegroup is not None and gender is not None and cases is not None:
        data.append((agegroup, gender, cases))

dataset = np.asarray(data, dtype=dtype)

dt = [('agegroup', int), ('cases', int)]
new_data = []

condition = np.isin(dataset[:, 0], i)
result = (i, np.asarray(np.where(condition)).size)
new_data.append(result)
new_dataset = np.asarray(new_data, dtype=dtype1)
sortedarray = np.sort(new_dataset, order='cases')

