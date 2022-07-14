#import streamlit as st

#st.title("Este es mi proyecto")

import streamlit as st
import time

st.write("Usuario:", st.secrets.db_username)
st.write("Password:", st.secrets.db_password)

#@st.cache()
def funcion_inevitablemente_lenta(a, b):
    time.sleep(2)
    return a * b

c1, c2, c3, c4 = st.columns([1, 1, 1, 2])
a = int(c1.text_input("a", value=1))
b = int(c2.text_input("b", value=2))
axb = funcion_inevitablemente_lenta(a, b)
c4.title(f"{a} * {b} = {axb}")
