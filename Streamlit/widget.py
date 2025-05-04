import streamlit as st
import pandas as pd

st.title("streamlit text input")
name=st.text_input("Enter your name")


age=st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is {age}")


options=["python", "java", "c++"]
selected_option=st.selectbox("Select your option", options)
st.write(f"You selected {selected_option}")



if name:
    st.write(f"Hello {name}")




data={
      "Name": ["Alice", "Bob", "Charlie"],
      "Age": [25, 30, 35],
      "City": ["New York", "Los Angeles", "Chicago"]
}

df=pd.DataFrame(data)
st.write("This is a dataframe")
st.dataframe(df)
st.write("This is a table")


uploaded_file=st.file_uploader("Upload a CSV file", type=["csv"])


if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write("This is the uploaded CSV file")
    st.dataframe(df)


