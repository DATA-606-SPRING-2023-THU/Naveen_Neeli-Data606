#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:45:43 2023

@author: naveenneeli
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st
import xgboost as xgb
import streamlit as st
from datetime import date
from PIL import Image
from random import randint
from datetime import datetime
import requests
import googlemaps


pickle_in = open("model_xb.pkl","rb")
mymodel = pickle.load(pickle_in)

#Predting the fare using saved model
def predict_taxi_fare(temp):
    prediction = mymodel.predict(temp)
    print(prediction)
    return prediction


# Findind realtime distance using google maps API
    
def gmaps(source,destination):
    
    #source = '4712 gateway terrace arbutus maryland 21227'
    #destination = '31 Capitol St Salinas, California(CA), 93901'
    gmaps_client = googlemaps.Client(key= 'AIzaSyBOvqGRvL7yfDmN7XJRtGW0LM7VxAtZ1n0')
    now = datetime.now()
        
    direction_result = gmaps_client.directions(source,destination, mode = 'driving', departure_time = now,transit_mode = 'car')
    
    dis = direction_result[0]['legs'][0]['distance']
    dur = direction_result[0]['legs'][0]['duration']
        
    
    distance = dis['value']/1000
    duration = dur['value']
    
    return distance,duration 
   

# Program starts here    
    
def main():
    st.title("Taxi Booking System")
    html_temp = """<div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Book your Taxi</h2>
    </div>"""
    st.markdown(html_temp,unsafe_allow_html=True)
    
    #Taking input from user
    source = st.text_input("Source")
    destination = st.text_input("Destination")
    
    result=""
    if st.button("Predict"):
        
        gratuityamount = 2
        surchargeamount = 0
        extrafareamount = 1
        tollamount = 0
        
        
        #Taking today's day of week
        temp = datetime.today().weekday()
        dayofweek = temp
        
        #Taking current hour
        temph= datetime.now()
        hour = temph.hour
        milege = 30
        
        
        distance,duration = gmaps(source,destination)
        
        Fareamount = 3.25+(((duration/60)/2)*0.27)
    # storing the input feature as numpy array
        temp = np.array([[Fareamount,gratuityamount,surchargeamount,extrafareamount,tollamount,duration,dayofweek,hour,milege,distance]])
        
        result=predict_taxi_fare(temp)
        st.success('The ride charge would be  ${}'.format(result))
        
    if st.button("About"):
        st.text("This webpage is built by Naveen Neeli")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
