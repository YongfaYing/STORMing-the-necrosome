import csv
import pandas as pd
import numpy as np
import math  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt
from scipy.stats import norm

filename=r"D:\document\image\two_color\composite\2/WT-L-2#-5-R1_Simple Segmentation.tif.csv"  #单体
# filename=r"D:\document\image\two_color\composite\2/WT-L-2#-5-R3_Simple Segmentation_Area.csv"  #多聚体
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)   #表格最上面每一列的名字
    #print(header_row)
    #结果为['Label ', 'Area', 'Feret', 'FeretX', 'FeretY', 'FeretAngle', 'MinFeret']
    label=pd.read_csv(filename, usecols=['Label'])   #读取特定的列,dataframe格式
    area = pd.read_csv(filename, usecols=['Area']) 

area=np.array(area)
area=area.tolist()
area0=[]
for i in area:
    for j in i:
        area0.append(j)

#单体
n={'Area≤25':0,'25<Area≤50':0,'50<Area≤100':0,'100<Area≤150':0,'150<Area≤200':0,'200<Area≤250':0,'250<Area≤300':0,
    '300<Area≤350':0,'350<Area≤400':0,'400<Area≤450':0,'Area>450':0}
for k in area0:
    if 1<k<=25:
        n['Area≤25']+=1
    if k>25 and k<=50:
        n['25<Area≤50']+=1 
    if k>50 and k<=100:
        n['50<Area≤100']+=1    
    if k>100 and k<=150:
        n['100<Area≤150']+=1
    if k>150 and k<=200:
        n['150<Area≤200']+=1
    if k>200 and k<=250:
        n['200<Area≤250']+=1
    if k>250 and k<=300:
        n['250<Area≤300']+=1
    if k>300 and k<=350:
        n['300<Area≤350']+=1
    if k>350 and k<=400:
        n['350<Area≤400']+=1
    if k>400 and k<=450:
        n['400<Area≤450']+=1
    if k>450:
        n['Area>450']+=1

#多聚体
# n={'Area≤100':0,'100<Area≤200':0,'200<Area≤300':0,'300<Area≤400':0,'400<Area≤500':0,'500<Area≤600':0, 'Area>600':0}
# for k in area0:
#     if k<=100:
#         n['Area≤100']+=1
#     if k>100 and k<=200:
#         n['100<Area≤200']+=1
#     if k>200 and k<=300:
#         n['200<Area≤300']+=1
#     if k>300 and k<=400:
#         n['300<Area≤400']+=1
#     if k>400 and k<=500:
#         n['400<Area≤500']+=1
#     if k>500 and k<=600:
#         n['500<Area≤600']+=1
#     if k>600:
#         n['Area>600']+=1

keys=[]
values=[]
for k,v in n.items():
    keys.append(k)
    values.append(v/len(area0))

#plt.figure(figsize=(7,7))
plt.rcParams['font.sans-serif'] = ['SimHei']  #显示汉字
plt.rcParams["axes.unicode_minus"] = False

x = [1,2,3,4,5,6,7,8,9,10,11]  #单体
# x = [1,2,3,4,5,6,7]  #多聚体
plt.bar(x, values, color=['#FA8600'], edgecolor='black', linewidth=1)

plt.xlabel('Area', fontsize=22)
plt.ylabel('Proportion', fontsize=22)
plt.xticks(x, keys, rotation=-30, ha="left", fontsize=10, size=16)   #修改x轴坐标，标签方向
plt.yticks(size=17)

outpath = r'D:\document\image\two_color\composite\2/'
plt.savefig(outpath+'R1单体面积比例柱状图.png',dpi=256,bbox_inches='tight')  #单体
# plt.savefig(outpath+'R3多聚体面积比例柱状图.png',dpi=256,bbox_inches='tight')  #多聚体
plt.show()


