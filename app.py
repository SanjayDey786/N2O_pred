import streamlit as st
import pandas as pd
import numpy as np
import pickle
import xgboost 
import sklearn

file1 = open('n2opredictor_new1.pkl', 'rb')
xgb = pickle.load(file1)
file1.close()


data = pd.read_csv("new_trained_data.csv")
data = data.iloc[:,1:]
#------------------------------------------------------------


st.title("N2O Predictor")


month = st.selectbox('Month', ['January','February','March','April','May','June','July','August','September','October','November','December'])


year = st.selectbox('Year',[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,202,2023,2024,2025,2026,2027])


pp_2 = st.number_input('PP2')

pp_7 = st.number_input('PP7')

airt = st.number_input('AIRT')

daftd = st.number_input('DAF_TD')

dafsd = st.number_input('DAF_SD')

wfp = st.number_input('WFPS25cm')

nh4 = st.number_input('NH4 Content')

no3 = st.number_input('NO3 Content')


#------------------------------------------------------------------------------------------------------------

if st.button('Predict NO2 Flux'):

    
    

    months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

    mnth = months[month]

    

    query = np.array([[airt, pp_2, nh4, pp_7, wfp, year, no3, daftd, dafsd,mnth]])
    

    prediction = xgb.predict(query)

    st.title("Predicted NO2 Flux is " +
             str(prediction))
