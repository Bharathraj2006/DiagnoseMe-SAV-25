import streamlit as st
import numpy as np
import joblib
import pandas as pd

def predict_page():
    model = joblib.load('diagnose_model.pkl')
    le_disease = joblib.load('le_disease.pkl')
    mlb = joblib.load('mlb.pkl')
     
    descriptions_df = pd.read_csv('Description.csv')
    precautions_df = pd.read_csv('Precaution.csv')

    st.title('Disease Prediction System')
    symptoms = { 
        "Skin Symptoms": [
            "itching", "skin rash", "nodal skin eruptions",
            "dischromic patches", "yellowish skin", "internal itching",
            "red spots over body", "pus filled pimples", "blackheads",
            "skin peeling", "silver-like dusting", "small dents in nails",
            "inflammatory nails", "blister", "red sore around nose",
            "yellow crust ooze", "redness of eyes"
        ],
        "Gastrointestinal Symptoms": [
            "stomach pain", "acidity", "ulcers on tongue", "vomiting",
            "abdominal pain", "nausea", "loss of appetite",
            "burning micturition", "spotting urination", "passage of gases",
            "indigestion", "diarrhoea", "constipation", "belly pain",
            "yellow urine", "foul smell of urine", "fluid overload"
        ],
        "Respiratory Symptoms": [
            "cough", "chest pain", "breathlessness", "continuous sneezing",
            "shivering", "chills", "watering from eyes", "mucoid sputum",
            "rusty sputum", "throat irritation", "phlegm"
        ],
        "General/Systemic Symptoms": [
            "fatigue", "weight loss", "restlessness", "lethargy",
            "irregular sugar level", "blurred and distorted vision", "obesity",
            "excessive hunger", "increased appetite", "polyuria",
            "sunken eyes", "dehydration", "high fever", "mild fever",
            "sweating", "muscle pain", "malaise", "joint pain",
            "pain behind the eyes", "back pain"
        ],
        "Neurological Symptoms": [
            "dizziness", "loss of balance", "lack of concentration",
            "stiff neck", "depression", "irritability",
            "visual disturbances", "weakness in limbs", "neck pain",
            "weakness of one body side", "altered sensorium", "unsteadiness",
            "mood swings", "anxiety", "slurred speech", "spinning movements"
        ],
        "Other Symptoms": [
            "extra marital contacts", "family history",
            "history of alcohol consumption", "receiving blood transfusion",
            "toxic look (typhos)", "bruising", "swollen legs",
            "swollen blood vessels", "prominent veins on calf", "weight gain",
            "cold hands and feet", "abnormal menstruation", "knee pain",
            "hip joint pain", "swelling joints", "painful walking",
            "movement stiffness", "cramps", "drying and tingling lips",
            "muscle wasting", "headache", "dark urine", "swelled lymph nodes",
            "acute liver failure", "swelling of stomach", "distention of abdomen",
            "bladder discomfort", "continuous feel of urine"
        ]
    }


    selected_categories = st.multiselect("", list(symptoms.keys()))
    selected_symptoms = []
    
    if selected_categories:
        for category in selected_categories:
            st.subheader(category)
            for symptom in symptoms[category]:
                if st.checkbox(symptom, key=symptom):  
                    selected_symptoms.append(symptom)
    if selected_symptoms:
        st.markdown("### Selected Symptoms:")
        for symptom in selected_symptoms:
            st.write(f"- {symptom}")
    else:
        st.write("No symptoms selected yet.")

    if len(selected_symptoms) >= 8: 
        if st.button('Predict'):
            try:
                
                input_encoded = mlb.transform([selected_symptoms])
                prediction = model.predict(input_encoded)
                predicted_disease = le_disease.inverse_transform(prediction)

                st.write(f'### Predicted Disease: {predicted_disease[0]}')

                description = descriptions_df.loc[descriptions_df['Disease'].str.lower() == predicted_disease[0].lower(), 'Description']
                if not description.empty:
                    st.markdown("### Disease Description:")
                    st.write(description.values[0])
                else:
                    st.write("No description available for this disease.")

                precautions = precautions_df.loc[precautions_df['Disease'].str.lower() == predicted_disease[0].lower(), ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
                if not precautions.empty:
                    st.markdown("### Precautions:")
                    for precaution in precautions.values.flatten():
                        st.write(f"- {precaution}")
                else:
                    st.write("No precautions available.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning('Please select at least 8 symptoms to proceed.')
