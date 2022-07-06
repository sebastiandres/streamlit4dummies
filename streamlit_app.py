import streamlit as st
import streamlit_book as stb

# Set wide display
st.set_page_config(layout="wide")

# Set multipage
save_answers = False

stb.set_book_config(menu_title="App Title",
                    menu_icon="apple",
                    options=[
                            "Intro",   
                            "Multitest", 
                            ], 
                    paths=[
                            "pages/Intro.py", 
                            "pages/00 Multitest", 
                            ],
                    icons=[
                            "tree", 
                            "code", 
                            ],
                    save_answers=save_answers,
                    )