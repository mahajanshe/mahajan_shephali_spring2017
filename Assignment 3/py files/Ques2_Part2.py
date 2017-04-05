
# coding: utf-8

# In[2]:

#Importing all the required libraries
import pandas as pd
import numpy as np
import csv
import datetime as dt
from io import StringIO


# In[3]:

#Converting csv into dataframe
df1=pd.read_csv('employee_compensation.csv')


# In[4]:

#Creating new dataframe
df2 = df1[['Year Type', 'Job Family', 'Employee Identifier', 'Salaries', 'Overtime', 'Total Salary', 'Total Benefits', 'Total Compensation']]


# In[5]:

#Comparing the values
df3 = df2[df2['Year Type'] == 'Calendar']


# In[6]:

#Calculating the average value
df4 = df3.groupby(['Job Family', 'Employee Identifier'], as_index= False).mean()


# In[7]:

#Checking the condition to satisfy
df5 = df4[df4['Overtime']> 0.05* df4['Salaries']]


# In[8]:

#Creating new dataframe
df6 = df5[['Job Family', 'Total Benefits', 'Total Compensation']]


# In[9]:

#Finding average
df7 = df6.groupby(['Job Family'], as_index= False).mean()


# In[10]:

print(df7.head())


# In[11]:

#Calculate the percentage
df7["Percent_Total_Benefit"] = 100* df7['Total Benefits']/df7['Total Compensation']


# In[12]:

#Sorting values
df8= df7.sort_values(['Percent_Total_Benefit'], ascending = [False])


# In[18]:

print(df8.head())


# In[15]:

df8.to_csv('employee_compensation_new1.csv')

