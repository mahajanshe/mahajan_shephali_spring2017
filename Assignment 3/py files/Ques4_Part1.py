
# coding: utf-8

# In[1]:

#Importing all the required libraries
import pandas as pd
import numpy as np
import csv, re
import datetime as dt


# In[2]:

#Converting csv into dataframe
df1=pd.read_csv('movies_awards.csv')


# In[3]:

#Filling zero's for NaN values
df1 = df1.fillna(value= 0)


# In[4]:

#Taking the required column in a new dataframe
df2 = df1[['Awards']]


# In[5]:

#Eliminating zero value rows
df3= df2.loc[~(df2==0).all(axis=1)]


# In[6]:

#Renaming the column
col_name =df3.columns[0]
df3=df3.rename(columns = {col_name:'Awards'})


# In[7]:

# df3['Awards_won'] = df3['Awards'].str.findall('(\d+) win')
# # df3['Awards_nominated'] = df3['Awards'].str.findall('(\d+) nominations.')
# df3['Awards_nominated'] = df3['Awards'].str.findall('(\d+) nomination.')
# df3['Prime_Awards_nominated'] = df3['Awards'].str.findall('Nominated for (\d+) Primetime Emmy')
# df3['Oscar_Awards_nominated'] = df3['Awards'].str.findall('Nominated for (\d+) Oscar.')
# df3['Golden_Globe_Awards_nominated'] = df3['Awards'].str.findall('Nominated for (\d+) Golden')
# df3['BAFTA_Awards_nominated'] = df3['Awards'].str.findall('Nominated for (\d+) BAFTA Film')
# df3['Prime_Awards_won'] = df3['Awards'].str.findall('Won(\d+) Primetime Emmy')
# df3['Oscar_Awards_won'] = df3['Awards'].str.findall('Won (\d+) Oscar')
# df3['Golden_Globe_Awards_won'] = df3['Awards'].str.findall('Won (\d+) Golden Globe')
# df3['BAFTA_Awards_won'] = df3['Awards'].str.findall('Won (\d+) BAFTA')


# In[8]:

# Extracting values and creating columns respectively

df3['Awards_won'] = df3['Awards'].apply(lambda x: int (re.findall('(\d+) win', x)[0]) if len(re.findall('(\d+) win', x)) !=0 else 0 )+ df3['Awards'].apply(lambda x: int (re.findall('Won (\d+)', x)[0]) if len(re.findall('Won (\d+)', x)) !=0 else 0 )#df3['Awards'].str.findall('Won (\d+)')
df3['Awards_nominated'] = df3['Awards'].apply(lambda x: int (re.findall('(\d+) nomination', x)[0]) if len(re.findall('(\d+) nomination', x)) !=0 else 0 )+ df3['Awards'].apply(lambda x: int (re.findall('Nominated for (\d+)', x)[0]) if len(re.findall('Nominated for (\d+)', x)) !=0 else 0 )
df3['Prime_Awards_nominated'] = df3['Awards'].apply(lambda x: int (re.findall('Nominated for (\d+) Primetime Emmy', x)[0]) if len(re.findall('Nominated for (\d+) Primetime Emmy', x)) !=0 else 0 )
df3['Oscar_Awards_nominated'] = df3['Awards'].apply(lambda x: int (re.findall('Nominated for (\d+) Oscar', x)[0]) if len(re.findall('Nominated for (\d+) Oscar', x)) !=0 else 0 )
df3['Golden_Globe_Awards_nominated'] = df3['Awards'].apply(lambda x: int (re.findall('Nominated for (\d+) Golden', x)[0]) if len(re.findall('Nominated for (\d+) Golden', x)) !=0 else 0 )
df3['BAFTA_Awards_nominated'] = df3['Awards'].apply(lambda x: int (re.findall('Nominated for (\d+) BAFTA', x)[0]) if len(re.findall('Nominated for (\d+) BAFTA', x)) !=0 else 0 )
df3['Prime_Awards_won'] = df3['Awards'].apply(lambda x: int (re.findall('Won (\d+) Primetime', x)[0]) if len(re.findall('Won (\d+) Primetime', x)) !=0 else 0 )
df3['Oscar_Awards_won'] = df3['Awards'].apply(lambda x: int (re.findall('Won (\d+) Oscar', x)[0]) if len(re.findall('Won (\d+) Oscar', x)) !=0 else 0 )
df3['Golden_Globe_Awards_won'] = df3['Awards'].apply(lambda x: int (re.findall('Won (\d+) Golden Globe', x)[0]) if len(re.findall('Won (\d+) Golden Globe', x)) !=0 else 0 )
df3['BAFTA_Awards_won'] = df3['Awards'].apply(lambda x: int (re.findall('Won (\d+) BAFTA', x)[0]) if len(re.findall('Won (\d+) BAFTA', x)) !=0 else 0 )


# In[9]:

df3.to_csv('Q4_P1.csv')


# In[10]:

print(df3.head())


# In[ ]:



