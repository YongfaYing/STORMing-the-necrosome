import csv
import pandas as pd
import numpy as np
import math  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt
from scipy.stats import norm  

  
filename="Area.csv"
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
        area0.append(i)

#area0.sort() #排序

x=list(range(1,len(area0)+1))
y=area0
plt.scatter(x,y,s=1)
plt.ylabel('Area')  
plt.xlabel('Label')  
plt.title(r'Protein area distribution')
plt.show()