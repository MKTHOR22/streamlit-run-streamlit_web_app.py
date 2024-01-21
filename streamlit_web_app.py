import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Text elements
st.title("Streamlit Web App")
st.header("Text Elements")
st.write("This is a Streamlit web application that showcases various elements and features.")

# Data elements
st.header("Data Elements")
data = pd.DataFrame({
    'Name': ['Arjun', 'suneel', 'yashu', 'balu'],
    'Age': [19, 20, 20, 23],
    'Salary': [50000, 60000, 70000, 55000]
})
st.dataframe(data)

# Chart elements
st.header("Chart Elements")
fig = px.bar(data, x='Name', y='Salary', title='Salary Distribution')
st.plotly_chart(fig)

# Input widgets
st.header("Input Widgets")
name = st.text_input("Enter your name")
age = st.slider("Select your age", 18, 100, 25)
submit_button = st.button("Submit")

if submit_button:
    st.success(f"Hello {name}, you are {age} years old!")

# Media elements
st.header("Media Elements")
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo", use_column_width=True)

# Layouts and containers
st.header("Layouts and Containers")
col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")

# Chat elements
st.header("Chat Elements")
st.info("This is an informational message.")
st.warning("This is a warning message.")
st.error("This is an error message.")

# Status elements
st.header("Status Elements")
status = st.radio("Select your status", ["Online", "Offline"])
if status == "Online":
    st.success("You are currently online.")
else:
    st.error("You are currently offline.")

# Control flow
st.header("Control Flow")
show_data = st.checkbox("Show Data")
if show_data:
    st.dataframe(data)

# Utilities
st.header("Utilities")
random_number = np.random.randint(1, 100)
st.write(f"Random Number: {random_number}")

# Footer
st.markdown("---")
st.write("Thank you for using this Streamlit web application!")

