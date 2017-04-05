
# coding: utf-8

# In[11]:

#Importing all the required libraries
import pandas as pd
import numpy as np
import csv
import datetime as dt
from io import StringIO


# In[12]:

#Converting csv into dataframe
df1=pd.read_csv('cricket_matches.csv')


# In[13]:

#Creating new dataframe
df3 = df1[['home', 'winner','innings1','innings1_runs', 'innings2', 'innings2_runs']]


# In[14]:

#Comparing the values
df4 = df3[df3['home']== df3['winner']]


# In[15]:

#Comparing the values
df5= df4[df4['winner'] == df4['innings2']]


# In[16]:

#Comparing the values
df6= df4[df4['winner'] == df4['innings1']]


# In[17]:

df5.shape


# In[18]:

df6.head()


# In[19]:

#Coying values into new column
df6['Score'] = df6['innings1_runs']


# In[20]:

frames =  [df5, df6]


# In[21]:

#Concating the dataframes 
df7 = pd.concat([df5,df6])


# In[22]:

df8 = df7[['home', 'Score']]


# In[23]:

#Calculating the mean
df9 = df8.groupby(['home'], as_index= False).mean()


# In[24]:

df9.to_csv('cricket_matches_new.csv')


# In[25]:

print(df9.head())

