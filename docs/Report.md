#  UMBC Capstone Project 
## Taxi fare prediction using interactive web page

## Background Information:
Utilizing taxi services in our day to day life became routine, but do you ever wonder why fare prices fluctuates even you travel in a 
regular route every time. The reason behind it is simple, the fare is dependent on various factors. Finding and utilizing those factors to 
build a similar system all about my project.

A fare is the cost that a person pays to use a public transportation system, such as a train, bus, or cab. The system in place to decide 
how much each individual passenger utilizing a transit vehicle at any particular moment is required to pay is known as the fare structure.
The total fare depends upon various attributes like distance, day of week, hour, duration etc. 

## Problem Statement:
Giving user an interactive page to provide source and destination information. Predicting the appropriate fare for the ride using 
machine learning model and reverting back to the user with fare display in USD.

## Work Flow:

                         
<img width="953" alt="Snip_TEMP0001" src="https://github.com/Naveen-Neeli/Naveen_Neeli-Data606/assets/91988644/dceb9f28-5d28-4fa7-b644-ed6faedc68e6">

The above diagram depicts the complete flow of this project.
## About Data:

Total files: 12 (each file represents each month of 2022)
Size : 25 - 65 MB
Rows: 3 M (All files together)
Columns: 28
Source: OpenData.DC.gov
https://opendata.dc.gov/documents/2b61c28adfbd431587ec728829cceb6e/explore

Data Columns:

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
16. DESTINATIONSTATE		VARCHAR2(255).     Drop off location state <br>
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

## Data Preprocessing:
Handled missing values using various techniques like replacing by average value of column<br>
Casting data type<br>
Created new features with existing features<br>
Identified and removed outliers using visualization techniques

## Outliers Visualization using scatterplot:

![image](https://github.com/Naveen-Neeli/Naveen_Neeli-Data606/assets/91988644/4812fc6e-9bfe-458e-aa84-e189253eadea)

![image](https://github.com/Naveen-Neeli/Naveen_Neeli-Data606/assets/91988644/dbbd07c2-faf5-47fc-b80f-f3aebeacde04)

![image](https://github.com/Naveen-Neeli/Naveen_Neeli-Data606/assets/91988644/3dd6a192-3931-4439-8cbd-4ec6bf95a310)

![image](https://github.com/Naveen-Neeli/Naveen_Neeli-Data606/assets/91988644/5c81ff8a-f786-455a-a2fc-9d45e67415a1)

The above are few visualizations drawn between different independent features which clearly shows the outliers lied in them. Removing those outliers increased the model accuracy.

## Machine learning model:
XGBoost:

XGBoost regressor, short for Extreme Gradient Boosting, is a highly effective machine learning algorithm widely used for regression tasks. It combines the gradient boosting framework with decision trees as base models. By sequentially adding trees that correct the errors made by previous trees, XGBoost improves prediction accuracy. It incorporates regularization techniques to prevent overfitting and provides insights into feature importance. Moreover, XGBoost is known for its speed and scalability, making it suitable for handling large datasets. With its flexibility, interpretability, and strong performance, XGBoost regressor has become a popular choice among data scientists for regression problems.

After training the model with preprocessed data, acquired an accuracy of 0.81. After training, the model is saved using pickle file for streamlit deployment.

## Google Platform API:
Google Cloud Platform (GCP) API refers to a collection of application programming interfaces (APIs) provided by Google that allow developers to access and utilize various services and functionalities offered by the Google Cloud Platform. These APIs enable developers to interact with GCP resources, including storage, computing power, machine learning capabilities, and more, programmatically.

In this project google platform direction's API's is used for finding the real time distance and duration for the user given source and destination

## Deploying the Model using Streamlit library:

Streamlit is an open-source Python library used for creating interactive web applications and data dashboards with minimal effort. It simplifies the process of building and deploying web interfaces for machine learning models, data visualizations, and other data-driven applications. With Streamlit, developers can quickly prototype and share their projects without having to write extensive HTML, CSS, or JavaScript code.

Streamlit provides a straightforward and intuitive API that allows users to create interactive elements such as sliders, checkboxes, buttons, and text inputs. It supports real-time updates, making it easy to build responsive and dynamic applications that update instantly as users interact with the interface. Additionally, Streamlit supports integration with popular data science libraries like Pandas, Matplotlib, and TensorFlow, enabling seamless integration of data processing and visualization into the web application.

Overall, Streamlit empowers data scientists and developers to create interactive web applications with ease, enabling them to share their work and insights effectively. Its simplicity and integration capabilities make it a popular choice for quickly building and deploying data-driven applications.


<img width="953" alt="Snip_TEMP0001" src="https://github.com/Naveen-Neeli/Naveen_Neeli-Data606/assets/91988644/3e221121-323d-4ca7-a01f-9984b769a553">

The above image is exactly how front end page looks like. Here the source and destination will be given by the user. When the user clicks predict button, total fare for the given travel information will be displayed to the user.

## Conclusion:
After detailed analysis and observation, few features were identified as the very impact features where the total amount depending on. They are "Distance", "Duration", "Day of Week" and "Hour". So these are the features to be considered when booking a taxi service to minimize the travel expenses.
























