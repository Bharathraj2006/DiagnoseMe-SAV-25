import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from Predict import predict_page
from about import about_page

with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center;">
        <img src="https://img.icons8.com/fluency/48/000000/medical-doctor.png" width="35" height="35" style="margin-right:50px"/>
        <h1 style="margin:1;">DiagnoseMe</h1>
    </div>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Home", "Predict", "About Us"],
        icons=["house", "activity", "info-circle"],
        menu_icon="cast", 
        default_index=0, 
    )
if selected == "Home":
    st.title("DiagnoseMe: Your Personal Health Assistant")

    st.header("Introduction")
    st.write(
        "DiagnoseMe is an intelligent health prediction tool designed to assist users in identifying potential diseases based on their symptoms. "
        "By inputting your symptoms, you can receive immediate insights into possible health conditions and precautions to take."
    )
    st.image("image.webp", use_column_width=True,width=50)
    st.header("How It Works")
    st.markdown("""
    1. **Select Symptoms**: Choose the symptoms you are experiencing from a categorized list.
    2. **Get Predictions**: Click on the "Predict Disease" button to receive possible disease predictions.
    3. **View Information**: Access detailed descriptions and precautions for the predicted diseases.
    """)

    st.header("Features")
    st.write(
        "- **Symptom-Based Predictions**: Accurate disease predictions based on user-inputted symptoms.\n"
        "- **Detailed Descriptions**: In-depth information about potential diseases.\n"
        "- **Precautions**: Suggestions on what actions to take if a certain disease is predicted.\n"
        "- **User-Friendly Interface**: Easy navigation and symptom selection for a seamless experience."
    )

    st.header("Why Use DiagnoseMe?")
    st.write(
        "DiagnoseMe empowers users to take charge of their health by providing quick access to health information. "
        "It's an invaluable resource for anyone seeking guidance on their symptoms before visiting a healthcare professional."
    )

    st.header("Disclaimer")
    st.write(
        "Please note that DiagnoseMe is not intended to replace professional medical diagnosis or treatment. "
        "Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition."
    )

elif selected == "Predict":
    predict_page()
elif selected == "About Us":
    about_page()
