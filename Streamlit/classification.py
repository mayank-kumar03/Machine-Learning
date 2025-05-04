import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load data function
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load the dataset
df, target_names = load_data()

# Train the model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Sidebar title
st.sidebar.title("Input Features")

# Input sliders
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Prepare input data
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

# Display prediction
st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")


