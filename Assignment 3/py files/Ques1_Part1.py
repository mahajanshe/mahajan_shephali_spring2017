
# coding: utf-8

# In[3]:

#Importing all the required libraries
import pandas as pd
import numpy as np
import csv
import datetime as dt
from io import StringIO


# In[4]:

#Converting csv into dataframe
df1=pd.read_csv('vehicle_collisions.csv', parse_dates=[1])


# In[5]:

#Separating values of year and month from the date format
# df['DATE'] = pd.to_datetime(df['date'])
df1['year'], df1['month'] = df1['DATE'].dt.year, df1['DATE'].dt.month 


# In[6]:

#Creating new dataframe
df2 = df1[['DATE', 'BOROUGH', 'year', 'month']]


# In[7]:

#Filtering data for 2016 year and Manhattan city
df_filtered = df2[(df2['year'] == 2016) & (df2['BOROUGH'] == 'MANHATTAN')]


# In[8]:

#Creating new dataframe
df3 = df_filtered[['BOROUGH', 'year', 'month']]


# In[9]:

#Checking the length of dataframe
length_manhattan = len(df_filtered.index)
length_manhattan


# In[10]:

#Grouping by the data w.r.t month
group_by_month = df3.groupby(['month']).size().reset_index(name= "MANHATTAN")


# In[11]:

#Creating dataframe for year 2016
df_filtered_ny = df2[df2['year'] == 2016]


# In[12]:

#Checking the length of data frame
length_ny = len(df_filtered_ny.index)
length_ny


# In[13]:

#Grouping by month to find data for New York
group_by_month_ny = df_filtered_ny.groupby(['month']).size().reset_index(name= "NYC")


# In[14]:

#Merging the two dataframes (for Manhattan and New York) over month column
df4= pd.DataFrame.merge(group_by_month, group_by_month_ny, on='month', how='outer')


# In[15]:

#Renaming the months using if else statements
def month(c):
    if c[0] == 1:
        return 'Jan'
    elif c[1] == 2:
        return 'Feb'
    elif c[2] == 3:
        return 'Mar'
    elif c[3] == 4:
        return 'Apr'
    elif c[4] == 5:
        return 'May'
    elif c[5] == 6:
        return 'Jun'
    elif c[6] == 7:
        return 'Jul'
    elif c[7] == 8:
        return 'Aug'
    elif c[8] == 9:
        return 'Sep'
    elif c[9] == 10:
        return 'Oct'
    elif c[10] == 11:
        return 'Nov'
    elif c[11] == 12:
        return 'Dec'
df5 = pd.DataFrame(data={'month':[1,2,3,4,5,6,7,8,9,10,11,12], 'MONTH': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']})
# df5['MANHATTAN'] = df5.apply(MANHATTAN, axis=1)


# In[16]:

#Merging the final dataframe
df6= pd.DataFrame.merge(df5, df4, on='month', how='outer')


# In[17]:

# Selecting the required columns
df7 = df6[['MONTH', 'MANHATTAN', 'NYC']]


# In[18]:

#Calculating and storing the percentage for Manhattan w.r.t New York for all months in 2016
df7["PERCENTAGE"] = df7['MANHATTAN']/df7['NYC']


# In[19]:

df7.to_csv('vehicle_collision_new.csv')


# In[20]:

#Finally displaying few rows of the dataframe
print(df7.head())

