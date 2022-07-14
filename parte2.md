# Parte 2 - Practical Kindom
*Nuestro héroe perfecciona sus habilidades y triunfa sobre el desafío* 

## 1. Actividad Práctica: Analizando un archivo cargado por usuario

Completar el archivo `pages/01_📃_Archivo.py` para que, usando la librería pandas y matplotlib, permita:
- [ ] Cargar un archivo csv y leerlo pudiendo seleccionar el tipo de encoding y el separador.
- [ ] Mostrar las primeras 10 líneas cargadas del archivo.
- [ ] Indicar el número de columnas y filas del archivo.
- [ ] Indicar para cada columna el nombre de la columna, el número de valores distintos, el valor más frecuente, el número de valores nulos y el porcentaje de valores nulos.
- [ ] Seleccionar 1 columna y realiza un histograma de los valores.

En `./datasets/` existen 2 datasets para testear la actividad: [`ExhaustiveDinosaurDataset.csv`](https://www.kaggle.com/datasets/kjanjua/jurassic-park-the-exhaustive-dinosaur-dataset) y [`CoffeeQuantityDataset.csv`](https://www.kaggle.com/datasets/volpatto/coffee-quality-database-from-cqi).

## 2. Session State

Considera el siguiente código a ejecutar en streamlit:

```python
c1, c2 = st.columns([1,2])
has_clicked = c1.button("Haz Click")
if has_clicked:
    c2.write("Presionaste el boton!!!")
else:
    c2.write("No has hecho presionado el boton")
```

Al ejecutarlo, funciona tal como esperabas. Por defecto, `st.button` regresa el valor `False` y al hacer click en él, cambia a `True` (y se actualiza el mensaje).

Tomemos ahora un ejemplo un poco distinto:

```python
c1, c2 = st.columns([1, 2])
has_clicked = c1.button("Haz Click")
number_of_clicks = 0
if has_clicked:
    number_of_clicks += 1
    c2.write(f"Has presionado el boton!!!. Número de clicks: {number_of_clicks}")
else:
    c2.write("No has presionado el boton")
```

El código anterior **NO** funciona para que el usuario pueda saber cuantas veces ha hecho click en el botón. ¿Porqué? Porque Streamlit ejecuta el script de nuevo cada vez que se carga la página, por lo que el valor de `number_of_clicks` se resetea a 0.

Para solucionar este problema, podemos usar `session_state` de Streamlit. Puedes imaginar `st.session_state` como un diccionario que es persistente en la sesión del usuario. Puedes poner en este diccionario cualquier elemento que quieras, pero ¡ten cuidado de asegurarte que inicializarlo con un valor inicial! 

Arreglemos el ejemplo:

```python
c1, c2 = st.columns([1, 2])
has_clicked = c1.button("Haz Click")
if "number_of_clicks" not in st.session_state:
    st.session_state["number_of_clicks"] = 0
if has_clicked:
    st.session_state["number_of_clicks"] += 1
    c2.write(f"Has presionado el boton!!!. Número de clicks: {st.session_state.number_of_clicks}")
else:
    c2.write("No has presionado el boton")
```

Puedes aprender más de session_state en [Session State API reference](https://docs.streamlit.io/library/api-reference/session-state).

## 5. Optimization

A esta altura te habrás dado cuenta que Streamlit no es super veloz. Por ello, algunos trucos te ayudarán a que la experiencia de usuario 
sea un poco más fluída.

Consideremos el siguiente ejemplo - ejecútalo!

```python
import streamlit as st
import time

def funcion_inevitablemente_lenta(a, b):
    time.sleep(2)
    return a * b

c1, c2, c3, c4 = st.columns([1, 1, 1, 2])
a = int(c1.text_input("a", value=1))
b = int(c2.text_input("b", value=2))
axb = funcion_inevitablemente_lenta(a, b)
c4.title(f"{a} * {b} = {axb}")
```

Al probar distintas combinaciones, vemos que la función es muy lenta. Al probar una combinación ya probada anteriormente, la función se ejecuta de nuevo.

Compara ahora con el siguiente ejemplo:

```python
import streamlit as st
import time

@st.cache()
def funcion_inevitablemente_lenta(a, b):
    time.sleep(2)
    return a * b

c1, c2, c3, c4 = st.columns([1, 1, 1, 2])
a = int(c1.text_input("a", value=1))
b = int(c2.text_input("b", value=2))
axb = funcion_inevitablemente_lenta(a, b)
c4.title(f"{a} * {b} = {axb}")
```

En este caso, hemos simplemente agregado `@st.cache` a la función. Esto significa que cada ejecución de la función se guarda en memoria, considerando sus argumentos como parte de la clave (además de otras cosas). Si vuelves a pedir la ejecución de la función para valores que ya son conocidos, se carga directamente de la memoria y no se ejecuta de nuevo.

Puedes aprender más de optimización de rendimiento en [Optimize performance with st.cache](https://docs.streamlit.io/library/advanced-features/caching), y en [Performance Optimization Methods](https://docs.streamlit.io/library/api-reference/performance).

## 3. Secrets

Nunca es aconsejable guardar contraseñas o información de tarjeta de crédito en el código (escribiéndolas directamente como variables) o en el repositorio (escribiéndolas en un archivo). Para solucionar este problema, Streamlit propociona un diccionario llamado `st.secrets`. ¿Como funciona? Muy simple:
* Si estás en Streamlit Share, los valores de `st.secrets` se pueden completar mediante la interface web en "Settings/Secrets" con la convención apropiada. 
* Si estás en local o con otro medio de deployment, debes crear (NO DEJAR EN EL REPOSITORIO) un archivo llamado `secrets.toml` en una carpeta llamada `.streamlit`. 

El formato de `secrets.toml` es un archivo de configuración de [TOML], que es muy similar a python. Por ejemplo, podría contener la siguiente línea:

```toml
# Este es un comentario
db_username = "Jane" 
db_password = "12345qwerty"
```

Puedes acceder a los valores disponibles en `st.secrets` como si fuera un diccionario:

```python
st.write("Usuario:", st.secrets.db_username)
st.write("Password:", st.secrets.db_password)
```

Puedes aprender más al respecto en 
[Secrets Management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management).

## 4. Query parameters

Cada vez tenemos más herramientas a nuestra disposición.

Una funcionalidad adicional que puede ser útil, es la de recuperar los parámetros de la URL. Esto puede usarse para consumir una API, o incluso esconder "Easter Eggs". 

Por ejemplo, imaginemos que el usuario está en la dirección `http://localhost:8501/?show_map=True&selected=asia&selected=america`. Puedes acceder a los query parameters usando lo siguiente:

```python
query_params = st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}
```

**Importante**: Los valores que regresa el diccionario para cada llave son siempre una lista, aunque el usuario haya entregado un único valor. Esto tiene sentido porque potencialmente el usuario puede entregar más de un valor para una misma llave.

De manera complementaria, si después de procesar ciertos parámetros, quieres volver a redirigir al usuario a una url con ciertos parametros, puedes usar la función `st.experimental_set_query_params`.

Para llevar aal usuario a la `http://localhost:8501/?show_map=True&selected=asia&selected=america`, deberías hacer lo siguiente:

```python
query_params = {show_map=True,
                selected=["asia", "america"],
                }
st.experimental_set_query_params(**query_params)
```

## 6. Streamlit components

Los componentes son extensiones realizados por la comunidad, pero no directamente por Streamlit. Algunos componentes han terminado por integrarse a Streamlit, cuando la funcionalidad es importante o muy útil. 

En el siguiente enlace puedes encontrar la [lista oficial de Componentes](https://streamlit.io/components) mientras que en este otro enlace, está la [lista no oficial de componentes](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634).

Hay muchos ejemplos, pero los más interesantes son los siguientes:
* [Drawable Canvas](https://share.streamlit.io/andfanilo/streamlit-drawable-canvas-demo/master/app.py) por Fanilo Andrianasolo.
* [WebRTC](https://share.streamlit.io/whitphx/streamlit-webrtc-example/main/app.py) por Yuichiro Tachibana.

En muchos casos, los componentes son una forma de empaquetar una funcionalidad o librería que ya existe en html/javascript, y lograr que pueda llamarse de manera nativa en Streamlit. 

Puedes encontrar la información oficial en [Streamlit Components](https://docs.streamlit.io/library/components).

## 7. Actividad Práctica: Consumiendo un API
Una API es una mecanismo de conectarse con un computador y lograr que haga cosas: entregar información (método GET), recibir información (método POST), etc.

![API](images/api.png){:height="400px"}

Algunos ejemplos de API:
* [dog.ceo](https://dog.ceo/dog-api/documentation/): API de perros (gratuita, abierta).
* [thecatapi](https://thecatapi.com/): API de gatos (pagada, requiere registro).
* [catfact](https://catfact.ninja/): API de gatos (gatuita 🤣, abierta).
* [api.nasa.gov](https://api.nasa.gov/): Api de la NASA (gratuita, requiere registro).
* [funtranslations](https://funtranslations.com/api/): API de traducciones (gratuita, abierta).
* [pokeapi](https://pokeapi.co/): API de pokemones (gratuita, abierta).
* [dinoipsum](https://dinoipsum.com/): API para generar texto de dinosaurios (gratuita, abierta).
* [dinosaur-facts-api](https://dinosaur-facts-api.shultzlab.com/): API para obtener datos de dinosaurios (gratuita, pública).
* [imgur api](https://apidocs.imgur.com/): API de Imgur (gratuita, requiere registro).
* [giphy api](https://developers.giphy.com/explorer): API de Giphy (gratuita, requiere registro).
* [github api](https://api.github.com/): API de Github (gratuita, requiere registro).
* [spotify api](https://developer.spotify.com/documentation/web-api/): API de Spotify (gratuita, requiere registro).
* [A Curated List of 100 Cool and Fun Public APIs to Inspire Your Next Project](https://betterprogramming.pub/a-curated-list-of-100-cool-and-fun-public-apis-to-inspire-your-next-project-7600ce3e9b3)
* [25 Crazy APIs For Your Next Project](https://blog.snap.hr/24/09/2018/25-crazy-apis-next-project/)
* [7 cool APIs you didn't know you needed](https://www.twilio.com/blog/cool-apis)

En esta actividad, completaremos la información de la pagina web con información que obtendremos una API.
La API que usaremos es la de [dog.ceo](https://dog.ceo/dog-api/documentation/). 

Editar el archivo `pages/02_🌐_API.py` para que:

- [ ] Obtenga una lista de todas las razas de perros.

- [ ] Permita al usuario seleccionar una raza específica.

- [ ] Muestre una foto al azar de un perro de esa raza.

- [ ] Muestre una foto de cada una de las subrazas, si existen.

## 8. Seguir aprendiendo

Consejos:
* No aprender sólo por saber. Buscar un proyecto apasionante, y aprender en lla medida que se necesita. ¡Hay que tirarse a la piscina!
* Seguir el desafío: "[30 días de Streamlit](https://share.streamlit.io/streamlit/30days)"

![LINKS](./images/link.png){:height="250px"}

Comunidades:
* Foro Oficial: https://discuss.streamlit.io/
* Discord: https://discord.com/invite/bTz5EDYh9Z

📖 Libros:
* Getting Started with Streamlit for Data Science, de Tyler Richards

Twitter:
* Streamlit: @streamlit
* Fanilo Andrianasolo: @andfanilo
* Charlie Wargnier: @DataChaz
* JM Napoles: @napoles3D