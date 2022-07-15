import streamlit as st
import requests
st.set_page_config(layout="wide")

def get_data(api_url):
    """
    This is a wrapper around requests.get that returns a json object, if possible.
    """
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        return response.json()['message']
    else:
        st.write(f"Error: {response.status_code} {response.text}")
        return None

st.title("Consumiendo la API de DOG.CEO")
api_url = "https://dog.ceo/dog-api/documentation/"
st.markdown(f"Todos los datos e imágenes mostrados se generan dinámicamente desde la API de [Dog.ceo]({api_url})")

# Get the list of all breeds
c1, c2 = st.columns(2)
breeds_dict = get_data("https://dog.ceo/api/breeds/list/all")

# Preprocessing the data
if breeds_dict:
    st.warning("Completar código")
    # Sort

    # Sort alphabetically

# Display
if breeds_dict:
    st.warning("Completar código")
    # Display the breeds that have more than 1 subbreed 

    # Create the select box

    # Get an image of the selected breed

    # Subbreeds
