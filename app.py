import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder


#load the trained model
model = tf.keras.models.load_model('model.h5')

#load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
#load the encoder: onehot-encoder & Label-encoder
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)
    
with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)
    

## streamlit app
st.title('CLIENT-RETENTION-INSIGHTS')

#user input
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 95)
balance = st.number_input('Balance', 0.0, 100000.0)
credit_score = st.number_input('Credit Score', 0, 1000)
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_credit_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])


#prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

## one-hot encoded
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

## combine the onehot-encoded data with the input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

## scale the data
input_data_scaled = scaler.transform(input_data)

## predict the churn
prediction = model.predict(input_data_scaled)
prediction_prob = prediction[0][0]

if prediction_prob > 0.5:
    st.write(f'The customer is likely to churn with a Probability: {prediction_prob:.2%}')
else:
    st.write(f'The customer is likely to not churn with a Probability: {(1 - prediction_prob):.2%}')