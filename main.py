import streamlit as st

def main():
    # Configuração da página
    st.set_page_config(
        page_title="Naces",
        page_icon="📊",
        layout="wide"
    )

    # Menu lateral
    st.sidebar.title("Navegação")
    aba_selecionada = st.sidebar.radio(
        "Selecione a aba:",
        ["📊 Tutores", "📈 Alunos"]
    )

    # Import e renderização da aba escolhida
    if aba_selecionada == "📊 Tutores":
        from abas import Tutores
        Tutores.mostrar()
    elif aba_selecionada == "📈 Alunos":
        from abas import Alunos
        Alunos.mostrar()

if __name__ == "__main__":
    main()
