import streamlit as st
import joblib
import numpy as np
st.set_page_config(page_title="Salary prediction",layout="centered")
model=joblib.load("salary_training_model.pkl")
st.title("salary prediction App")
st.write("Prediaction salary based on years of professional experiance")
st.sidebar.header("Employee information")
exp=st.sidebar.number_input("years of experiance",min_value=30,max_value=60,step=1)
if st.button("Predict salry"):
    input=np.array([[exp]])
    pred=model.predict(input)
    # to display the result
    st.success(f"predicted salary={pred}")