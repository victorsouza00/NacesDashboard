import streamlit as st
import pandas as pd
from test import planilha
from graficos.graficos_tutores import Ativos,Bolsista,CursoTutor,mostrarPlanilha

def mostrar():
    st.title("📊 Tutores")
    st.write("Aqui você pode visualizar os tutores.")

    df = mostrarPlanilha(planilha,0)
    st.dataframe(df)
    st.text("Tutores : " + str(df.shape[0]))

    busca = st.text_input("Buscar:")
    if busca:
        df_busca = df[df.apply(lambda row: row.astype(str).str.contains(busca, case=False).any(), axis=1)]
        st.dataframe(df_busca)

    col1, col2  = st.columns(2)
    with col1:
        CursoTutor(df)
    with col2:
        Bolsista(df)

    col3 , col4 = st.columns(2)
    with col3:
        Ativos(df)
