import csv
import pandas as pd
import numpy as np
import math 
import os
import cv2

path = r'D:/STORM images analysis/STORM/Data/TIF input/RIP3-pRIP3/TIF input_HeLa-R3 R3pR3_20210926/Output'  #The folder address of the csv result file
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

def iteration_c1():   
    lab=labeld_c1[r]
    la=set(lab) 
    d=[]
    for d1 in labeld_c1:
        for d2 in d1:
            d.append(d2)
    d=set(d) 
    for k in range(len(label_c1)):
        if label_c1[k][0] not in d:  
            for l in la:  
                x0=abs(x_c1[k][0]-x_c1[int(l)-1][0])
                y0=abs(y_c1[k][0]-y_c1[int(l)-1][0])
                m=max(area_c1[k][0],area_c1[int(l)-1][0])
                m=math.sqrt(m)
                global a_c1
                if (x0<20 and y0<20) or (x0<m*2 and y0<m*2):  
                    labeld_c1[r].append(label_c1[k][0])
                    a_c1=a_c1+area_c1[k][0]
                    break
def iteration_c2():   
    lab=labeld_c2[r]
    la=set(lab) 
    d=[]
    for d1 in labeld_c2:
        for d2 in d1:
            d.append(d2)
    d=set(d) 
    for k in range(len(label_c2)):
        if label_c2[k][0] not in d:  
            for l in la:  
                x0=abs(x_c2[k][0]-x_c2[int(l)-1][0])
                y0=abs(y_c2[k][0]-y_c2[int(l)-1][0])
                m=max(area_c2[k][0],area_c2[int(l)-1][0])
                m=math.sqrt(m)
                global a_c2
                if (x0<20 and y0<20) or (x0<m*2 and y0<m*2):   
                    labeld_c2[r].append(label_c2[k][0])
                    a_c2=a_c2+area_c2[k][0]
                    break

for c1c2_name in c1c2_list:
    filename1=c1c2_name[0]+'.tif.csv'
    filename2=c1c2_name[1]+'.tif.csv'
    with open(filename1) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        label_c1=pd.read_csv(filename1, usecols=[' '])   
        area_c1 = pd.read_csv(filename1, usecols=['Area'])
        x_c1=pd.read_csv(filename1, usecols=['XM'])
        y_c1=pd.read_csv(filename1, usecols=['YM'])
        feret_c1=pd.read_csv(filename1, usecols=['Feret'])
        minferet_c1=pd.read_csv(filename1, usecols=['MinFeret'])
        AR_c1=pd.read_csv(filename1, usecols=['AR'])
    with open(filename2) as f:
        reader=csv.reader(f)
        header_row=next(reader)   
        label_c2=pd.read_csv(filename2, usecols=[' '])   
        area_c2 = pd.read_csv(filename2, usecols=['Area'])
        x_c2=pd.read_csv(filename2, usecols=['XM'])
        y_c2=pd.read_csv(filename2, usecols=['YM'])
        feret_c2=pd.read_csv(filename2, usecols=['Feret'])
        minferet_c2=pd.read_csv(filename2, usecols=['MinFeret'])
        AR_c2=pd.read_csv(filename2, usecols=['AR'])

    label_c1=np.array(label_c1)   
    label_c1=label_c1.tolist()    
    area_c1=np.array(area_c1)
    area_c1=area_c1.tolist()
    x_c1=np.array(x_c1)
    x_c1=x_c1.tolist()
    y_c1=np.array(y_c1)
    y_c1=y_c1.tolist()
    feret_c1=np.array(feret_c1)
    feret_c1=feret_c1.tolist()
    minferet_c1=np.array(minferet_c1)
    minferet_c1=minferet_c1.tolist()
    AR_c1=np.array(AR_c1)
    AR_c1=AR_c1.tolist()
    label_c2=np.array(label_c2)   
    label_c2=label_c2.tolist()    
    area_c2=np.array(area_c2)
    area_c2=area_c2.tolist()
    x_c2=np.array(x_c2)
    x_c2=x_c2.tolist()
    y_c2=np.array(y_c2)
    y_c2=y_c2.tolist()
    feret_c2=np.array(feret_c2)
    feret_c2=feret_c2.tolist()
    minferet_c2=np.array(minferet_c2)
    minferet_c2=minferet_c2.tolist()
    AR_c2=np.array(AR_c2)
    AR_c2=AR_c2.tolist()

    Label_c1=['Label_c1']
    Area_c1=['Area_c1']
    labeld_c1=[['Label_part_c1']]
    r=1
    for i in range(len(label_c1)):
        a_c1=0
        d=[]
        for d1 in labeld_c1:
            for d2 in d1:
                d.append(d2)
        d=set(d)
        if label_c1[i][0] not in d:   
            labeld_c1.append([label_c1[i][0]])
            a_c1+=area_c1[i][0]
            for j in range(len(label_c1)):
                if label_c1[i][0]==label_c1[j][0] or label_c1[j][0] in d:
                    continue
                x0=abs(x_c1[i][0]-x_c1[j][0])
                y0=abs(y_c1[i][0]-y_c1[j][0])
                m=max(area_c1[i][0],area_c1[j][0])
                m=math.sqrt(m)
                if (x0<20 and y0<20) or (x0<m*2 and y0<m*2):     
                    labeld_c1[r].append(label_c1[j][0])
                    a_c1+=area_c1[j][0] 
            for v in range(10):
                iteration_c1()  

            if a_c1>10:     
                Area_c1.append(a_c1)
                Label_c1.append(r)
                r+=1
            else:
                del labeld_c1[r]

    rows=zip(Label_c1,labeld_c1,Area_c1)
    print(rows)
    Filename_c1=c1c2_name[0]+'_Area.csv'     #c1 protein overall area
    with open(Filename_c1, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)

    Label_c2=['Label_c2']
    Area_c2=['Area_c2']
    labeld_c2=[['Label_part_c2']]
    r=1
    for i in range(len(label_c2)):
        a_c2=0
        d=[]
        for d1 in labeld_c2:
            for d2 in d1:
                d.append(d2)
        d=set(d)
        if label_c2[i][0] not in d:   
            labeld_c2.append([label_c2[i][0]])
            a_c2+=area_c2[i][0]
            for j in range(len(label_c2)):
                if label_c2[i][0]==label_c2[j][0] or label_c2[j][0] in d:
                    continue
                x0=abs(x_c2[i][0]-x_c2[j][0])
                y0=abs(y_c2[i][0]-y_c2[j][0])
                m=max(area_c2[i][0],area_c2[j][0])
                m=math.sqrt(m)
                if (x0<20 and y0<20) or (x0<m*2 and y0<m*2):  
                    labeld_c2[r].append(label_c2[j][0])
                    a_c2+=area_c2[j][0] 
            for v in range(10):
                iteration_c2()  

            if a_c2>40:     
                Area_c2.append(a_c2)
                Label_c2.append(r)
                r+=1
            else:
                del labeld_c2[r]

    rows=zip(Label_c2,labeld_c2,Area_c2)
    print(rows)
    Filename_c2=c1c2_name[1]+'_Area.csv'    #c2 protein overall area
    with open(Filename_c2, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)

    image_name=c1c2_name[0]+'.jpg'   
    image=cv2.imread(image_name)
    Index=0
    center_x_c1=['CX']
    center_y_c1=['CY']   
    max_l_c1=['Max_L']
    angle_c1=['Angle']
    for i in labeld_c1[1:]:
        x0=[]
        y0=[]
        area0=[]
        for j in i:
            x0.append(x_c1[j-1][0])
            y0.append(y_c1[j-1][0])
            area0.append(area_c1[j-1][0])
        
        if len(x0)>1:
            L=[]
            dx=[]
            dy=[]
            T0=[]
            Ox=0
            Oy=0
            for c in range(len(x0)):  
                Ox+=x0[c]*area0[c]/Area_c1[Index+1]
                Oy+=y0[c]*area0[c]/Area_c1[Index+1]
            center_x_c1.append(Ox)
            center_y_c1.append(Oy)
            center_=(round(Ox),round(Oy))  

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
            max_l_c1.append(l)
            index0=L.index(max(L))  
            dx=dx[index0]
            dy=dy[index0]
            la=l*0.5+math.sqrt(Area_c1[Index+1])*1.5      
            lb=la/2  
            axesLength=(round(la),round(lb))
            if T0[index0]==True:
                p=math.degrees(math.asin(dy/l))   
            else:
                p=180-math.degrees(math.asin(dy/l))      
            angle=p
            angle_c1.append(angle)
            startAngle = 0
            endAngle = 360
            color = (255, 0, 0)
            thickness = 2  
            window_name = 'Image'
            image = cv2.ellipse(image, center_, axesLength, angle, 
                                startAngle, endAngle, color, thickness) 
            text=str(Index+1)
            place=(round(Ox)-40,round(Oy)+25)    
            cv2.putText(image, text, place, cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
            
        if len(x0)==1:
            r=round(math.sqrt(Area_c1[Index+1]*2))
            max_l_c1.append(r)
            angle_c1.append(0)
            center_x_c1.append(x0[0])
            center_y_c1.append(y0[0])
            center_=(round(x0[0]),round(y0[0]))
            image = cv2.circle(image,center_,r,(255,0,0),2)
            text=str(Index+1)
            place=(round(x0[0])-30,round(y0[0])+30)   
            cv2.putText(image, text, place, cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
            
        print(i)
        Index+=1  
    
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  
    cv2.imshow('Image',image)
    #cv2.waitKey(0)   
    cv2.destroyAllWindows()
    show_name=c1c2_name[0]+'_show.jpg'  
    cv2.imwrite(show_name,image)    #c1 Visualization
    
    c1center_name=c1c2_name[0]+'_center.csv'
    rows=zip(center_x_c1,center_y_c1,max_l_c1,angle_c1)
    with open(c1center_name, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)  

    image_name=c1c2_name[1]+'.jpg'   
    image=cv2.imread(image_name)
    Index=0
    center_x_c2=['CX']
    center_y_c2=['CY']   
    max_l_c2=['Max_L']
    angle_c2=['Angle']
    for i in labeld_c2[1:]:
        x0=[]
        y0=[]
        area0=[]
        for j in i:
            x0.append(x_c2[j-1][0])
            y0.append(y_c2[j-1][0])
            area0.append(area_c2[j-1][0])
        
        if len(x0)>1:
            L=[]
            dx=[]
            dy=[]
            T0=[]
            Ox=0
            Oy=0
            for c in range(len(x0)):  
                Ox+=x0[c]*area0[c]/Area_c2[Index+1]
                Oy+=y0[c]*area0[c]/Area_c2[Index+1]
            center_x_c2.append(Ox)
            center_y_c2.append(Oy)
            center_=(round(Ox),round(Oy))  

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
            max_l_c2.append(l)
            index0=L.index(max(L))  
            dx=dx[index0]
            dy=dy[index0]
            la=l*0.5+math.sqrt(Area_c2[Index+1])*1.5   
            lb=la/2  
            axesLength=(round(la),round(lb))
            if T0[index0]==True:
                p=math.degrees(math.asin(dy/l))   
            else:
                p=180-math.degrees(math.asin(dy/l))      
            angle=p
            angle_c2.append(angle)
            startAngle = 0
            endAngle = 360
            color = (255, 0, 0)
            thickness = 2  
            window_name = 'Image'
            image = cv2.ellipse(image, center_, axesLength, angle, 
                                startAngle, endAngle, color, thickness) 
            text=str(Index+1)
            place=(round(Ox)+40,round(Oy)+25)     
            cv2.putText(image, text, place, cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
            
        if len(x0)==1:
            r=round(math.sqrt(Area_c2[Index+1]*2))
            max_l_c2.append(r)
            angle_c2.append(0)
            center_x_c2.append(x0[0])
            center_y_c2.append(y0[0])
            center_=(round(x0[0]),round(y0[0]))
            image = cv2.circle(image,center_,r,(255,0,0),2)
            text=str(Index+1)
            place=(round(x0[0])+30,round(y0[0])+30)    
            cv2.putText(image, text, place, cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)     
        print(i)
        Index+=1 
       
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  
    cv2.imshow('Image',image)
    #cv2.waitKey(0)   
    cv2.destroyAllWindows()
    show_name=c1c2_name[1]+'_show.jpg'  
    cv2.imwrite(show_name,image)    #c2 Visualization
    
    c2center_name=c1c2_name[1]+'_center.csv'
    rows=zip(center_x_c2,center_y_c2,max_l_c2,angle_c2)
    with open(c2center_name, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)    

    filename01=c1c2_name[0]+'_center.csv'
    filename02=c1c2_name[1]+'_center.csv'
    with open(filename01) as f01:
        reader01=csv.reader(f01)
        header_row=next(reader01)   
        xy1=pd.read_csv(filename01, usecols=['CX','CY'])   
    with open(filename02) as f02:
        reader02=csv.reader(f02)
        xy2=pd.read_csv(filename02, usecols=['CX','CY'])

    xy1=np.array(xy1)
    xy1=xy1.tolist()
    xy2=np.array(xy2)
    xy2=xy2.tolist()

    label01=['Label_c1']
    label01_detail=[]
    label01_part_detail=[]
    label02=['Label_c2']
    label02_detail=[]
    label02_part_detail=[]
    area01=['Area_c1']
    area01_detail=[]
    area02=['Area_c2']
    area02_detail=[]
    value=['Area1/Area2']
    value_detail=[]
    C1_=['']
    label_part_detail_c1=[]  
    area_part_detail_c1=[]
    feret_part_detail_c1=[]
    minferet_part_detail_c1=[]
    AR_part_detail_c1=[]
    C2_=['']
    label_part_detail_c2=[]  
    area_part_detail_c2=[]
    feret_part_detail_c2=[]
    minferet_part_detail_c2=[]
    AR_part_detail_c2=[]
    i1=0   
    for x1, y1 in xy1:
        j1=0  
        for x2, y2 in xy2:
            x=abs(x1-x2)
            y=abs(y1-y2)
            a=Area_c1[i1+1]   
            b=Area_c2[j1+1]
            max_=a if a > b else b   
            m=math.sqrt(max_)
            if x<m*2 and y<m*2:    #Parameters for judging whether two proteins overlap
                label01_detail.append('Label_c1')
                label01_part_detail.append('Label_c1_part')
                label02_detail.append('Label_c2')
                label02_part_detail.append('Label_c2_part')
                area01_detail.append('Area_c1')
                area02_detail.append('Area_c2')
                value_detail.append('Area1/Area2')
                label_part_detail_c1.append('Label_detail')
                area_part_detail_c1.append('Area')
                feret_part_detail_c1.append('Feret')
                minferet_part_detail_c1.append('MinFeret')
                AR_part_detail_c1.append('AR') 
                label_part_detail_c2.append('Label_detail')
                area_part_detail_c2.append('Area')
                feret_part_detail_c2.append('Feret')
                minferet_part_detail_c2.append('MinFeret')
                AR_part_detail_c2.append('AR') 
                label01.append(Label_c1[i1+1])
                label01_detail.append(Label_c1[i1+1])
                label01_part_detail.append(labeld_c1[Label_c1[i1+1]])
                label02.append(Label_c2[j1+1])
                label02_detail.append(Label_c2[j1+1])
                label02_part_detail.append(labeld_c2[Label_c2[j1+1]])
                area01.append(Area_c1[i1+1])
                area01_detail.append(Area_c1[i1+1])
                area02.append(Area_c2[j1+1])
                area02_detail.append(Area_c2[j1+1])
                v=Area_c1[i1+1]/Area_c2[j1+1]
                value.append(v)
                value_detail.append(v)
                C1_.append('C1')
                for l_detail in labeld_c1[Label_c1[i1+1]]:
                    label_part_detail_c1.append(l_detail)
                    area_part_detail_c1.append(area_c1[l_detail-1][0])
                    feret_part_detail_c1.append(feret_c1[l_detail-1][0])
                    minferet_part_detail_c1.append(minferet_c1[l_detail-1][0])
                    AR_part_detail_c1.append(AR_c1[l_detail-1][0])
                    C1_.append('')
                C2_.append('C2')
                for l_detail in labeld_c2[Label_c2[j1+1]]:
                    label_part_detail_c2.append(l_detail)
                    area_part_detail_c2.append(area_c2[l_detail-1][0])
                    feret_part_detail_c2.append(feret_c2[l_detail-1][0])
                    minferet_part_detail_c2.append(minferet_c2[l_detail-1][0])
                    AR_part_detail_c2.append(AR_c2[l_detail-1][0])
                    C2_.append('')
                if len(labeld_c1[Label_c1[i1+1]])>len(labeld_c2[Label_c2[j1+1]]):
                    for di_c2 in range(len(labeld_c1[Label_c1[i1+1]])-len(labeld_c2[Label_c2[j1+1]])):
                        C2_.append('')
                        label_part_detail_c2.append('')
                        area_part_detail_c2.append('')
                        feret_part_detail_c2.append('')
                        minferet_part_detail_c2.append('')
                        AR_part_detail_c2.append('')
                elif len(labeld_c1[Label_c1[i1+1]])<len(labeld_c2[Label_c2[j1+1]]):
                    for di_c1 in range(len(labeld_c2[Label_c2[j1+1]])-len(labeld_c1[Label_c1[i1+1]])):
                        C1_.append('')
                        label_part_detail_c1.append('')
                        area_part_detail_c1.append('')
                        feret_part_detail_c1.append('')
                        minferet_part_detail_c1.append('')
                        AR_part_detail_c1.append('')
                max_di=max(len(labeld_c1[Label_c1[i1+1]]),len(labeld_c2[Label_c2[j1+1]]))
                for di__ in range(max_di):
                    label01_detail.append('')
                    label01_part_detail.append('')
                    label02_detail.append('')
                    label02_part_detail.append('')
                    area01_detail.append('')
                    area02_detail.append('')
                    value_detail.append('')
                C1_.append('')
                label_part_detail_c1.append('')
                area_part_detail_c1.append('')
                feret_part_detail_c1.append('')
                minferet_part_detail_c1.append('')
                AR_part_detail_c1.append('')
                C2_.append('')
                label_part_detail_c2.append('')
                area_part_detail_c2.append('')
                feret_part_detail_c2.append('')
                minferet_part_detail_c2.append('')
                AR_part_detail_c2.append('')
            j1+=1
        i1+=1

    rows=zip(label01,label02,area01,area02,value)
    print(rows)
    Ratio_name=c1c2_name[0][0:-22]+'_Area_ratio.csv'   #The ratio of the area of the two proteins in the overlapping part
    with open(Ratio_name, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)
    rows=zip(label01_detail,label01_part_detail,label02_detail,label02_part_detail,area01_detail,area02_detail,value_detail,C1_,label_part_detail_c1,area_part_detail_c1,feret_part_detail_c1,minferet_part_detail_c1,AR_part_detail_c1,C2_,label_part_detail_c2,area_part_detail_c2,feret_part_detail_c2,minferet_part_detail_c2,AR_part_detail_c2)
    print(rows)
    Ratio_name=c1c2_name[0][0:-22]+'_overlap_detail.csv'  #Two protein details in the overlapping part
    with open(Ratio_name, 'w', newline='') as csvfile:   
        writer  = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)
    


    