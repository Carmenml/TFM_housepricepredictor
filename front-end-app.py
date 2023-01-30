#importación de librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#color fondo de la app

st.markdown("<style>body{ background-color: #F4F4F4;}</style>", unsafe_allow_html=True)

#título app




empty = st.empty()
empty.markdown("<center><div style='color: darkblue; font-size: 40px;'><b>🔑 BUSCADOR DE VIVIENDAS CON RENTABILIDAD</b></div></center>", unsafe_allow_html=True)

st.write(
        """     
- 🤗   ¿Quieres invertir? te mostramos las viviendas con mayor rentabilidad del mercado.
- 🤗   ¿Tienes una vivienda y quieres saber su precio en función de lo que hay actualmente en el mercado? Esta es tu herramienta.
"""
    )

st.markdown('<hr>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Buscardor de viviendas rentables", "¿Cuál es el precio de mi vivienda"])

with tab1:
    st.header("Aquí")
    
with tab2:
    st.header("Aquí2")

#importación de datos
#importacion de prueba con el dataset que cree de precios predicho y variación de precios, este dataset no es correcto hay que hacerlo con el que se cree definitivo. Mientras tanto cogemos este de prueba para configurar la visualización.



data = pd.read_csv('data/datos_finales_visualizacion.csv', index_col = 0)


st.subheader("Aplicar Filtros")
#meter en máximo y mínimo una función que coja automáticamente esos valores de los datos del dataset
room_number = st.slider("Selecciona el número de habitaciones", int(data['room_number'].min()), int(data['room_number'].max()), value=int(data['room_number'].min()))
bath_number = st.slider("Selecciona el número de baños", int(data['bath_number'].min()), int(data['bath_number'].max()), value=int(data['bath_number'].min()))
constructed_area = st.slider("Selecciona los metros cuadrados", int(data['constructed_area'].min()), int(data['constructed_area'].max()), value=int(data['constructed_area'].min()))
Price = st.slider("Precio Máximo", int(data['price'].min()), int(data['price'].max()), value=int(data['price'].max()))
Rentabilidad = st.slider("Rentabilidad mínima", float(data['%_rentabilidad'].min()), float(data['%_rentabilidad'].max()), value=float(data['%_rentabilidad'].min()))

#Aplicar los primeros filtros al dataset.
filtered_data = data.query(f"room_number >= {room_number} and bath_number >= {bath_number} and constructed_area >= {constructed_area}")

st.markdown('<br>', unsafe_allow_html=True)

# Añadir filtros para las diferentes características de la vivienda

has_swimmingpool = st.checkbox("Piscina", value=False)
has_garden = st.checkbox("Jardín", value=False)
has_lift = st.checkbox("Ascensor", value=False)
has_parking = st.checkbox("parking", value=False)
has_terrace = st.checkbox("Terraza", value=False)
is_new_development = st.checkbox("Nueva Construcción", value=False)
is_needs_renovating = st.checkbox("Necesita Reforma", value=False)
is_goog_condition = st.checkbox("En Buena Condición", value=False) #cambiar el nombre a la columna del dataset, por error lo puse mal

    

# filtrar el conjunto de datos en función de los valoresif has_swimmingpool:
if has_swimmingpool:
    filtered_data = filtered_data[filtered_data['has_swimmingpool'] == True]
if has_garden:
    filtered_data = filtered_data[filtered_data['has_garden'] == True]
if has_lift:
    filtered_data = filtered_data[filtered_data['has_lift'] == True]
if has_parking:
    filtered_data = filtered_data[filtered_data['has_parking'] == True]
if has_terrace:
    filtered_data = filtered_data[filtered_data['has_terrace'] == True]
if is_new_development:
    filtered_data = filtered_data[filtered_data['is_new_development'] == True]
if is_needs_renovating:
    filtered_data = filtered_data[filtered_data['is_needs_renovating'] == True]
if is_goog_condition:
    filtered_data = filtered_data[filtered_data['is_goog_condition'] == True]

#filtro precio
filtered_data = filtered_data[filtered_data['price'] <= Price]
filtered_data = filtered_data[filtered_data['%_rentabilidad'] >= Rentabilidad]

st.markdown("<p style='color: darkblue; font-size: 40px;'>Número de viviendas: <strong>{}</strong></p>".format(filtered_data.shape[0]), unsafe_allow_html=True)

st.write("Número de viviendas: ", filtered_data.shape[0])

st.dataframe(filtered_data)




#gráfico habitaciones y baños

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].hist(filtered_data['room_number'], bins = range(int(filtered_data['room_number'].min()), int(filtered_data['room_number'].max())), color = 'orange', edgecolor = 'white')
axs[0].set_xlabel('Número de habitaciones')
axs[0].set_ylabel('Frequency')


axs[1].hist(filtered_data['bath_number'], bins = range(int(filtered_data['bath_number'].min()), int(filtered_data['bath_number'].max())), color= 'orange', edgecolor = 'white')
axs[1].set_xlabel('Número de baños')
axs[1].set_ylabel('Frequency')

st.pyplot()

st.write("holaaaaaaaa")

# Crear la primera gráfica de barras con el número de habitaciones
plt.figure(figsize=(10,5))
plt.bar(filtered_data['room_number'].value_counts().index, filtered_data['room_number'].value_counts().values, color = 'purple')
plt.title('number of Bedroom')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
st.pyplot()

st.pyplot()

# Crear la segunda gráfica de barras con el número de baños
plt.figure(figsize=(10,5))
plt.bar(filtered_data['bath_number'].value_counts().index, filtered_data['bath_number'].value_counts().values, color = 'orange')
plt.title('number of Bathroom')
plt.xlabel('Bathrooms')
plt.ylabel('Count')
st.pyplot()

