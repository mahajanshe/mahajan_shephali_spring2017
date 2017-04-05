
# coding: utf-8

# In[1]:

#Importing all the required libraries
import pandas as pd
import numpy as np
import csv
import datetime as dt
from io import StringIO


# In[2]:

#Converting csv into dataframe
df1=pd.read_csv('employee_compensation.csv')


# In[3]:

##Creating new dataframe
df2 = df1[['Organization Group', 'Department', 'Total Compensation']]


# In[4]:

#Calculating average
df3 = df2.groupby(['Organization Group', 'Department'], as_index= False).mean()


# In[5]:

#Sorting the values in desc order
df4= df3.sort_values(['Total Compensation'], ascending = [False])


# In[6]:

# df4.to_csv('employee_compensation_new.csv', sep='\t', encoding='utf-8')
df4.to_csv('employee_compensation_new.csv')


# In[7]:

print(df4.head())

