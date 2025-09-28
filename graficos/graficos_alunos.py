import streamlit as st
import pandas as pd
import plotly.express as px

def mostrarPlanilha(planilha, pagina : int):
    planilhaFinal = planilha.get_worksheet(pagina)
    dados = planilhaFinal.get_all_values()  # pega tudo como string
    header = dados[0]  # primeira linha = cabeçalho
    valores = dados[1:]  # resto = dados
    df = pd.DataFrame(valores, columns=header)
    return df

def CursoAluno(df):
    contagem = df["CURSO"].value_counts().sort_index()
    chart_df = pd.DataFrame({"Quantidade" : contagem})
    with st.container():
        st.subheader("Cursos dos Alunos")
        st.bar_chart(chart_df, use_container_width=True)

def Deficiencias(df):
    deficienciasSplit = df["DEFICIENCIA(S)"].dropna().apply(lambda x: [d.strip() for d in x.split(",")])
    deficienciasAll = [item for sublist in deficienciasSplit for item in sublist]
    contagem = pd.Series(deficienciasAll).value_counts().sort_index()
    chart_df = pd.DataFrame({"Quantidade" : contagem})
    with st.container():
        st.subheader("Deficiências dos Alunos")
        st.bar_chart(chart_df, use_container_width=True)

def CursoAlunoPorcentagem(df):
    contagem = df["CURSO"].value_counts(normalize=True).sort_index() * 100
    chart_df = pd.DataFrame({"Porcentagem" : contagem.round(2)})
    with st.container():
        st.subheader("Porcentagem de Alunos por Curso")
        st.bar_chart(chart_df, use_container_width=True)

def DeficienciasPorcentagem(df):
    deficienciasSplit = df["DEFICIENCIA(S)"].dropna().apply(lambda x: [d.strip() for d in x.split(",")])
    deficienciasAll = [item for sublist in deficienciasSplit for item in sublist]
    contagem = pd.Series(deficienciasAll).value_counts(normalize=True).sort_index() * 100
    chart_df = pd.DataFrame({"Porcentagem" : contagem.round(2)})
    with st.container():
        st.subheader("Porcentagem de Alunos por Deficiências")
        st.bar_chart(chart_df, horizontal=True,use_container_width=True)

def CursoAlunoPorcentagemPizza(df):
    contagem = df["CURSO"].value_counts()
    fig = px.pie(values=contagem.values, names=contagem.index, title="Distribuição de Alunos por Curso")
    st.plotly_chart(fig, use_container_width=True)

def DeficienciasPorcentagemPizza(df):
    deficienciasSplit = df["DEFICIENCIA(S)"].dropna().apply(lambda x: [d.strip() for d in x.split(",")])
    deficienciasAll = [item for sublist in deficienciasSplit for item in sublist]
    contagem = pd.Series(deficienciasAll).value_counts()
    fig = px.pie(values=contagem.values, names=contagem.index, title="Distribuição de Alunos por Deficiências")
    st.plotly_chart(fig, use_container_width=True)

def SituacaoXDeficiencias(df):
    status = df["SITUAÇÃO ACADÊMICA"].value_counts().sort_index()
    statusOptions = list(status.index) + ["Todos"]
    
    deficienciasSplit = df["DEFICIENCIA(S)"].dropna().apply(lambda x: [d.strip() for d in x.split(",")])
    deficienciasAll = [item for sublist in deficienciasSplit for item in sublist]
    deficienciasUniqueOptions = sorted(set(deficienciasAll))

    deficienciaSelected = st.selectbox("Escolha a deficiência:", options=sorted(deficienciasUniqueOptions)+["Todos"])
    statusSelected = st.selectbox("Escolha o status:", options=statusOptions)

    df_filtrado = df.copy()
    if deficienciaSelected != "Todos":
        df_filtrado = df_filtrado[df_filtrado["DEFICIENCIA(S)"].str.contains(deficienciaSelected, na=False)]
    if statusSelected != "Todos":
        df_filtrado = df_filtrado[df_filtrado["SITUAÇÃO ACADÊMICA"] == statusSelected]

    contagem = df_filtrado["SITUAÇÃO ACADÊMICA"].value_counts().sort_index()
    chart_df = pd.DataFrame({"Quantidade" : contagem})  
    with st.container():
        st.subheader("Situação Acadêmica X Deficiências")
        st.bar_chart(chart_df, use_container_width=True)