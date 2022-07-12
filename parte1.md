# Parte 1 - Streamlit World
*Nuestro héroe abandona su mundo conocido y debe desarrollar nuevas habilidades* 

## Sobre mi

### ¿Quién soy?

Trabajo en la empresa uPlanner como Chief Data Officer, liderando los equipos de Data Scientists y Data Engineers (¿Interesado? ¡contáctame!). Llevo programando en Python desde el 2008, y siempre estoy buscando nuevas librerías. Actualmente me gustan matplotlib y altair para los gráficos, pandas para la manipulación de datos, jupyter notebooks para la colaboración y exploración, y streamlit para compartir y disponibilizar código y funcionalidades en línea. He participado en diversas PyCon (Colombia, Argentina, Chile, Latam) y desarrollado algunas librerías open source (pypsdier y streamlit_book). 

¿Más sobre mí? [Github](), [Twitter]() & [Linkedin]().

### ¿Qué relación tengo con streamlit?

Aprendí de la librería streamlit en plena pandemia. Por formación, desarrollo código pero no tengo experiencia (ni tiempo) para convertir código en una GUI/página web. Streamlit solucionó ese problema y me permitió generar mucha visibilidad en mi trabajo y ayudarme a resolver muchos problemas (y crear otros).

En Noviembre del 2021 hice una charla sobre streamlit en la PyCon Chile donde presenté directamente desde una app hecha en streamlit, y poco después, comencé a participar más activamente en la comunidad de streamlit. He participado en 2 hackatones de Streamlit, obteniendo premios en ambas, y publicado en el blog de streamlit.

### Ventajas que presenta usar Streamlit
* Ofertas de trabajo: se está volviendo una librería extreamadamente popular. 
* Cada proyecto se vuelve algo concreto y que puedo compartir, mejora la visibilidad de mi trabajo.
* He ganado premios en Hackatones.


### Puro bla bla bla... muéstranos algunos ejemplos!
Algunas de mis apps, por orden cronológico:
Míos:
https://stbook-template.streamlitapp.com/
https://sebastiandres-streamlit-happy-birds-happy-birds-qzi7ap.streamlitapp.com/ 
https://sebastiandres-ml-edu-confusion-matrix-streamlit-app-3q5126.streamlitapp.com/
https://sebastiandres-streamlit-xkcd-streamlit-app-0f8sh1.streamlitapp.com/ 
https://datasaurus.streamlitapp.com/
* xkcd plots: mi primera app en streamlit, explorando los widgets y cómo graficar.
* sdad
* The confusion matrix
* happy birds
* Multipage template app
Ejemplos
https://share.streamlit.io/spiruel/satschool/main/app.py  
https://streamlit.io/gallery
https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
https://share.streamlit.io/streamlit/roadmap/
https://github.com/jrieke/best-of-streamlit 
https://share.streamlit.io/streamlit/demo-deepdream
https://streamlit.io/components
https://geospatial.streamlitapp.com/
https://share.streamlit.io/streamlit/demo-deepdream

 



## Sobre Streamlit

### ¿Cuándo usar streamlit?
Usa Streamlit si quieres:
* Concentrarte en tu código pero también poder compartirlo con el resto del mundo de manera sencilla.
* No necesitas que la página web sea "ultra-responsiva" y no necesitas tener un control completo del diseño de la página. 
* Si tu webapp no está orientada a smartphones.
* Si quieres crear aplicaciones en minutos y no en horas.

### ¿Qué es streamlit?
* Es una librería para python que permite crear webapps interactivas 100% python y de manera MUY sencilla
* Con multiples opciones de deployment
* Con soporte nativo a librerías de visualización como matplotlib, plotly, altair, etc.
* Con una una comunidad extremadamente activa desarrollando mejoras, nuevos componentes, tutoriales y más.

### Historia
Streamlit recientemente cumplió 2 años y sacó su release 1.10.0, con un versionamiento vertiginoso.

IMAGEN DE LAS STARS

En X 2022 fue adquirida por Snowflake, una compañía de software que ofrece una plataforma de datos para el desarrollo de aplicaciones.

### Filosofía
"Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps."

Es muchísimo más simple de usar que frameworks para la web como django, flask, bottle u otras. ¡Todo es python!

En el nicho de dashboard y webapps se relaciona con las librerías: plotly, panel, voila y gradio.

Personalmente, antes de conocer streamlit usaba jupyter notebooks como wrapper de código.

### ¿Porqué usar streamlit?

* Fácil: Elementos, variables, archivos, gráficos, etc: todo es Python 🐍
* Simple pero potente: Programar con streamlit es como jugar con legos... está diseñado para encajar perfectamente y que puedas armar todo lo que quieras.
* Batteries included: Incluye una colección de elementos de construcción, extensible mediante componentes, y por supuesto, con todas tus librerías favoritas.


## Instalación

### ¿Cómo instalar streamlit?
Es una librería de python: usa pip

```
pip install streamlit
```

o si quieres una versión específica
```
pip install streamlit==1.10.0
```

### ¿Cómo desarrollar en streamlit?
Si quieres desarrollar una webapp y compartirla, conviene generar un ambiente de trabajo para que puedas la ejecución sea reproducible: crea un archivo `requirements.txt` con las librerías y sus versiones a utilizar.

```
# requirements.txt
streamlit==1.10.0
matplotlib==3.1.3
```

Con virtualenv creas un ambiente de trabajo e instalas las librerías desde requirements.txt:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
(para salir del ambiente virtual, usa `deactivate`)

### Versionamiento: cuidado con la version!

## Ejecutando en local
- Ejemplos. Virtualenvs.
- Actividad 1.2: Ejecutar en local

### Actividad práctica 1.1
Para las actividades del taller resulta ideal contar con una cuenta gratuita en github. Si no tienes una, puedes crearla en github.com. Si no tienes cuenta y no deseas crear una, puedes ejecutar en local las actividades y unicamente no podrás hacer deployment a la nube.

Realiza las siguientes tareas:

[+] Realiza un fork del repositorio

[+] Descarga el repositorio a local: 
```
git clone myuser@github:mirepo
```

[+] Genera el ambiente virtual y activalo
```
virtualenv venv
source venv/bin/activate
```

[+] Instala las librerías
```
pip install -r requirements.txt
```

[+] Levanta la aplicación
```
streamlit run streamlit_app.py
```

¿Cómo se usa?
(1) Crear y editar un archivo streamlit_app.py con algún contenido:

## Elementos de Streamlit
La [documentación de la API](https://docs.streamlit.io/library/api-reference) de streamlit es magnífica. Revísala frencuentamente, porque la librería mejora semana a semana.

### Configuración (setup)
El primer paso (o el último paso, según prefieras) es realizar algunas configuraciones de la aplicación. Estas son opcionales, pero permiten hacer que la aplicación se vea mejor.

La función `set_page_config` ([doc](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)) permite configurar el favicon y título de la página en el navegador, y también si el texto debe ocupar todo el ancho posible (`wide`) o centrado (`centered`). Debe ser el primer comando que se ejecuta en la aplicación, después de importar la(s) librería(s).

```
st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="❤️",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
```

La funcionalidad de multipágina es muy reciente en Streamlit ([api](https://docs.streamlit.io/library/get-started/multipage-apps)). Su funcionamiento es sencillo: todas las páginas adicionales a mostrar deben existir en una carpeta llamada `pages`. Los archivos se mostrarán de manera alfabética, y el nombre de la página será el nombre del archivo (omitiendo si existe inicialmente un número o un emoji)

```
Home.py # Archivo principal a ejecutar mediante "streamlit run Home.py"
└─── pages/
  └─── 1_Intro.py # Primera página
  └─── 2_Página_dos.py # Segunda página
  └─── 99_😎_Ultima_página.py # Tercera página, y tiene como ícono un emoji 😎
```

### ¿Cómo colocar elementos?
Existen varios formas de ordenar el contenido de una aplicación: 

* Columnas ([st.columns]()): Permite crear columnas de ancho fijo, agregado elementos a cada uno de ellas.

```
col1, col2 = st.columns(2) # Anchos iguales
#col1, col2 = st.columns([2, 1]) # Anchos proporcionales
with col1:
    st.write("A cat")
    st.button("A button")
col2.button("Another button")
col2.write("A dog")
```

* Expander ([st.expander]()): Permite crear un elemento acordeón que se despliega o se contrae.

```
with st.expander("Título del expander"):
    # Este contenido se muestra solo cuando se expande el elemento
    st.write("Hola mundo")
```

* Tabs ([st.tabs]()): Permite crear un menú de pestañas.

```
with st.tabs("Título de la pestaña 1"):
    # Este contenido se muestra en la pestaña 1
    st.write("Hola mundo")

with st.tabs("Título de la pestaña 2"):
    # Este contenido se muestra en la pestaña 2
    st.write("¿Que tal, festival?")
```

* Sidebar ([st.sidebar]()): Permite agregar elementos a la barra lateral de la aplicación. Esta barra lateral se muestra sólo si tiene elementos en ella (páginas o elementos agregados).

```
# En lugar de llamar a st directamente
# Llamamos a st.sidebar
st.sidebar.write('Esto está en el sidebar')
if st.sidebar.button('Mi botón opcional'):
    st.balloons()
```



Existe un trucazo muy interesante. Si necesitas calcular varias cosas y mostrar un elemento después, puedes generar un placeholder utilizando la función `st.empty`.
Con ello, streamlit sabe que tiene que reservar un lugar para un elemento que le será alimentado después (y que puede ser cualquier elemento válido y compatible). También puedes usar `st.empty` para hacer desaparecer un elemento creado de esta forma.

Prueba copiando, pegando y ejecutando este código en el archivo `pages/99_🗑️_sandbox.py`
```
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
```

### ¿Qué elementos colocar?
- inputs
- control flow, messages
- text, media, charts

- Actividad 1.3: Personalizar la página principal

## Deployment a la nube
- Streamlit cloud

¿Como se comparte online?
Prerrequisito: Almacenar en un repositorio con git.
Streamlit Cloud
Múltiples opciones: gratis y de pago

Permite vincular a repositorio de github y hacer deploy en 1 click

¡La página web se actualiza automática al cambiar el código en el repositorio!

La opción gratis permite tener hasta 3 apps en línea.

- Otras opciones: hugging face, heroku, azure, aws, etc.
- Actividad 1.4: Subir cambios a github y subir a la nube

## Componentes
- Donde buscar. 
- Ejemplos: ¿camara yuihiro?

## Consejos
- Revisar la api constantemente. Siempre agregan nuevas funcionalidades.
- Seguir en redes sociales a @streamlit y personas de interés.