# TFM_propertypricepredictor 
This repository contains all things about my final master's project (Data Science). This consists of an <strong> analysis of the current offer for the sale of properties in Churriana, Malaga </strong> , which includes a <strong> predictive model of the price of the property</strong>.

1. Clonar mi repositorio tfmpricepredictor: git clone https://github.com/Carmenml/TFM_propertypricepredictor.git

2. Crear entorno virtual con el comando conda env create -f tfm_environment.yml. 

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
        * Casses.ipynb
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
    * environment.yml: entorno de conda usado para el desarrollo del proyecto llamado tfm-env. se debe activar en vuestro dispositivo.
    * front-end-app.py: aplicación para la parte del front end desarrollada con streamlit.
