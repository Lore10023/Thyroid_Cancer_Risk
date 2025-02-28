import streamlit as st
import joblib
import numpy as np

model = joblib.load('xgb_model.jb')


st.title("Thyroid Cancer Risk & Diagnosis Prediction")

age = st.number_input("Age", min_value=1, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
country = st.text_input("Country", "USA")
ethnicity = st.text_input("Ethnicity", "Asian")
family_history = st.selectbox("Family History", ["Yes", "No"])
radiation_exposure = st.selectbox("Radiation Exposure", ["Yes", "No"])
iodine_deficiency = st.selectbox("Iodine Deficiency", ["Yes", "No"])
smoking = st.selectbox("Smoking", ["Yes", "No"])
obesity = st.selectbox("Obesity", ["Yes", "No"])
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
tsh_level = st.number_input("TSH Level", min_value=0.0, value=1.0)
t3_level = st.number_input("T3 Level", min_value=0.0, value=1.0)
t4_level = st.number_input("T4 Level", min_value=0.0, value=1.0)
nodule_size = st.number_input("Nodule Size", min_value=0.0, value=1.0)

gender = 1 if gender == "Male" else 0
family_history = 1 if family_history == "Yes" else 0
radiation_exposure = 1 if radiation_exposure == "Yes" else 0
iodine_deficiency = 1 if iodine_deficiency == "Yes" else 0
smoking = 1 if smoking == "Yes" else 0
obesity = 1 if obesity == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0

input_data = np.array([[age, gender, family_history, radiation_exposure, iodine_deficiency, 
                         smoking, obesity, diabetes, tsh_level, t3_level, t4_level, nodule_size]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    diagnosis = "Positive for Thyroid Cancer" if prediction[0] == 1 else "Negative for Thyroid Cancer"
    st.success(f"Predicted Diagnosis: {diagnosis}")