import streamlit as st
st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["Inputs", "Control", "Output y Media", "Celebración"])

with tab1:
     c1, c2, c3, c4, c5, c6 = st.columns(6)
     c1.button("st.button")
     c2.checkbox("st.checkbox")
     c3.number_input("st.number_input", value=5, min_value=0, max_value=10, step=1)
     c4.slider("st.slider", value=50, min_value=0, max_value=100, step=1)
     c5.date_input("st.date_input")  
     c6.time_input("st.time_input")  
     st.write("---")
     c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
     c1.color_picker("st.color_picker")
     c2.text_input("st.text_input")
     c3.text_area("st.text_area")
     c4.radio("st.radio", options=["AM", "FM", "Online"])
     c5.selectbox("st.selectbox", options=["Sopaipilla", "Terremoto", "Mote con Huesillo", "Pastel de Choclo"])
     c6.select_slider("st.select_slider", options=["uno", "dos", "tres", "cuatro"])
     c7.multiselect("st.multiselect", options=["Tomate", "Palta", "Mayo", "Mostaza", "Ketchup", "Piña"])
     st.write("---")
     c1, c2, c3, c4 = st.columns([1,1,1,1])
     c2.camera_input("st.camera_input")
     c3.file_uploader("st.file_uploader")

with tab2:
     c1, c2, c3, c4 = st.columns(4)
     c1.error("st.error")
     c2.warning("st.warning")
     c3.info("st.info")
     c4.success("st.success")

     _, c1, c2, c3,_ = st.columns(5)
     if c1.button("Botón para mostrar st.progress"):
          import time
          my_bar = c1.progress(0)
          for i in range(0,101,10):
               my_bar.progress(i)
               time.sleep(.2)
          my_bar.empty()
     if c2.button("Botón para mostrar st.spinner"):
          import time
          with st.spinner('Desaparecerá en 1.5 segundos...'):
               time.sleep(1.5)
     if c3.button("Botón para mostrar st.exception"):
          try:
               1/0
          except Exception as e:
               st.exception(e)

with tab3:
     c1, c2, c3, c4, c5 = st.columns(5)
     c1.download_button("st.download_button", data=b"0101", help="Una explicación al botón")
     c2.metric("st.metric", "#1")
     c3.code("st.write\nst.markdown\nst.title\nst.header\nst.subheader\nst.caption\nst.code\nst.text\nst.latex")
     c4.code("st.dataframe\nst.table\nst.json")
     c5.code("st.line_chart\nst.area_chart\nst.bar_chart\nst.pyplot\nst.altair_chart\nst.vega_lite_chart\nst.plotly_chart\nst.bokeh_chart\nst.pydeck_chart\nst.graphviz_chart\nst.map")
     st.write("---")
     c1, c2, c3 = st.columns(3)
     c1.caption("st.image")
     c1.image("https://images.unsplash.com/photo-1548407260-da850faa41e3")
     c2.caption("st.audio")
     c2.audio("https://upload.wikimedia.org/wikipedia/commons/b/bb/Test_ogg_mp3_48kbps.wav")
     c3.caption("st.video")
     c3.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
     
with tab4:
     c1, c2, c3, c4 = st.columns([3,1,1,3])
     if c2.button("¡Feliz fiesta!"):
          st.balloons()
     if c3.button("¡Feliz Navidad!"):
          st.snow()
