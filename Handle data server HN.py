#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json    
from glob import glob


# In[2]:

print("Merge json file.......")
files=glob('*.json')
Json_new=open("Data_all_HN.json", "w",encoding='utf-8')
for file in files:
    with open(file) as f:
        for line in f:
            Json_new.write(line)
Json_new.close()


# In[ ]:

print("Convert to dataframe.......")

data = []
with open('Data_all_HN.json') as f:
    for line in f:
        data.append(json.loads(line))


# In[ ]:


df = pd.DataFrame(data)


# In[ ]:
print("Handling data.......")

data_handle=df.copy()
data_handle['Loại khách hàng']=''
data_handle['Số điện thoại']=''
data_handle['Quận']=''
data_handle['Loại mặt hàng']=''
for i in range(data_handle.shape[0]):
    print("Handle data ",i,".")
    try:
        data_handle['SĐT'][i]= str(data_handle['SĐT'][i]).replace("0","'0",1)
        copy=data_handle['Thời gian đăng'][i]
        data_handle['Thời gian đăng'][i]=copy.split('đăng')[1]
        data_handle['Loại khách hàng'][i]=copy.split('đăng')[0].split('Tin')[1]
        data_handle['Quận'][i]=data_handle['Url'][i].split('/')[3]
        data_handle['Loại mặt hàng'][i]=data_handle['Url'][i].split('/')[4]
    except:
        pass


# In[ ]:


sequence = ['Stt','Id','Tên người dùng','SĐT','Địa chỉ','Khu vực','Quận','Mặt hàng','Loại mặt hàng','Giá','Loại tin','Thời gian đăng','Loại khách hàng','Mô tả','Url']
data_handle = data_handle.reindex(columns=sequence)


# In[ ]:

print("Write to json file.......")

file=open("Data_HN_Handle.json", "w",encoding='utf-8')
for i in range(data_handle.shape[0]):
    line = json.dumps(dict(data_handle.loc[i]), ensure_ascii=False)+"\n"
    file.write(line)
file.close()


# In[ ]:

print("Write to csv file.......")

data_handle.to_csv("Data_HN_Handle.csv",encoding='utf-8')

