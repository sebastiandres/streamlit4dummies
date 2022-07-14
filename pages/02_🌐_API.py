import streamlit as st
import requests

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

st.title("Consumiendo una API")

api_url = "https://dog.ceo/dog-api/documentation/"
st.markdown(f"Todos los datos e imágenes mostrados se generan dinámicamente desde la API de [Dog.ceo]({api_url})")

# Get the list of all breeds

c1, c2 = st.columns(2)
breeds_dict = get_data("https://dog.ceo/api/breeds/list/all")
breed_with_subbreeds = []
for breed in breeds_dict:
    subbreeds = breeds_dict[breed]
    if len(subbreeds) > 0:
        breed_with_subbreeds.append(f"{breed} ({len(subbreeds)} sub-breeds)")
    else:
        breed_with_subbreeds.append(breed)

if breeds_dict:
    # Create the select box
    breed_sel = c1.selectbox('Selecciona una raza', breed_with_subbreeds)
    breed = breed_sel.split(' ')[0]
    # Get an image of the selected breed
    api_url =  f"https://dog.ceo/api/breed/{breed}/images/random"
    image_url = get_data(api_url)
    if image_url:
        c1.image(image_url, width=300)
        c1.caption(f"Imagen de la raza {breed}")
    # Subbreeds
    subbreeds = breeds_dict[breed]
    N_subbreeds = len(subbreeds)
    if N_subbreeds > 0:
        cols = st.columns(N_subbreeds)
        for i, subbreed in enumerate(subbreeds):
            api_url = f"https://dog.ceo/api/breed/{breed}/{subbreed}/images/random"
            image_url = get_data(api_url)
            if image_url:
                cols[i].image(image_url)
                cols[i].caption(f"Imagen de la subraza {subbreed}")