import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("predict the Loan Amount")
st.markdown("Enter your details below:")

# Input fields
gender = st.text_input("gender",value="Male or Female")
married = st.text_input("Married",value="Yes or No")
education = st.text_input("education",value="Graduate or Not Graduate")
self_employed = st.text_input("Employed",value="Yes or NO")
income = st.number_input("Annual Income (KPA)", value=100)
credit_score = st.number_input("score", value=0.68)
property_area = st.selectbox(
    "Area",
    ['Urban', 'Semiurban', 'Rural']
)

if st.button("Predict loan Amount"):
    input_data = {
        "gender": gender,
        "married": married,
        "education": education,
        "self_employed": self_employed,
        "income": income,
        "credit_his": credit_score,
        "pro_area": property_area
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