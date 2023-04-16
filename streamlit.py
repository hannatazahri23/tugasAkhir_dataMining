import streamlit as st
from sklearn import linear_model
import pandas as pd
import numpy as np

df = pd.read_csv("toyota.csv", usecols = ["year", "mileage", "tax", "mpg", "engineSize", "price"])

model_regresi_linier = linear_model.LinearRegression()
model_regresi_linier.fit(df[["year", "mileage", "tax", "mpg", "engineSize"]], df.price)

st.title('Prediksi Harga Mobil Toyota Bekas')

year = st.number_input("Masukan tahun mobil", 0)
mileage = st.number_input("Masukan KM mobil", 0)
tax = st.number_input("Masukan pajak mobil (*pounds)", 0)
mpg = st.number_input("Masukan konsumsi BBM mobil", 0)
engineSize = st.number_input("Masukan ukuran mesin (per-liter)", 0)

if st.button ("Cek Harga") :
    prediksi = int(model_regresi_linier.predict([[year, mileage, tax, mpg, engineSize]]))
    st.success(f"Prediksi Harga Mobil = RP.{prediksi*18000}")