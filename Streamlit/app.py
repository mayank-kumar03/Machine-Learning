import streamlit as st
import pandas as pd
import numpy as np


st.title("Streamlit App with Pandas and Numpy")


##dispaly simple text
st.write("this is a simple text")

##create a dataframe
df = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8],
    "C": [9, 10, 11, 12]
})
##display the dataframe
st.write("this is a dataframe")
st.dataframe(df)


##create a line chart
chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c']
)
st.line_chart(chart_data)