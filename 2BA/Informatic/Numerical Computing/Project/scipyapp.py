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
AGERANGE = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']
for i in range(2, max_row+1):
    agegroup = sheet.cell(row = i, column = 4).value
    gender = sheet.cell(row = i, column = 5).value
    cases = sheet.cell(row = i, column = 6).value
    
    if agegroup is not None and gender is not None and cases is not None:
        data.append((agegroup, gender, cases))

dtype = [('agegroup', 'U5'), ('gender', 'U1'), ('cases', int)]
dataset = np.asarray(data, dtype=dtype)

dt = []
for age in AGERANGE:
    condition = np.isin(dataset['agegroup'], age)
    index = np.where(condition)
    total = dataset["cases"][index].sum()
    dt.append((age, total))

new_dataset = np.asarray(dt, dtype=[('agegroup', 'U5'), ('cases', int)])
print(new_dataset)