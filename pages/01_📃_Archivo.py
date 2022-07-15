import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.title("Procesando un archivo csv")

# Cargar un archivo csv y leerlo pudiendo seleccionar el tipo de encoding y el separador.
st.header("Cargando un archivo")
c1, c2, c3, c4 = st.columns([3,1,1,1])
uploaded_file = c1.file_uploader("Cargar un archivo csv", type=["csv"])
encoding = c2.selectbox("Enconding", ["utf-8", "latin-1", "utf-16"])
separator = c3.selectbox("Separador", [",", ";", "|", "tab"]).replace("tab", "\t")
nrows = c4.number_input("Número de filas", value=10, min_value=1, step=1)

if uploaded_file is not None:
    # Cargar las primeras 10 líneas
    uploaded_file.seek(0) # Trick to reset the file pointer to the beginning of the file


    # Mostrar el dataframe

    # Indicar el número de columnas y filas del archivo.

    # Describir el dataframe

    # Seleccionar 1 columna y realiza un histograma de los valores.