import pickle
import streamlit as st

# Load the model
model = pickle.load(open('estimasi_mobil_toyota.sav', 'rb'))

# Title
st.title('Estimasi Harga Mobil Second Toyota')

# Input
year = st.number_input('Tahun')
mileage = st.number_input('Jarak Tempuh Mobil')
tax = st.number_input('Pajak Mobil')
mpg = st.number_input('Konsumsi BBM')
engineSize = st.number_input('Ukuran Mesin')

# Predict
predict = ''
if st.button('Estimasi Harga Mobil'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])[0]
    st.write(f'Harga mobil bekas Toyota sekitar: EUR {predict:,.0f}')
    st.write(f'Harga mobil bekas Toyota sekitar: IDR (Juta) {predict*17180}')