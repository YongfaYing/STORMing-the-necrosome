import csv
import pandas as pd
import numpy as np
import math 
import os
import cv2

path = r'D:/STORM images analysis/STORM/Data/TIF input/RIP3-pRIP3/TIF input_HeLa-R3 R3pR3_20210926/Output'   #The folder address of the Area_ratio.csv file
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
#print(csv_list)
c1c2_list=[]
for i in range(len(csv_list)-1):
    c1=csv_list[i]
    c2=csv_list[i+1]
    c1_=c1[0:-22]
    c2_=c2[0:-22]
    if c1_==c2_ and c1[-21]=='1' and c2[-21]=='2': 
        c1c2_list.append([c1,c2])
#print(c1c2_list)

for c1c2_name in c1c2_list:
    filename1=c1c2_name[0]+'.tif.csv'
    filename2=c1c2_name[1]+'.tif.csv'
    composite_name=c1c2_name[0][0:-22]+'_composite.png'   
    image=cv2.imread(composite_name)

    filename=c1c2_name[0][0:-22]+'_Area_ratio.csv'
    with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        label1=pd.read_csv(filename, usecols=['Label_c1'])
        label2=pd.read_csv(filename, usecols=['Label_c2'])
        area1 = pd.read_csv(filename, usecols=['Area_c1'])
        area2 = pd.read_csv(filename, usecols=['Area_c2'])
        
    filename_c1=c1c2_name[0]+'_center.csv'
    with open(filename_c1) as f1:
        reader1=csv.reader(f1)
        x1=pd.read_csv(filename_c1, usecols=['CX'])
        y1=pd.read_csv(filename_c1, usecols=['CY'])
        l1=pd.read_csv(filename_c1, usecols=['Max_L'])
        angle1=pd.read_csv(filename_c1, usecols=['Angle'])

    filename_c2=c1c2_name[1]+'_center.csv'
    with open(filename_c2) as f2:
        reader2=csv.reader(f2)
        x2=pd.read_csv(filename_c2, usecols=['CX'])
        y2=pd.read_csv(filename_c2, usecols=['CY'])
        l2=pd.read_csv(filename_c2, usecols=['Max_L'])
        angle2=pd.read_csv(filename_c2, usecols=['Angle'])

    label1=np.array(label1)   
    label1=label1.tolist()    
    label2=np.array(label2)   
    label2=label2.tolist()
    area1=np.array(area1)
    area1=area1.tolist()
    area2=np.array(area2)
    area2=area2.tolist()
    x1=np.array(x1)
    x1=x1.tolist()
    y1=np.array(y1)
    y1=y1.tolist()
    x2=np.array(x2)
    x2=x2.tolist()
    y2=np.array(y2)
    y2=y2.tolist()
    l1=np.array(l1)
    l1=l1.tolist()
    l2=np.array(l2)
    l2=l2.tolist()
    angle1=np.array(angle1)
    angle1=angle1.tolist()
    angle2=np.array(angle2)
    angle2=angle2.tolist()

    for i in range(len(label1)):
        area=area1[i][0]+area2[i][0]
        Ox=x1[label1[i][0]-1][0]*area1[i][0]/area + x2[label2[i][0]-1][0]*area2[i][0]/area
        Oy=y1[label1[i][0]-1][0]*area1[i][0]/area + y2[label2[i][0]-1][0]*area2[i][0]/area
        center_=(round(Ox),round(Oy))  

        l=l1[label1[i][0]-1][0]*area1[i][0]/area + l2[label2[i][0]-1][0]*area2[i][0]/area
        la=l*0.5+math.sqrt(area)*1.8    
        lb=la*0.7  
        axesLength=(round(la),round(lb))

        angle=angle1[label1[i][0]-1][0]*area1[i][0]/area + angle2[label2[i][0]-1][0]*area2[i][0]/area
        startAngle = 0
        endAngle = 360
        color = (255, 0, 0)
        thickness = 2  
        window_name = 'Image'
        image = cv2.ellipse(image, center_, axesLength, angle, 
                            startAngle, endAngle, color, thickness)   
        print(i)
    
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  
    cv2.imshow('Image',image)
    #cv2.waitKey(0)   
    cv2.destroyAllWindows()  
    composite_show_name=c1c2_name[0][0:-22]+'_composite_show.jpg'
    cv2.imwrite(composite_show_name,image)        #Visualization

