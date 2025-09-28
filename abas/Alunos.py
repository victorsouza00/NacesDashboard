import streamlit as st
import pandas as pd
from test import planilha
from graficos.graficos_alunos import mostrarPlanilha,CursoAluno,Deficiencias,CursoAlunoPorcentagem,DeficienciasPorcentagem,CursoAlunoPorcentagemPizza,DeficienciasPorcentagemPizza,SituacaoXDeficiencias

def mostrar():
    st.title("📈 Alunos")
    st.write("Aqui você pode visualizar os alunos.")

    df = mostrarPlanilha(planilha, 2)
    st.dataframe(df)
    st.text("Alunos : " + str(df.shape[0]))

    busca = st.text_input("Buscar:")
    if busca:
        df_busca = df[df.apply(lambda row: row.astype(str).str.contains(busca, case=False).any(), axis=1)]
        st.dataframe(df_busca)

    col1, col2  = st.columns(2)
    with col1:
        CursoAluno(df)
    with col2:
        Deficiencias(df)
    col3,col4 = st.columns(2)
    with col3:
        CursoAlunoPorcentagem(df)
    with col4:
        DeficienciasPorcentagem(df)

    col5,col6 = st.columns(2)
    with col5:
        CursoAlunoPorcentagemPizza(df)
    with col6:
        DeficienciasPorcentagemPizza(df)
    col7,col8 = st.columns(2)
    with col7:
        SituacaoXDeficiencias(df)
