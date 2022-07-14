import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.title("Procesando un archivo csv")

# Cargar un archivo csv y leerlo pudiendo seleccionar el tipo de encoding y el separador.
st.header("Cargando un archivo")
c1, c2, c3 = st.columns(3)
uploaded_file = c1.file_uploader("Cargar un archivo csv", type=["csv"])
encoding = c2.selectbox("Enconding", ["utf-8", "latin-1", "utf-16"])
separator = c3.selectbox("Separador", [",", ";", "|", "tab"]).replace("tab", "\t")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding=encoding, sep=separator, dtype=str)

    # Mostrar las primeras 10 líneas cargadas del archivo.
    st.dataframe(df.head(10))

    # Indicar el número de columnas y filas del archivo.
    st.header("Número de columnas y filas")
    st.write(f"Número de columnas: {len(df.columns)}")
    st.write(f"Número de filas: {len(df)}")

    # Indicar para cada columna el nombre de la columna, el número de valores distintos, el valor más frecuente, el número de valores nulos y el porcentaje de valores nulos.
    st.header("Información de cada columna")
    c1, c2 = st.columns(2)
    col = c1.selectbox("Seleccionar columna", df.columns)
    dtype = c2.selectbox("Seleccion tipo de dato", ["str", "int", "float"])
    s = df[col].astype(dtype)
    c1.write(f"Nombre de la columna: {col}")
    c1.write(f"Número de valores distintos: {len(df[col].unique())}")
    c1.write(f"Valor más frecuente: {df[col].value_counts().idxmax()}")
    c2.write(f"Número de valores nulos: {df[col].isnull().sum()}")
    c2.write(f"Porcentaje de valores nulos: {df[col].isnull().sum() / len(df) * 100}%")

    # Seleccionar 1 columna y realiza un histograma de los valores.
    st.header("Histograma")
    fig = plt.figure(figsize=(10, 6)) 
    plt.hist(s, bins=20, orientation='horizontal')
    st.pyplot(fig)
    #st.pyplot()