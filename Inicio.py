import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("Mi primera App en Streamlit")
st.write("¡¡¡Hola Mundo!!!")

st.subheader("Datos")
N = 10
df = pd.DataFrame(100*np.random.randn(5, N), columns=('col%d' % i for i in range(N)))
st.dataframe(df)  # Same as st.write(df)

st.subheader("Gráficos")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader("Foto de gato porque internet")
st.image("https://cataas.com/cat/cute")