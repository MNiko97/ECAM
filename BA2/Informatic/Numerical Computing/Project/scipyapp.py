import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
import numpy as np 
import os, openpyxl, wget

ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"
FILE = 'COVID19BE.xlsx'
SHEET = 'CASES_AGESEX'
URL= 'https://epistat.sciensano.be/Data/COVID19BE.xlsx'

if os.path.isfile(ROOT+FILE) :
    print("UDPDATING DATA ...")
    print('Removing file : ' + FILE)
    os.remove(ROOT+FILE)
    print("Downloading file : " + FILE)
    wget.download(URL, ROOT)
    print("\nDownload Completed Successfully  !")
else :
    print("Downloading file : " + FILE)
    wget.download(URL, ROOT)
    print("\nDownload Completed Successfully !")

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
sd = np.std(dataset['cases'])
mean = np.mean(dataset['cases'])

# for i in range(len(dataset)):
#     if dataset[i]['cases'] > 1 :
#         test = np.repeat(dataset[i], dataset[i]['cases'])
        
# print(test)

def ageSort(dataset, sex):
    dt = []
    dataset = np.delete(dataset, np.where(dataset['gender'] != sex))
    for age in AGERANGE:
        index = np.where(np.isin(dataset['agegroup'], age))
        total = dataset["cases"][index].sum()
        dt.append((age, total))
    data = np.asarray(dt, dtype=[('agegroup', 'U5'), ('cases', int)])
    return data

def plot():
    men_dataset = ageSort(dataset, 'M')
    women_dataset = ageSort(dataset, 'F')
    sd = np.std(dataset['cases'])
    mean = np.mean(dataset['cases'])

    fig, ax = plt.subplots()
    men = ax.bar(AGERANGE, men_dataset['cases'],  align='center', label='Men', picker=True)
    women = ax.bar(AGERANGE, women_dataset['cases'], align='center', bottom=men_dataset['cases'], label='Women', picker=True)
    
    title = 'COVID-19 Contamination in Belgium'
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('Age Class', fontsize='12')
    ax.set_ylabel('Infected', fontsize='12')
    ax.grid()
    ax.legend()
    
    cid = fig.canvas.mpl_connect('pick_event', onpick)
    plt.show()

def onpick(event):
    rect = event.artist
    handles,labels = rect.axes.get_legend_handles_labels()
    # Search for current artist within all plot groups
    label = [label for h,label in zip(handles, labels) if rect in h.get_children()]
    if len(label) == 1:
        label = label[0]
    else:
        label = None
    print (label)

        
plot()