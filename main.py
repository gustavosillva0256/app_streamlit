"""
📚 App Streamlit - Fluxo de Formação de Professores (CEFOPE)
👨‍💻 Desenvolvedor: Gustavo Pereira
🎯 Tema: Análise do fluxo de formação de professores através do CEFOPE
"""

import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os

# Adiciona o diretório src ao path para importações
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from components.header import render_header
from components.sidebar import render_sidebar
from pages.dashboard import render_dashboard
from pages.formacao import render_formacao
from pages.estatisticas import render_estatisticas
from pages.evolucao import render_evolucao
from pages.comparativos import render_comparativos

# Configuração da página
st.set_page_config(
    page_title="CEFOPE - Formação de Professores",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Função principal do aplicativo"""
    
    # CSS customizado - FORÇA TEMA CLARO no Streamlit Cloud
    st.markdown("""
    <style>
    /* FORÇA TEMA CLARO - Streamlit Cloud Cache Buster */
    .stApp {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Sidebar clara */
    .stSidebar {
        background-color: #f0f2f6 !important;
    }
    
    /* Conteúdo principal */
    .main .block-container {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #262730 !important;
    }
    
    /* Cards */
    .stMetric {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
    }
    
    /* Tabelas */
    .stDataFrame {
        background-color: #ffffff !important;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #1f77b4 !important;
        color: white !important;
    }
    
    /* Override para Streamlit Cloud */
    .stApp > div {
        background-color: #ffffff !important;
    }
    
    /* Forçar todos os elementos */
    * {
        background-color: inherit !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Renderiza o cabeçalho
    render_header()
    
    # Renderiza a barra lateral com navegação
    selected_page = render_sidebar()
    
    # Renderiza a página selecionada
    if selected_page == "Dashboard":
        render_dashboard()
    elif selected_page == "Formação de Professores":
        render_formacao()
    elif selected_page == "Estatísticas por Região":
        render_estatisticas()
    elif selected_page == "Evolução Temporal":
        render_evolucao()
    elif selected_page == "Comparativos":
        render_comparativos()

if __name__ == "__main__":
    main()
