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

3. The first analysis shows the records of all the crimes on daily basis.

4. It represents all the crimes that occur on each day.

5. CSV Files and plots are generated for top ten cities.

As per the results of graphs, two major analysis can be drawn:

1. The crimes are found to be occured in maximum number on Fridays (Mostly weekends are the target)

2. The other conclusion that can be withdrawn is that most of the crimes occured in the boston city were unarmed or without weapons. 

![](Images/csv_ana1.PNG?raw=true)

![](Images/Ana1.1.PNG?raw=true)
The first graph shows the crimes occured on daily basis in overall Boston city.


![](Images/Ana1.2.PNG?raw=true)
The second graph shows in what all incidents involved the use of various weapons.



### Question 2

Which are the crimes occured in Boston city with their high to low frequency rates from year 2012-2015?


**Analysis 2**
1. Used relative path to access the csv file that is present in the data folder.

2. Extracted the data from the csv file using 'pd.read_csv command'. This command gives me the data in form of dataframe.

3. Used the COMPNOS(column1) factor to find the frequencies of all the types of crime present in (INCIDENT_TYPE_DESCRIPTiON) column.


![](Images/csv_ana2.PNG?raw=true)

The above csv shows the crime type and corresponding values.

![](Images/Ana2.PNG?raw=true)
The above graph plotted  show the frequency rate of all the crimes occured in city of Boston (Year 2012- 2015) 


### Question 3

How are the statistics of crimes occuring in Boston City for various months?

**Analysis 3**

1. Used relative path to access the csv file that is present in the data folder.

2. Extracted the data from the csv file using 'pd.read_csv command'. This command gives me the data in form of dataframe.

3. As the month for every year was not separately give, we have to do some pre process on the dates mentioned in the "FROMDATE"
column.

4. In the csv, considered the monthly data of the four different kind of crime incidents.

The graph below shows the monthly evaluation of the crime incidents occured over the four years.

![](Images/Ana3.PNG?raw=true)


### Question 4

What is the per hour crime rate in the city of Boston?

**Analysis 4**

1. Used relative path to access the csv file that is present in the data folder.

2. Extracted the data from the csv file using 'pd.read_csv command'. This command gives me the data in form of dataframe.

3. Further, I need to find the hours of day. So I did some prepocessing and extracted all the hours from the give time when the incidents took place from the "FROMDATE" column.

4. In the csv, considered the hourly data of the for all the crime incidents.

The graph below shows the monthly evaluation of the crime incidents occured over the four years.

![](Images/Ana4.PNG?raw=true)



### Question 5

What is the per hour crime rate in the city of Boston?

**Analysis 5**

1. Used relative path to access the csv file that is present in the data folder.

2. Extracted the data from the csv file using 'pd.read_csv command'. This command gives me the data in form of dataframe.

3. I processed the month from the "FROMDATE" column. also I used the year from the same column. 

4. In the csv, considered the combine data for month and year and the respective crime incidents.

The graph below shows the monthly evaluation of the crime incidents occured over the four years.

![](Images/Ana5.PNG?raw=true)

