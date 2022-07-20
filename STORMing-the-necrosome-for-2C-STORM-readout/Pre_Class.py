import csv
import pandas as pd
import numpy as np
import math 
import os
import cv2

path = r'D:/STORM images analysis/STORM/Data/TIF input/RIP3-pRIP3/TIF input_HeLa-R3 R3pR3_20210926/HeLa-R3pR3 csv'  #The folder address of the overlap_detail.csv file 
path_list=os.listdir(path)
#print(path_list)
csv_list=[]
for file_name in path_list:
    if os.path.splitext(file_name)[1] == '.csv':
        file_name=os.path.splitext(file_name)[0]  
        csv_list.append(file_name)
csv_list.sort()
#print(csv_list)
detail_list=[]
for i in range(len(csv_list)-1):
    c=csv_list[i]
    if c[-14:]=='overlap_detail': 
        detail_list.append(c)
#print(detail_list)

for detail_ in detail_list:
    detail_name=detail_+'.csv'
    with open(detail_name) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        label_c1=pd.read_csv(detail_name, usecols=[0]) 
        label_c1_part=pd.read_csv(detail_name, usecols=[1])
        label_c1_detail=pd.read_csv(detail_name, usecols=[8])
        label_c2=pd.read_csv(detail_name, usecols=[2]) 
        label_c2_part=pd.read_csv(detail_name, usecols=[3]) 
        label_c2_detail=pd.read_csv(detail_name, usecols=[14])
        area_c1 = pd.read_csv(detail_name, usecols=[9])
        feret_c2=pd.read_csv(detail_name, usecols=[16])
        AR_c2=pd.read_csv(detail_name, usecols=[18])

    label_c1=np.array(label_c1)   
    label_c1=label_c1.tolist() 
    label_c1_part=np.array(label_c1_part)   
    label_c1_part=label_c1_part.tolist()
    label_c1_detail=np.array(label_c1_detail)   
    label_c1_detail=label_c1_detail.tolist() 
    label_c2=np.array(label_c2)   
    label_c2=label_c2.tolist()
    label_c2_part=np.array(label_c2_part)   
    label_c2_part=label_c2_part.tolist()
    label_c2_detail=np.array(label_c2_detail)   
    label_c2_detail=label_c2_detail.tolist()
    area_c1=np.array(area_c1)
    area_c1=area_c1.tolist()
    feret_c2=np.array(feret_c2)
    feret_c2=feret_c2.tolist()
    AR_c2=np.array(AR_c2)
    AR_c2=AR_c2.tolist()

    labeld_c1=[[]]
    labeld_c2=[[]]
    for label1 in label_c1_detail:
        if pd.isnull(label1[0]):   
            break
        labeld_c1[0].append(int(label1[0]))
    for label2 in label_c2_detail:
        if pd.isnull(label2[0]):
            break
        labeld_c2[0].append(int(label2[0]))

    PC=[['Label','c2_AR','c2_Feret','c1_area']]
    max_feret=0
    num_c2=len(labeld_c2[0])
    for i in range(num_c2):
        length_=float(feret_c2[i][0])
        max_feret=max(max_feret,length_)
    lab_c1=str(label_c1[0][0])
    lab_c2=str(label_c2[0][0])
    PC.append(['label_'+lab_c1+'+'+lab_c2])
    str_max_feret=str(max_feret)
    list_max_feret=[str_max_feret]
    PC[1].append(AR_c2[feret_c2.index(list_max_feret)][0])
    PC[1].append(feret_c2[feret_c2.index(list_max_feret)][0])
    num_c1=len(labeld_c1[0])
    for i in range(num_c1):
        PC[1].append(int(area_c1[i][0]))
    index_=[]
    for index_i in range(len(label_c1)):

        if label_c1[index_i][0] == 'Label_c1':
            index_.append(index_i)
    #print(index_)
    
    c_i=1
    pc_i=2
    for index in index_:
        labeld_c1.append([label_c1_detail[index][0]])
        labeld_c2.append([label_c2_detail[index][0]])
        for label1 in label_c1_detail[index+1:]:
            if pd.isnull(label1[0]):   
                break
            labeld_c1[c_i].append(int(label1[0]))
        for label2 in label_c2_detail[index+1:]:
            if pd.isnull(label2[0]):
                break
            labeld_c2[c_i].append(int(label2[0]))
        max_feret=0
        num_c2=len(labeld_c2[c_i])-1
        for i in range(num_c2):
            length_=float(feret_c2[index+1+i][0])
            max_feret=max(max_feret,length_)
        lab_c1=str(label_c1[index+1][0])
        lab_c2=str(label_c2[index+1][0])
        PC.append(['label_'+lab_c1+'+'+lab_c2])
        str_max_feret=str(max_feret)
        list_max_feret=[str_max_feret]
        PC[pc_i].append(AR_c2[feret_c2.index(list_max_feret)][0])
        PC[pc_i].append(feret_c2[feret_c2.index(list_max_feret)][0])
        num_c1=len(labeld_c1[c_i])-1
        for i in range(num_c1):
            PC[pc_i].append(int(area_c1[index+1+i][0]))
        c_i+=1
        pc_i+=1
    max_len=0
    for pc_ in PC:
        len_=len(pc_)
        max_len=max(max_len,len_)
    for j in range(len(PC)):
        add_len=max_len-len(PC[j])
        PC[j].extend(add_len*[''])
    PC_trans = list(map(list, zip(*PC)))

    Pre_Class1_name=detail_name[0:-19]+'_Pre_Class_1.csv'
    with open(Pre_Class1_name, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in PC:
            writer.writerow(row)
    Pre_Class2_name=detail_name[0:-19]+'_Pre_Class_2.csv'
    with open(Pre_Class2_name, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in PC_trans:
            writer.writerow(row)
    
        




    