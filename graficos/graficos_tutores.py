import streamlit as st
import pandas as pd


def BolsistaManual(df):
    # Conta bolsistas e voluntários
    bolsistas_preg = (df['BOLSAS'] == "Bolsista - PREG").sum()
    bolsistas = (df['BOLSAS'] == "Bolsista").sum()
    bolsistas_naces = (df['BOLSAS'] == "Bolsista - NACES").sum()
    chart_df = pd.DataFrame({
        'Quantidade': [bolsistas_preg, bolsistas, bolsistas_naces]
    }, index=['Bolsistas - PREG', 'Bolsistas', 'Bolsistas - NACES'])

    with st.container():
        st.subheader("Tipo de Bolsas")
        st.bar_chart(chart_df, use_container_width=True)

def Bolsista_(df):
    # Conta todos os tipos de bolsas automaticamente
    contagem = df['BOLSAS'].value_counts().sort_index()
    chart_df = pd.DataFrame({'Quantidade': contagem})

    with st.container():
        st.subheader("Tipo de Bolsas")
        st.bar_chart(chart_df, use_container_width=True)

def Ativos(df):
    # Conta ativos e inativos
    contagem = df["SITUAÇÃO"].value_counts().sort_index()
    chart_df = pd.DataFrame({'Quantidade': contagem})
    with st.container():
        st.subheader("Status dos Tutores")
        st.bar_chart(chart_df, use_container_width=True)

    
def Bolsista(df):
    cursos = df["CURSO DO(A) TUTOR(A)"].unique()
    cursos_opcoes = list(cursos) + ["Todos"]

    status = df["SITUAÇÃO"].unique() 
    status_opcoes = list(status) + ["Todos"]

    curso_escolhido = st.selectbox("Escolha o curso:", options=sorted(cursos_opcoes))
    status_escolhido = st.selectbox("Escolha o status:", options=status_opcoes)

    df_filtrado = df.copy()
    if curso_escolhido != "Todos":
        df_filtrado = df_filtrado[df_filtrado["CURSO DO(A) TUTOR(A)"] == curso_escolhido]

    if status_escolhido != "Todos":
        df_filtrado = df_filtrado[df_filtrado["SITUAÇÃO"] == status_escolhido]

    contagem = df_filtrado["BOLSAS"].value_counts().sort_index()
    chart_df = pd.DataFrame({"Quantidade": contagem})

    with st.container():
        st.subheader("Tipo de Bolsas")
        st.bar_chart(chart_df, use_container_width=True)

def CursoTutor(df):
    contagem = df["CURSO DO(A) TUTOR(A)"].value_counts().sort_index()
    chart_df = pd.DataFrame({"Quantidade" : contagem})
    with st.container():
        st.subheader("Cursos dos Tutores")
        st.bar_chart(chart_df, use_container_width=True)


def mostrarPlanilha(planilha, pagina : int):
    planilhaFinal = planilha.get_worksheet(pagina)
    dados = planilhaFinal.get_all_values()  # pega tudo como string
    header = dados[0]  # primeira linha = cabeçalho
    valores = dados[1:]  # resto = dados
    df = pd.DataFrame(valores, columns=header)
    return df

