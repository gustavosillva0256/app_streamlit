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
    
    # CSS customizado para garantir tema claro - v3.0 - Streamlit Cloud Fix
    st.markdown("""
    <style>
    /* Tema claro - CSS ULTRA AGRESSIVO para Streamlit Cloud */
    .stApp {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Sidebar clara - seletores múltiplos */
    .stSidebar,
    .css-1d391kg,
    .css-1d391kg .css-1v0mbdj,
    .stSidebar .css-1d391kg,
    .stSidebar .css-1d391kg .css-1v0mbdj,
    .stSidebar .css-1d391kg .css-1v0mbdj .css-1v0mbdj {
        background-color: #f0f2f6 !important;
    }
    
    /* Texto principal - múltiplos seletores */
    .main .block-container,
    .main .block-container > div,
    .main .block-container > div > div {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Headers - todos os níveis */
    h1, h2, h3, h4, h5, h6,
    .main .block-container h1,
    .main .block-container h2,
    .main .block-container h3 {
        color: #262730 !important;
    }
    
    /* Cards com borda sutil */
    .stMetric,
    .stMetric > div,
    .stMetric > div > div {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
    }
    
    /* Tabelas - múltiplos seletores */
    .stDataFrame,
    .stDataFrame table,
    .stDataFrame table tr,
    .stDataFrame table td {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #1f77b4 !important;
        color: white !important;
    }
    
    /* Forçar tema claro no Streamlit Cloud - ULTRA AGRESSIVO */
    .stApp > div,
    .stApp > div > div,
    .stApp > div > div > div {
        background-color: #ffffff !important;
    }
    
    /* Override para elementos específicos do Streamlit Cloud */
    .stApp [data-testid="stSidebar"] {
        background-color: #f0f2f6 !important;
    }
    
    .stApp [data-testid="stSidebar"] * {
        background-color: #f0f2f6 !important;
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
