import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("predict the Loan Amount")
st.markdown("Enter your details below:")

# Input fields
Gender = st.text_input("gender",value="Male or Female")
Married = st.text_input("Married",value="Yes or No")
Education = st.text_input("education",value="Graduate or Not Graduate")
Self_Employed = st.text_input("Employed",value="Yes or NO")
ApplicantIncome = st.number_input("Annual Income (KPA)", value=100)
Credit_History = st.number_input("score", value=0.68)
Property_Area = st.selectbox(
    "Area",
    ['Urban', 'Semiurban', 'Rural']
)

if st.button("Predict loan Amount"):
    input_data = {
        "Gender": Gender,
        "Married": Married,
        "Education": Education,
        "Self Employed": Self_Employed,
        "Income": ApplicantIncome,
        "Credit Score": Credit_History,
        "Property Area": Property_Area
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "response" in result:
            prediction = result["response"]
            st.success(f"Predicted loan amount: **{prediction['predicted amount']}**")
            st.write("🔍 Confidence:", prediction["confidence"])
            st.write("📊 Class Probabilities:")
            st.json(prediction["class_probabilities"])

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")