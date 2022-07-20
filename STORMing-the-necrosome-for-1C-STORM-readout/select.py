import csv
import pandas as pd
import numpy as np
import math 
import os
import cv2

path = r'D:/STORM images analysis/STORM/Data/TIF input/Time course-RIP1RIP3/Csv collection'   #The folder address of the Area.csv file
path_list=os.listdir(path)
#print(path_list)
csv_list=[]
for file_name in path_list:
    if os.path.splitext(file_name)[1] == '.csv':
        file_name=os.path.splitext(file_name)[0]
        if os.path.splitext(file_name)[1] == '.tif':
            file_name=os.path.splitext(file_name)[0]   
            csv_list.append(file_name)
csv_list.sort()

for filename_ in csv_list:
    filename=filename_+'.tif.csv'
    with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        label=pd.read_csv(filename, usecols=[' '])   
        area = pd.read_csv(filename, usecols=['Area'])
        feret=pd.read_csv(filename, usecols=['Feret'])
        minferet=pd.read_csv(filename, usecols=['MinFeret'])
        AR=pd.read_csv(filename, usecols=['AR'])

    label=np.array(label)   
    label=label.tolist()    
    area=np.array(area)
    area=area.tolist()
    feret=np.array(feret)
    feret=feret.tolist()
    minferet=np.array(minferet)
    minferet=minferet.tolist()
    AR=np.array(AR)
    AR=AR.tolist()

    label_=['Label']  
    area_=['Area']
    feret_=['Feret']
    minferet_=['MinFeret']
    AR_=['AR']

    for i in label:
        for j in i:
            if area[j-1][0]>150:   
                label_.append(j)
                area_.append(area[j-1][0])
                feret_.append(feret[j-1][0])
                minferet_.append(minferet[j-1][0])
                AR_.append(AR[j-1][0])
                
    
    label_.append(' ')
    area_.append(' ')
    feret_.append(' ')
    minferet_.append(' ')
    AR_.append(' ')

    file_=[]
    file_.append(filename_)
    rows=zip(label_,area_,feret_,minferet_,AR_)
    print(rows)
    Filename='Merge.csv'
    with open(Filename, 'a', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        writer.writerow(file_)
        for row in rows:
            writer.writerow(row)

