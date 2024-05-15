import streamlit as st
import pandas as pd
import pickle 
import json
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

#load files

with open('list_cat_cols.txt', 'r') as file_1:
  list_cat_col = json.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
  list_num_col = json.load(file_2)

with open('model_knn.pkl', 'rb') as file_3:
  model_knn = pickle.load(file_3)



def run():
    #buat form inputan
    with st.form('form_harga_sewa'):
        BHK = st.number_input('BHK',  min_value = 1, max_value = 3, value = 1)
        Size = st.number_input('Size', min_value = 10, max_value = 8000, value = 750)
        Floor = st.number_input('Floor', min_value = 1, max_value = 76, value = 1)
        Bathroom = st.number_input('Bathroom', min_value = 1, max_value = 10, value = 1)

        st.markdown('---')

        Area_Type = st.selectbox('Area Type', ('Super Area', 'Carpet Area'))
        City = st.selectbox('City', ('Kolkata', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad'))
        Furnishing_Status = st.selectbox('Furnishing Status', ('Unfurnished', 'Semi-Furnished', 'Furnished'))
        Tenant_Preferred = st.selectbox('Tenant Preferred', ('Bachelors/Family', 'Bachelors', 'Family'))
        Point_of_Contact = st.selectbox('Point of Contact', ('Contact Owner', 'Contact Agent', 'Contact Builder'))
        
        #submit button
        submitted = st.form_submit_button('Predict')
    
    data_inf = {
        'BHK' : 2,
        'Rent': 15000,
        'Size' : 750, 
        'Floor' : 1, 
        'Area Type' : 'Super Area', 
        'Area Locality' : 'Dumdum Park', 
        'City' : 'Koltaka',
        'Furnishing Status' : 'Semi-Furnished', 
        'Tenant Preferred' : 'Bachelors', 
        'Bathroom' : 1,
        'Point of Contact' : 'Contact Owner'
        }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        numerical_cols = list_num_col
        categorical_cols = list_cat_col

        # Making column transformer for preprocessing
        transformer = ColumnTransformer([
        ('scaler', StandardScaler(), numerical_cols),
        ('encoding', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ])
        # Transform the new data using the pipeline
        predictions = model_knn.predict(data_inf)
        # Print the predictions
        st.write("Predictions Harga Sewa:", predictions)

if __name__ == '__main__':
   run()

