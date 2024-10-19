import streamlit as st
import numpy as np
import joblib


st.title ('Early Diabetes Prediction')

X = joblib.load('XScaled1.pkl')
RForest = joblib.load('RForest1.pkl')

Age = st.number_input('Age')
Gender = st.number_input('Gender: 0(F) 1(M)')
Weakness = st.number_input('Weakness 0(No) & 1(Yes)')
Genital_Thrush = st.number_input('G-Thrush 0(No) & 1(Yes)')
Visual_Blurring = st.number_input('V-Blurring 0(No) & 1(Yes)')
Itching = st.number_input('Itching 0(No) & 1(Yes)')
Irritability = st.number_input('Irritability 0(No) & 1(Yes)')
Delayed_Healing = st.number_input('D-Healing 0(No) & 1(Yes)')
Obesity = st.number_input('Obesity 0(No) & 1(Yes)')
Excessive_Urine_Prod = st.number_input('Ex-Urine-Prod 0(No) & 1(Yes)')
Excessive_Thirst = st.number_input('Ex-Thirst 0(No) & 1(Yes)')
Sudden_Weight_Loss = st.number_input('SWt-Loss 0(No) & 1(Yes)')
Excessive_Hunger = st.number_input('Ex-Hunger 0(No) & 1(Yes)')
Muscle_Weakness = st.number_input('M-Weakness 0(No) & 1(Yes)')
Muscle_Stiffness = st.number_input('M-Stiffness 0(No) & 1(Yes)')
Hair_Loss = st.number_input('Hair Loss 0(No) & 1(Yes)')

features = np.array([[Age,Gender,Weakness,Genital_Thrush,Visual_Blurring,Itching,Irritability,Delayed_Healing,Obesity,Excessive_Urine_Prod,Excessive_Thirst,Sudden_Weight_Loss,Excessive_Hunger,Muscle_Weakness,Muscle_Stiffness,Hair_Loss]])

if st.button('Predict'):
    
    prediction = RForest.predict(features)
    if prediction ==0:
        st.write(f'The predicted outcome is Negative')
    else:
        st.write(f'The predicted outcome is Positive')
   
