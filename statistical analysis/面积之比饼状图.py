import csv
import pandas as pd
import numpy as np
import math  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt
from scipy.stats import norm

filename=r"D:\document\image\two_color\composite\2/WT-L-2#-5-_Area_ratio.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)   #表格最上面每一列的名字
    #print(header_row)
    #结果为['Label ', 'Area', 'Feret', 'FeretX', 'FeretY', 'FeretAngle', 'MinFeret']
    AR=pd.read_csv(filename, usecols=['Area1/Area2'])   #读取特定的列,dataframe格式


AR=np.array(AR)
AR=AR.tolist()

AR.sort()
ar=[]
for i in AR:
    for j in i:
        ar.append(j)

n={'AR≤0.25':0,'0.25<AR≤0.5':0,'0.5<AR≤1':0,'1<AR≤2':0,'AR>2':0}
for k in ar:
    if k<=0.25:
        n['AR≤0.25']+=1
    if k>0.25 and k<=0.5:
        n['0.25<AR≤0.5']+=1
    if k>0.5 and k<=1:
        n['0.5<AR≤1']+=1
    if k>1 and k<=2:
        n['1<AR≤2']+=1
    if k>2:
        n['AR>2']+=1
keys=[]
values=[]
for k,v in n.items():
    keys.append(k)
    values.append(v)

plt.figure(figsize=(7,7))#将画布设定为正方形，则绘制的饼图是正圆
label=keys#定义饼图的标签，标签是列表
explode=[]
for e in range(len(keys)):
    explode.append(0.01)
#设定各项距离圆心n个半径

values=values
plt.pie(values,explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图
#plt.title('Protein area distribution')#绘制标题
plt.savefig('面积之比饼状图.png',dpi=256,bbox_inches='tight')
plt.show()