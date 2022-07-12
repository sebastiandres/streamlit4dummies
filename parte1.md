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
* xkcd plots: mi primera app en streamlit, explorando los widgets y cómo graficar.
* sdad
* The confusion matrix
* happy birds
* Multipage template app

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
Todo está en la API

### Configuración (setup)
- set_page_config
- themes
- Multipages

### ¿Cómo colocar elementos?
- layouts
- placeholders
- sidebar

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
- Seguir en redes sociales a @streamlit y personas de interés: 

---
Contenido acá


Parte 1: 55 minutos. Temas: instalación de librerías, ejecutando en local, deployment a la nube (opciones), widgets y lógica de streamlit, consideraciones para multipaging.
Presentación.
About me: Formación, CDO / Streamlit creator.
Streamlit:
Ejemplos
https://streamlit.io/gallery
https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
https://share.streamlit.io/streamlit/roadmap/
https://github.com/jrieke/best-of-streamlit 
https://share.streamlit.io/streamlit/demo-deepdream
https://streamlit.io/components
https://geospatial.streamlitapp.com/
https://share.streamlit.io/spiruel/satschool/main/app.py  
 
Míos:
https://stbook-template.streamlitapp.com/
https://sebastiandres-streamlit-happy-birds-happy-birds-qzi7ap.streamlitapp.com/ 
https://sebastiandres-ml-edu-confusion-matrix-streamlit-app-3q5126.streamlitapp.com/
https://sebastiandres-streamlit-xkcd-streamlit-app-0f8sh1.streamlitapp.com/ 
https://datasaurus.streamlitapp.com/
https://share.streamlit.io/spiruel/satschool/main/app.py  

Como partir
Extensiones
Multipaging
Ayuda
Instalación
Ejecución en local
Deployment a la nube: opciones