import streamlit as st
import pickle
import sklearn

model = pickle.load(open('model.pkl','rb'))

st.title("Iris Species Predictor")
st.subheader('Enter species details below')

sepal_length = st.number_input('Sepal Length',min_value=3.5,max_value=8.5)
sepal_width = st.number_input('Sepal Width',min_value=1.5,max_value=5.0)
petal_length = st.number_input('Petal Length',min_value=1.0,max_value=7.5)
petal_width = st.number_input('Petal Width',min_value=0.1,max_value=3.0)

if st.button('Predict'):
    result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
    if result == 0:
        st.header("Setosa")
        st.image('Irissetosa.jpg')
    elif result == 1:
        st.header("Virginica")
        st.image('iris_virginica.jpg')
    else:
        st.header("Versicolor")
        st.image('Iris_versicolor.jpg')