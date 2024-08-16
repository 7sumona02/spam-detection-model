import streamlit as st
import joblib

model = joblib.load('spam-detection.pkl')

st.title("Email Spam Detector")

email_text = st.text_area("Enter the email text:")

if st.button("Detect Spam"):
    email_text_reshaped = [email_text]  # This converts the input to a list, making it a 2D array
    prediction = model.predict(email_text_reshaped)
    
    if prediction[0] == 1:
        st.write("This email is Spam.")
    else:
        st.write("This email is not Spam.")
