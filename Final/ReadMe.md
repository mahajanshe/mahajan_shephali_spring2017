# Data Analysis using Python - Final Project

## Boston City Crime Data Analysis

![](Images/Boston.jpeg?raw=true)


### Data Collection

The data for Boston city crime incidents is taken from the link provided below.

Link: https://data.cityofboston.gov/Public-Safety/Crime-Incident-Reports-July-2012-August-2015-Sourc/7cdf-6fgx   -CSV

Crime Incident Reports in this link are provided by Boston Police Department from July,2012 till August,2015 that is for four years.  

This csv file is stored as "Crime_Report_Boston" in the data folder.

### Question 1
Can it be found if on which day of the week most number of crimes take place in boston?

**Analysis 1**

Following steps were taken to perform analysis 1:

1. Used relative path to access the csv file that is present in the data folder.

2. Extracted the data from the csv file using 'pd.read_csv command'. This command gives me the data in form of dataframe.

3.The first analysis shows the records of all the crimes on daily basis
It represents all the crimes that occur on each day
As per the results of graphs, two major analysis can be drawn:
1. The crimes are found to be occured in maximum number on Fridays (Mostly weekends are the target)
2. The other conclusion that can be withdrawn is that most of the crimes occured in the boston city were unarmed or without weapons. 

![](Images/csv_ana1.PNG?raw=true)

![](Images/Ana1.1.PNG?raw=true)

Which are the crimes occuring in Boston city with their high to low frequency rates?
#Analysis_2 show which are the crimes that occured in the boston city over the 3 years(2012- 2015)
#The bar graph plotted below show the frequency rate of all the crimes occured in city of boston
