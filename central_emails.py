import streamlit as st

# Ao abrir a página define a home como página inicial
if not 'pagina_central_email' in st.session_state:
    st.session_state.pagina_central_email = 'home'


def mudar_pagina(nome_pagina):
    """
    Função responsável pela alteração dos nomes das páginas na session_state
    """
    st.session_state.pagina_central_email = nome_pagina


def home():
    """
    Função responsável por preencher o que será apresentado na Página Home
    """
    st.markdown("# Central de Emails")


def pag_templates():
    """
    Função responsável por preencher o que será apresentado na Página Templates
    """
    st.markdown("# Templates")


def pag_lista_emails():
    """
        Função responsável por preencher o que será apresentado na Página Lista de Emails
        """
    st.markdown("# Lista de Emails")


def pag_configuracao():
    """
        Função responsável por preencher o que será apresentado na Página Configuração
        """
    st.markdown("# Configuração")


def main():
    """
    Função principal
    :return:
    """
    # Definição dos Botões da Sidebar
    st.sidebar.button("Central de Emails", use_container_width=True, on_click=mudar_pagina, args=('home',))
    st.sidebar.button("Templates", use_container_width=True, on_click=mudar_pagina, args=('templates',))
    st.sidebar.button("Lista de Emails", use_container_width=True, on_click=mudar_pagina, args=('lista_emails',))
    st.sidebar.button("Configuração", use_container_width=True, on_click=mudar_pagina, args=('configuracao',))

    if st.session_state.pagina_central_email == 'home':
        home()

    elif st.session_state.pagina_central_email == 'templates':
        pag_templates()

    elif st.session_state.pagina_central_email == 'lista_emails':
        pag_lista_emails()

    elif st.session_state.pagina_central_email == 'configuracao':
        pag_configuracao()


if __name__ == "__main__":
    main()
