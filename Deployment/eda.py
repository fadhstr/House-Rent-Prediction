import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title='House Rent - EDA'
)

def run():
    st.title('House Rent Prediction')
    st.subheader('EDA untuk analisa dataset House Rent') 

    image = Image.open('house.jpg')
    st.image(image, caption='House Rent')

    st.write('Page ini dibuat oleh Fadhil')
    st.write('**Milestone2**')
    st.write('# Milestone2')

    st.markdown('---')

    df = pd.read_csv('House_Rent_Dataset.csv')
    st.dataframe(df)

    # Histogram untuk melihat distribusi harga sewa
    plt.figure(figsize=(8, 6))
    plt.hist(df['Rent'], bins=20)
    plt.title('Price of Rent')
    plt.xlabel('Rent')
    plt.ylabel('Frequency')
    st.pyplot()

    # Scatterplot between Furnishing Status and Rent
    plt.figure(figsize=(8, 6))
    plt.scatter(data=df, x='Furnishing Status', y='Rent')
    plt.title('Furnishing Status vs Rent')
    st.pyplot()

    # Scatterplot between Size and Rent
    plt.figure(figsize=(8, 6))
    plt.scatter(data=df, x='Size', y='Rent')
    plt.title('Size vs Rent')
    st.pyplot()

    # Box plot untuk melihat adanya outlier
    plt.figure(figsize=(8, 6))
    plt.boxplot(df['Rent'])
    plt.title('Boxplot of Rent')
    plt.xlabel('Rent')
    st.pyplot()

    # Membuat Bar chart area type
    plt.figure(figsize=(8, 6))
    Area_Type_freq = df['Area Type'].value_counts()
    Area_Type_freq.plot(kind='bar', rot=0)
    st.pyplot()

if __name__ == '__main__':
    run()
