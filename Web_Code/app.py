# import streamlit as st
# import pickle
# import numpy as np

# # import the model
# pipe = pickle.load(open('pipe.pkl','rb'))
# df = pickle.load(open('df.pkl','rb'))

# st.title("Laptop Predictor")

# # brand
# company = st.selectbox('Brand',df['Company'].unique())

# # type of laptop
# type = st.selectbox('Type',df['TypeName'].unique())

# # Ram
# ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# # weight
# weight = st.number_input('Weight of the Laptop')

# # Touchscreen
# touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# # IPS
# ips = st.selectbox('IPS',['No','Yes'])

# # screen size
# screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)

# # resolution
# resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# #cpu
# cpu = st.selectbox('CPU',df['Cpu brand'].unique())

# hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

# gpu = st.selectbox('GPU',df['Gpu brand'].unique())

# os = st.selectbox('OS',df['os'].unique())

# if st.button('Predict Price'):
#     # query
#     ppi = None
#     if touchscreen == 'Yes':
#         touchscreen = 1
#     else:
#         touchscreen = 0

#     if ips == 'Yes':
#         ips = 1
#     else:
#         ips = 0

#     X_res = int(resolution.split('x')[0])
#     Y_res = int(resolution.split('x')[1])
#     ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
#     query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

#     query = query.reshape(1,12)
#     st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from pathlib import Path

# Load model and dataframe  
# pipe = pickle.load(open('pipe.pkl', 'rb'))
# df = pickle.load(open('df.pkl', 'rb'))

BASE_DIR = Path(__file__).parent

pipe = pickle.load(open(BASE_DIR / "pipe.pkl", "rb"))
df = pickle.load(open(BASE_DIR / "df.pkl", "rb"))


# Set page configuration
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="auto"
)

# Title
st.title("Laptop Price Predictor")

# Brand
company = st.selectbox(
    'Brand',
    df['Company'].unique()
)

# Laptop Type
type_name = st.selectbox(
    'Type',
    df['TypeName'].unique()
)

# RAM
ram = st.selectbox(
    'RAM (in GB)',
    [2, 4, 6, 8, 12, 16, 24, 32, 64]
)

# Weight
weight = st.number_input(
    'Weight of Laptop'
)

# Touchscreen
touchscreen = st.selectbox(
    'Touchscreen',
    ['No', 'Yes']
)

# IPS Panel
ips = st.selectbox(
    'IPS Panel',
    ['No', 'Yes']
)

# Screen Size
screen_size = st.slider(
    'Screen Size (in inches)',
    10.0,
    18.0,
    13.0
)

# Resolution
resolution = st.selectbox(
    'Screen Resolution',
    [
        '1920x1080',
        '1366x768',
        '1600x900',
        '3840x2160',
        '3200x1800',
        '2880x1800',
        '2560x1600',
        '2560x1440',
        '2304x1440'
    ]
)

# CPU
cpu = st.selectbox(
    'CPU',
    df['Cpu brand'].unique()
)

# HDD
hdd = st.selectbox(
    'HDD (in GB)',
    [0, 128, 256, 512, 1024, 2048]
)

# SSD
ssd = st.selectbox(
    'SSD (in GB)',
    [0, 8, 128, 256, 512, 1024]
)

# GPU
gpu = st.selectbox(
    'GPU',
    df['Gpu brand'].unique()
)

# Operating System
os = st.selectbox(
    'Operating System',
    df['os'].unique()
)

# Predict Button
if st.button('Predict Price'):

    # Convert categorical values
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Extract resolution
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    # Calculate PPI
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    # Create dataframe for prediction
    query = pd.DataFrame({
        'Company': [company],
        'TypeName': [type_name],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'IPS Panel': [ips],
        'PPI': [ppi],
        'Cpu brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu brand': [gpu],
        'os': [os]
    })

    # Prediction
    prediction = pipe.predict(query)[0]

    # Final Price
    price = int(np.exp(prediction))

    # Display result
    st.success(f"Predicted Laptop Price: ₹ {price}")