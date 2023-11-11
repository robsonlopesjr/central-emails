from pathlib import Path
import streamlit as st

# Ao abrir a página define a home como página inicial
if not 'pagina_central_email' in st.session_state:
    st.session_state.pagina_central_email = 'home'

# Variável para armazenar o endereço da pasta principal
PASTA_ATUAL = Path(__file__).parent


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

    st.button('Adicionar Template', on_click=mudar_pagina, args=('adicionar_novo_template',))


def pag_adicionar_novo_template():
    """
    Função responsável por preencher o que será apresentado na Página Novo Template
    """
    st.markdown("# Novo Template")
    nome_template = st.text_input('Nome do template:')
    texto_template = st.text_area('Escreva o texto do template:', height=400)
    st.button('Salvar', on_click=salvar_template, args=('nome_template', 'texto_template'))


def salvar_template(nome, texto):
    """
    Função que irá armazenar o template em disco local
    :param nome: str
    :param texto: str
    """
    PASTA_TEMPLATES = PASTA_ATUAL / 'templates'

    # Cria a pasta templates e faz a validação para verificar se ja existe
    PASTA_TEMPLATES.mkdir(exist_ok=True)

    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'

    with open(PASTA_TEMPLATES / nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)

    mudar_pagina('templates')


def pag_lista_emails():
    """
    Função responsável por preencher o que será apresentado na Página Lista de Emails
    """
    st.markdown("# Lista de Emails")

    st.button('Adicionar Lista', on_click=mudar_pagina, args=('adicionar_nova_lista',))


def pag_adicionar_nova_lista():
    """
    Função responsável por preencher o que será apresentado na Página Nova Lista de Emails
    """
    st.markdown("# Nova Lista")
    nome_lista = st.text_input('Nome da lista:')
    emails_lista = st.text_area('Escreva os e-mails separados por vírgula:', height=400)
    st.button('Salvar', on_click=salvar_lista, args=('nome_lista', 'emails_lista'))


def salvar_lista(nome, texto):
    """
    Função que irá armazenar a lista de e-mails em disco local
    :param nome: str
    :param texto: str
    :return:
    """
    PASTA_LISTAS = PASTA_ATUAL / 'lista_email'

    # Cria a pasta listas e faz a validação para verificar se ja existe
    PASTA_LISTAS.mkdir(exist_ok=True)

    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'

    with open(PASTA_LISTAS / nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)

    mudar_pagina('lista_emails')


def pag_configuracao():
    """
    Função responsável por preencher o que será apresentado na Página Configuração
    """
    st.markdown("# Configuração")


def main():
    """
    Função principal
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

    elif st.session_state.pagina_central_email == 'adicionar_novo_template':
        pag_adicionar_novo_template()

    elif st.session_state.pagina_central_email == 'lista_emails':
        pag_lista_emails()

    elif st.session_state.pagina_central_email == 'adicionar_nova_lista':
        pag_adicionar_nova_lista()

    elif st.session_state.pagina_central_email == 'configuracao':
        pag_configuracao()


if __name__ == "__main__":
    main()
