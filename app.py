import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import PowerTransformer
import pickle

file1 = open('n2opredictor.pkl', 'rb')
gb = pickle.load(file1)
file1.close()

pt = PowerTransformer()

data = pd.read_csv("traineddata.csv")

#------------------------------------------------------------


st.title("N2O Predictor")

experiment = st.selectbox('Experiment Type', data['Experiment'].unique())

datause = st.selectbox('DataUse', data['DataUse'].unique())

replication = st.selectbox('Type Of Replication', data['Replication'].unique())

month = st.selectbox('Month', data['Month'].unique())

vegetation = st.selectbox('Type Of Vegetation',data['Vegetation'].unique())

year = st.selectbox('Year',[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,202,2023,2024,2025,2026,2027])

n_rate = st.number_input('N_rate')

pp_2 = st.number_input('PP2')

pp_7 = st.number_input('PP7')

airt = st.number_input('AIRT')

daftd = st.number_input('DAF_TD')

dafsd = st.number_input('DAF_SD')

wfp = st.number_input('WFPS25cm')

nh4 = st.number_input('NH$ Content')

no3 = st.number_input('NO3 Content')

clay = st.number_input('Clay Content')

sand = st.number_input('Sand Content')

som = st.number_input('SOM')


#------------------------------------------------------------------------------------------------------------

if st.button('Predict NO2 Flux'):

    
    if experiment == 'BCSE_KBS':
        experiment = 1
    elif experiment == 'MCSE-T2' :
        experiment = 2
    else:
        experiment = 3

    if datause == 'Building':
        datause = 1
    else:
        datause = 2

    if replication == 'R1':
        replication = 1
    elif replication == 'R2':
        replication = 2
    elif replication == 'R3':
        replication = 3
    elif replication == 'R4':
        replication = 4
    else:
        replication = 5

    if month == 'January':
        month = 1
    elif month == 'February':
        month = 2
    elif month == 'March':
        month = 3
    elif month == 'April':
        month = 4
    elif month == 'May':
        month = 5
    elif month == 'June':
        month = 6
    elif month == 'July':
        month = 7
    elif month == 'August':
        month = 8
    elif month == 'September':
        month = 9
    elif month == 'October':
        month = 10
    elif month == 'November':
        month = 11
    else:
        month = 12

    if vegetation == 'Corn':
        vegetation = 1
    elif vegetation == 'GLYMX':
        vegetation = 2
    else:
        vegetation = 3

    
    l1 = [ experiment, datause, replication, mnth, vegetation, year]
    arr1 = [[n_rate], [pp_2], [pp_7], [airt], [daftd], [dafsd], [wfp], [nh4], [no3], [clay], [sand], [som] ]

    arr2 = pt.fit_transform(arr1)
    l2 = []

    for i in range(len(arr2)):
        l2.append(float(arr2[i]))

    l1.extend(l2)

    

    query = np.array(l1)

    query = query.reshape(1, 18)

    prediction = gb.predict(query)[0]

    st.title("Predicted NO2 Flux is " +
             str(prediction))
