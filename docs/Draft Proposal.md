## About the project

## Goal
My initial thoughts about the project is to predict taxi fares in DC city which would be helpful for the user to plan his/her trip. <br>

## About Data

Total files: 12 (each file represents each month of 2022) <br>
Size : 25 - 65 MB <br>
Rows: 3 M (All files together) <br>
Columns: 28 <br>
Source: OpenData.DC.gov <br>
https://opendata.dc.gov/documents/2b61c28adfbd431587ec728829cceb6e/explore


## Data Columns

1.  COLUMN_NAME		DATA_TYPE		                DESCRIPTION <br>
2.  OBJECTID			NUMBER(9)		             Table Unique Identifier	<br>
3.  TRIPTYPE			VARCHAR2(255)	           Type of Taxi Trip <br>
4.  PROVIDERNAME		VARCHAR2(255)	         Taxi Company that Provided 								
5.  FAREAMOUNT			VARCHAR2(255)	         Meter Fare Amount <br>
6.  GRATUITYAMOUNT		VARCHAR2(255)	       Tip amount <br>
7.  SURCHARGEAMOUNT		VARCHAR2(255)	       Surcharge fee <br>
8.  EXTRAFAREAMOUNT		VARCHAR2(255)	       Extra fees <br>
9.  TOLLAMOUNT			VARCHAR2(255)	         Toll amount <br>
10. TOTALAMOUNT		VARCHAR2(255)	           Total amount from Meter 								
11. PAYMENTTYPE		VARCHAR2(255)	           Payment type <br>
12. ORIGINCITY			VARCHAR2(255)        	 Pick up location city <br>
13. ORIGINSTATE		VARCHAR2(255)	           Pick up location state <br>
14. ORIGINZIP			VARCHAR2(255)	           Pick up location zip <br>
15. DESTINATIONCITY		VARCHAR2(255)	       Drop off location city <br>
16. DESTINATIONSTATE		VARCHAR2(255).    Drop off location state <br>
17. DESTINATIONZIP		VARCHAR2(255)	       Drop off location zip <br>
18. MILEAGE			VARCHAR2(255)	             Trip milaege <br>
19. DURATION			VARCHAR2(255)	           Trip time - duration of 								
20. ORIGIN_BLOCK_LATITUDE	NUMBER		       Pick up location latitude <br>
21. ORIGIN_BLOCK_LONGITUDE/NUMBER		       Pick up location longitude <br>
22. RIGIN_BLOCKNAME		VARCHAR2(255)	       Pick up location street 								
23. DESTINATION_BLOCK_LAT	NUMBER		       Drop off location latitude <br>
24. DESTINATION_BLOCK_LONGNUMBER		       Drop off location longitude <br>
25. DESTINATION_BLOCKNAME	VARCHAR2(255)	   Drop off location street 							
26. AIRPORT			CHAR(1)		                 Pick up or drop off 									
27. ORIGINDATETIME_TR	DATE			           Pick up date and time	 <br>
28. DESTINATIONDATETIME_TRDATE			       Drop off date and time	 <br>

## Additional Information
Payment Type <br>
1.	Credit <br>
2.	Cash <br>

## Feature Selection
My X variables would be FAREAMOUNT, GRATUITYAMOUNT, SURCHARGEAMOUNT, EXTRAFAREAMOUNT, TOLLAMOUNT, PAYMENTTYPE, MILEAGE, DURATION, ORIGIN_BLOCK_LATITUDE	NUMBER, ORIGIN_BLOCK_LongNUMBER	NUMBER,DESTINATION_BLOCK_LAT	NUMBER,DESTINATION_BLOCK_LONGNUMBER, DESTINATIONDATETIME_TRDATE

My Y variable would be TOTALAMOUNT

## Model
I would like to apply couple of machine learning algorithms like Linear regression, XBoost, RandomForest on the data and compare their performances using Mean Absolute Error. Finally pick the best performing algorithm. <br>

## Front End
I would like to implement a webpage where it takes information like source and destination from the customer then provides the estimated fare for the trip. <br>

## Cloud Storage
I would like store my data in the S3 bucket of AWS and acces it in my python program. <br>

## Flask
Flask is a web framework, it’s a Python module that lets you develop web applications easily. <br>
It helps to integrate a web page(html code) to the model(python code) and allows a two way communication in this project.

