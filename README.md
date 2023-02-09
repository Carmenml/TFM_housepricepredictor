# TFM_propertypricepredictor 
Este repositorio contiene todo lo relacionado con mi proyecto final de master (Data Science). Consiste en un análisis de la oferta actual de venta de inmuebles en Churriana, Málaga, que incluye un modelo predictivo del precio del inmueble.

## Objetivo

El objetivo del proyecto es poder localizar oportunidaes de inversión de viviendas a la venta en la zona de Churriana. Se desarrolla una app con Stramlit dónde visualmente se puede identificar las viviendas más rentables en función de las características que se desee. Por otro lado se decide completar el proyecto incluyendo en la app otro apartado en el que una persona introduce datos de su vivienda y la herramienta le proporciona el precio estimado de mercado.

### Pasos para replicar mi proyecto

1. Clonar mi repositorio tfmpricepredictor: git clone https://github.com/Carmenml/TFM_propertypricepredictor.git

2. Crear entorno virtual y activarlo:
    * conda env create -f environment.yml 
    * seguidamente activar dicho entorno con el siguiente comando: conda activate tfm-env.

3. orden de ejecución. 
El repositorio está dividido en las siguientes carpetas:

* Informativas
    * data_scrapping: contiene los dataset extraídos del scraping, por un lado un dataset de los ids de la zona de estudio (Churriana) y por otro el dataset con la información de cada vivienda correspondiente a ese id. 
    * data: contiene todos los datasets que se han ido generando a partir del tratamiento del dataset inicial scrapeado.
    * graficas: contiene pngs de las gráficas que se han ido generando en todos los notebooks.
* A ejecutar:
    * notebooks (con orden de ejecución):
        * 1_Scrapping.ipynb (no ejecutar, ya tenemos los datos generados en la carpeta data-scrapping)
        * 2_Exploracion_data-churriana.ipynb
        * classes.ipynb
        * Store.ipynb
        * Funciones_modelos_ML.ipynb
        * Evaluacion_modelos_ML.ipynb
        * Evaluacion_modelos_ML_WithoutOutliers.ipynb
        * Aplicacion_modelo_final.ipynb

Tras ejecutar los notebooks ejecutamos de los archivos que no están en ninguna carpeta el de front-end-app.py para abrir la aplicación en nuestro local. Para ello ejecutamos en el terminal el comando run  front-end-app.py. Es importante que tengamos activado el entorno mencionado environment.yml(tfm-env),

Los diferentes archivos fuera de las carpetas:
* Informativo
    * README.md (leer)
    * initial_idea_presentation.pdf
    * 0_Herramientas y Librerías necesarias.txt: contiene todo lo usado para realizar el proyecto.

* A aplicar o ejecutar
    * environment.yml: entorno de conda usado para el desarrollo del proyecto llamado tfm-env. se debe activar en vuestro dispositivo:
        * conda env create -f environment.yml 
        * seguidamente activar dicho entorno con el siguiente comando: conda activate tfm-env.
        
    * front-end-app.py: aplicación para la parte del front end desarrollada con streamlit:
        * streamlit run front-end-app.py
        
Una vez en funcionamiento la app ya podéis deisfrutar de la visualización de las viviendas más rentables o ver cual sería el precio de vuestra vivienda.


<fontsize= '30px'><strong>¡Gracias!</strong></fontsize>