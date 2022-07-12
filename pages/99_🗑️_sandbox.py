import streamlit as st

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

import time
if st.button("Click me!"):
    st.write("Uno")
    e2 = st.empty()
    e3 = st.empty()
    e3.write("Tres")
    time.sleep(2)
    e2.write("Dos")
    time.sleep(2)
    e3.empty()
    e2.empty()