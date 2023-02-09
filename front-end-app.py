#importación de librerias

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

st.set_page_config(layout="wide")
#Oculta warnings relacionados con Pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown("""
<style>
body{ background-color: #F4F4F4; 
padding-top:0px}
.stButton {padding-left: 20px; margin-top: 20px}
</style>
""", unsafe_allow_html=True)

#título app
empty = st.empty()
empty.markdown("<center><div style='color: darkblue; font-size: 70px;'><b>🔑 BUSCADOR DE VIVIENDAS CON RENTABILIDAD</b></div></center>", unsafe_allow_html=True)


st.markdown("<center><div style='color: orange; font-size: 30px;'><b>BARRIO DE CHURRIANA, MÁLAGA</b></div></center>", unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

#Definiciónde Tabs
tab1, tab2 = st.tabs(["Buscardor de viviendas rentables", "¿Cuál es el precio de mi vivienda?"])


#importacion de datos finales
data = pd.read_csv('data/datos_finales_visualizacion.csv', index_col = 0)
data = data.sort_values(by='%_rentabilidad',ascending=False)

#Configuración Tabs 1 rentabilidad de viviendas
with tab1:
    col1, col2 = st.columns([1,3], gap='medium')
    with col1:
        st.subheader("Aplicar Filtros")
        #meter en máximo y mínimo una función que coja automáticamente esos valores de los datos del dataset
        Price = st.slider("Precio Máximo", int(data['price'].min()), int(data['price'].max()), value=int(data['price'].max()))
        Rentabilidad = st.slider("Rentabilidad mínima", float(data['%_rentabilidad'].min()), float(data['%_rentabilidad'].max()), value=float(data['%_rentabilidad'].min()))
        room_number = st.slider("Selecciona el número de habitaciones", int(data['room_number'].min()), int(data['room_number'].max()), value=int(data['room_number'].min()))
        bath_number = st.slider("Selecciona el número de baños", int(data['bath_number'].min()), int(data['bath_number'].max()), value=int(data['bath_number'].min()))
        constructed_area = st.slider("Selecciona los metros cuadrados", int(data['constructed_area'].min()), int(data['constructed_area'].max()), value=int(data['constructed_area'].min()))

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
        is_goog_condition = st.checkbox("En Buena Condición", value=False)

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
        


    #Configuración Tabs 2 calculador precio de la vivienda  
    with col2:
        #st.subheader("Aplicar Filtros")
        st.markdown("<p style='color: darkblue; font-size: 40px;'>Número de viviendas: <strong>{}</strong></p>".format(filtered_data.shape[0]), unsafe_allow_html=True)

        st.dataframe(filtered_data)

        #gráfico habitaciones y baños
        plt.figure(figsize=(6,3))
        plt.bar(filtered_data['room_number'].value_counts().index, filtered_data['room_number'].value_counts().values, color = 'orange')
        plt.title('Número Habitaciones', color='darkblue')
        plt.xlabel('Habitaciones', color='darkblue')
        plt.ylabel('Count', color='darkblue')
        st.pyplot()

        plt.figure(figsize=(6,3))
        plt.bar(filtered_data['bath_number'].value_counts().index, filtered_data['bath_number'].value_counts().values, color = 'orange')
        plt.title('Número de baños',color='darkblue')
        plt.xlabel('Baños',color='darkblue')
        plt.ylabel('Count',color='darkblue')
        st.pyplot()
        
        #distribución de rentabilidad
        sb.distplot(filtered_data['%_rentabilidad'], color = 'orange')
        plt.title('Distribucíon de rentabilidad', fontsize = 16, color= 'darkblue')
        plt.xlabel('Rentabilidad', fontsize = 10, color='darkblue')
        plt.ylabel('Frecuencia', fontsize = 10, color='darkblue')
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        st.pyplot()
    
with tab2:
    
    col1, col2, col3 = st.columns(3)
    with col1:
        latitud = st.number_input("Latitud", value = 0.0, format="%.5f")
    with col2:
        longitud = st.number_input("Longitud", value = 0.0, format="%.5f")
    with col3:
        cert_energetica = st.selectbox('Cert. energética',
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'desconocido'), index = 7)


    col4, col5, col6 = st.columns(3)
    with col4:
        n_hab = st.number_input("Habitaciones", min_value=0)
    with col5:
        n_bathrooms = st.number_input("Baños", min_value=0)
    with col6:
        construido = st.number_input("Área construida", min_value=0)
    
    col7, col8, col9, col10 = st.columns(4)
    with col7:
        terraza = st.checkbox("Terraza", value=False, key = 'terraza2')
    with col8:
        parking = st.checkbox("Parking", value=False)
    with col9:
        piscina = st.checkbox("Piscina", value=False, key = 'piscina2')
    with col10:
        ascensor = st.checkbox("Ascensor", value=False, key = 'ascensor2')
    
    col11, col12, col13, col14 = st.columns(4)
    with col11:
        jardin = st.checkbox("Jardin", value=False)
    with col12:
        nueva_construccion = st.checkbox("Nueva construcción", value=False)
    with col13:
        renovacion = st.checkbox("Necesita reformas", value=False)
    with col14:
        buenas_cond = st.checkbox("Buenas condiciones", value=False)
    
    calcular = st.button('Calcular')
        
with st.container():
    
    #Abrimos y recuperamos el modelo entrenado para aplicarlo a los datos de entrada del usuario
    pickle_file = open('./notebooks/lr.pickle','rb')
    lr = pickle.load(pickle_file)
    
    #Diccionario Certificacion => Numérico
    certificacion = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'desconocido': 8}
    
    #Estructura de datos definida a partir de los datos de usuario para lanzar la predicción del modelo
    datos_test = {'latitude':[latitud], 'longitude':[longitud], 'energy_certification':[certificacion[cert_energetica]], 'room_number':[n_hab], 'bath_number':[n_bathrooms], 'has_garden':[int(jardin)], 'has_terrace':[int(terraza)], 'has_parking':[int(parking)], 'has_swimmingpool':[int(piscina)], 'has_lift':[int(ascensor)], 'constructed_area':[construido], 'is_new_development':[int(nueva_construccion)], 'is_needs_renovating':[int(renovacion)], 'is_goog_condition':[int(buenas_cond)]}
    
    df = pd.DataFrame(data=datos_test)
    
    if calcular:
        precio_predicho = lr.predict(df)
        empty = st.empty()
        precio_final = '{:,}'.format(int(precio_predicho[0]))
        empty.markdown("<center><div style='color: darkblue; font-size: 25px;'><b>El precio estimado de tu vivienda es</b></div>"
                   "<br><div style='color: darkblue; font-size: 25px;'>" + precio_final + " €</div></center>", unsafe_allow_html=True)