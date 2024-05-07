import streamlit as st
import requests

st.title("Iris Classification")

sepalLength = st.slider("Sepal Length", 0,10)
sepalWidth = st.slider("Sepal Width", 0,10)

petalLength = st.slider("Petal Length", 0,10)
petalWidth = st.slider("Petal Width", 0,10)

def display_image(prediction):
    st.image(f"images/{prediction}.jpg", use_column_width=True)

def givePrediction():
    data = {"sepalLength":sepalLength, 
            "sepalWidth":sepalWidth, 
            "petalLength":petalLength,
            "petalWidth":petalWidth}
    
    response = requests.post("http://localhost:8000/", json=data)
    if response.status_code == 200:
        y_pred = response.json()["Prediction"]
        if(y_pred==0):
            st.success("Predicted: Setosa")
        
        if(y_pred==1):
            st.error("Predicted: Versicolour")

        if(y_pred==2):
            st.warning("Predicted: Virginica")

        display_image(y_pred)
    else:
        st.error("Request not fulfilled")

st.button("Predict",on_click=givePrediction)
    