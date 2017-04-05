
# coding: utf-8

# In[8]:

#Importing all the required libraries
import pandas as pd
import numpy as np
import csv
import datetime as dt
from io import StringIO


# In[9]:

#Converting csv into dataframe
df1=pd.read_csv('vehicle_collisions.csv', parse_dates=[1])


# In[10]:

#Creating new dataframe
df2 = df1[['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE','VEHICLE 5 TYPE']]


# In[11]:

#Filling zero's for NaN values
df2 = df2.fillna(value= 0)


# In[12]:

#Check for column value not equal to zero
df3 = df2[(df2['BOROUGH'] != 0)]


# In[13]:

#Replacing the values
df3['VEHICLE 1 TYPE'] = df3['VEHICLE 1 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df3['VEHICLE 2 TYPE'] = df3['VEHICLE 2 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df3['VEHICLE 3 TYPE'] = df3['VEHICLE 3 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df3['VEHICLE 4 TYPE'] = df3['VEHICLE 4 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')
df3['VEHICLE 5 TYPE'] = df3['VEHICLE 5 TYPE'].str.replace(r'[a-zA-Z0-9/ ()-]+', '1')


# In[15]:

df3 = df3.fillna(value= 0)  #Fill zero's


# In[16]:

#Datatype change
df3['VEHICLE 1 TYPE']=df3['VEHICLE 1 TYPE'].astype(str).astype(int)
df3['VEHICLE 2 TYPE']=df3['VEHICLE 2 TYPE'].astype(str).astype(int)
df3['VEHICLE 3 TYPE']=df3['VEHICLE 3 TYPE'].astype(str).astype(int)
df3['VEHICLE 4 TYPE']=df3['VEHICLE 4 TYPE'].astype(str).astype(int)
df3['VEHICLE 5 TYPE']=df3['VEHICLE 5 TYPE'].astype(str).astype(int)


# In[17]:

#Sum of vehicle count
df4= df3.groupby(['BOROUGH'], as_index=False).sum()


# In[20]:

#Calculating the respective values 
df4['ONE_VEHICLE_INVOLVED'] = df4['VEHICLE 1 TYPE'] - df4['VEHICLE 2 TYPE']
df4['TWO_VEHICLES_INVOLVED'] = df4['VEHICLE 2 TYPE'] - df4['VEHICLE 3 TYPE']
df4['THREE_VEHICLES_INVOLVED'] = df4['VEHICLE 3 TYPE'] - df4['VEHICLE 4 TYPE']
df4['MORE_VEHICLES_INVOLVED'] = df4['VEHICLE 4 TYPE']


# In[19]:

#Print the output
print(df4.head())


# In[60]:

#Storing in csv
df4.to_csv('vehicle_collisions_new1.csv')

