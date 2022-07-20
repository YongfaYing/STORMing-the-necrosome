import csv
import pandas as pd
import numpy as np
import math 
import os
import cv2

path = r'D:/STORM images analysis/STORM/Data/TIF input/Time course-RIP1RIP3/Output'   #The folder address of the csv result file
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

def iteration():   
    lab=labeld[r]
    la=set(lab) 
    d=[]
    for d1 in labeld:
        for d2 in d1:
            d.append(d2)
    d=set(d) 
    for k in range(len(label)):
        if label[k][0] not in d:  
            for l in la:  
                x0=abs(x[k][0]-x[int(l)-1][0])
                y0=abs(y[k][0]-y[int(l)-1][0])
                m=max(area[k][0],area[int(l)-1][0])
                m=math.sqrt(m)
                global a
                if (x0<20 and y0<20) or (x0<m*2 and y0<m*2):
                    labeld[r].append(label[k][0])
                    #a=a+area[k][0]
                    break

for filename_ in csv_list:
    filename=filename_+'.tif.csv'
    with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        label=pd.read_csv(filename, usecols=[' '])   
        area = pd.read_csv(filename, usecols=['Area'])
        x=pd.read_csv(filename, usecols=['XM'])
        y=pd.read_csv(filename, usecols=['YM'])
        minferet=pd.read_csv(filename, usecols=['MinFeret'])
        AR=pd.read_csv(filename, usecols=['AR'])

    label=np.array(label)   
    label=label.tolist()    
    area=np.array(area)
    area=area.tolist()
    x=np.array(x)
    x=x.tolist()
    y=np.array(y)
    y=y.tolist()
    minferet=np.array(minferet)
    minferet=minferet.tolist()
    AR=np.array(AR)
    AR=AR.tolist()

    Label=['Label']
    Area=['Area']
    labeld=[['Label_part']]
    r=1
    for i in range(len(label)):
        a=0
        d=[]
        for d1 in labeld:
            for d2 in d1:
                d.append(d2)
        d=set(d)
        if label[i][0] not in d:   
            labeld.append([label[i][0]])
            for j in range(len(label)):
                if label[i][0]==label[j][0] or label[j][0] in d:
                    continue
                x0=abs(x[i][0]-x[j][0])
                y0=abs(y[i][0]-y[j][0])
                m=max(area[i][0],area[j][0])
                m=math.sqrt(m)
                if (x0<20 and y0<20) or (x0<m*2 and y0<m*2):
                    labeld[r].append(label[j][0]) 
            for v in range(10):
                iteration()  
            for b in labeld[-1]:
                if area[b-1][0]>150:   
                    a+=area[b-1][0]

            if a>200:     
                Area.append(a)
                Label.append(r)
                r+=1
            else:
                del labeld[r]

    rows=zip(Label,labeld,Area)
    print(rows)
    Filename=filename_+'_Area.csv'    #protein overall area
    with open(Filename, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)

    image_name=filename_+'.jpg'   
    image=cv2.imread(image_name)
    with open(Filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        Area = pd.read_csv(Filename, usecols=['Area'])
    
    Area=np.array(Area)
    Area=Area.tolist()
    Index=0
    for i in labeld[1:]:
        x0=[]
        y0=[]
        area0=[]
        for j in i:
            x0.append(x[j-1][0])
            y0.append(y[j-1][0])
            area0.append(area[j-1][0])
        
        if len(x0)>1:
            L=[]
            dx=[]
            dy=[]
            T0=[]
            Ox=0
            Oy=0
            area_all=0
            for area_i in range(len(x0)):
                area_all+=area0[area_i]
            for c in range(len(x0)):  
                Ox+=x0[c]*area0[c]/area_all
                Oy+=y0[c]*area0[c]/area_all
            center_=(round(Ox),round(Oy))  #Center coordinates

            for m in range(len(x0)):
                x1=x0[m]
                y1=y0[m]
                for n in range(len(x0)):
                    if m<n:
                        x2=x0[n]
                        y2=y0[n]
                        dx0=abs(x1-x2)
                        dy0=abs(y1-y2)
                        l=math.sqrt(dx0**2+dy0**2)
                        L.append(l)
                        dx.append(dx0)
                        dy.append(dy0)
                        if (x1-x2)*(y1-y2)>0:  
                            T0.append(True)
                        else:
                            T0.append(False)
            l=max(L)
            index0=L.index(max(L))  
            dx=dx[index0]
            dy=dy[index0]
            la=l*0.5+math.sqrt(area_all)*1.5    
            lb=la/2  
            axesLength=(round(la),round(lb))
            if T0[index0]==True:
                p=math.degrees(math.asin(dy/l))   
            else:
                p=180-math.degrees(math.asin(dy/l))      
            angle=p
            startAngle = 0
            endAngle = 360
            color = (255, 0, 0)
            thickness = 2  
            window_name = 'Image'
            image = cv2.ellipse(image, center_, axesLength, angle, 
                                startAngle, endAngle, color, thickness) 
            text=str(Index+1)
            place=(round(Ox)+40,round(Oy)+40)    
            cv2.putText(image, text, place, cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 2)
            
        if len(x0)==1:
            r=round(math.sqrt(Area[Index][0]*2))
            center_=(round(x0[0]),round(y0[0]))
            image = cv2.circle(image,center_,r,(255,0,0),2)
            text=str(Index+1)
            place=(round(x0[0])+30,round(y0[0])+30)
            cv2.putText(image, text, place, cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 2)
            
        print(i)
        Index+=1  
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  
    cv2.imshow('Image',image)
    #cv2.waitKey(0)   
    cv2.destroyAllWindows()
    show_name=filename_+'_show.jpg'  
    cv2.imwrite(show_name,image)    #Visualization