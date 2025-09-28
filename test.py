import streamlit as st
import gspread 
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import json 
fileName = "tutorianacesufrpe-735e16ea9f89.json"
idFile = "1U-T-xuGMHcCHSnQKo75dVlnuQ61zX3ee22I58rfIork"
title = "Tabela_de_Tutores"

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]


cred_dict = st.secrets["gcp_service_account"]
creds_dict = dict(cred_dict)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes=scope)
client = gspread.authorize(creds)

#creds = ServiceAccountCredentials.from_json_keyfile_name(filename=fileName, scopes=scope)

#client = gspread.authorize(creds)
planilha = client.open_by_key(idFile)



#------------------- Definição do metodos ---------------------

def mostrarPlanilha(planilha, pagina : int):
    planilhaFinal = planilha.get_worksheet(pagina)
    dados = planilhaFinal.get_all_values()  # pega tudo como string
    header = dados[0]  # primeira linha = cabeçalho
    valores = dados[1:]  # resto = dados
    df = pd.DataFrame(valores, columns=header)
    return df


def mostrarPlanilhaTutorados():
    planilhaFinal = planilha.get_worksheet(1)
    df = pd.DataFrame(planilhaFinal.get_all_records())
    return df

def adicionarDados(planilha, worksheet, dados):
    planilhaFinal = planilha.get_worksheet(worksheet)
    planilhaFinal.append_row(dados)
