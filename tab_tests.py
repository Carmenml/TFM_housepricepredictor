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
