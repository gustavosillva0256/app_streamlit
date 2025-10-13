# Cache buster para Streamlit Cloud
cache_clear_version = "2025-10-12-19-00-00"

"""
📚 App Streamlit - Sistema de Análise Educacional - ES
🎯 Tema: Análise de dados educacionais do Espírito Santo
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
from pages.sobre import render_sobre
from pages.formacao import render_formacao
from pages.estatisticas import render_estatisticas
from pages.evolucao import render_evolucao
from pages.comparativos import render_comparativos

# ---------------------------------------------------------
# ⚙️ Configuração da Página
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sistema de Análise Educacional - ES",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 🎨 CSS Customizado Seguro para Streamlit Cloud
# ---------------------------------------------------------
st.markdown("""
<style>

/* Fundo geral do app */
.stApp {
    background-color: #ffffff !important;
    color: #262730 !important;
    font-family: "Inter", "Segoe UI", sans-serif !important;
}

/* Container principal */
.main .block-container {
    background-color: #ffffff !important;
    color: #262730 !important;
    padding: 1.5rem 2rem !important;
    border-radius: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f4f6fa !important;
    border-right: 1px solid #e0e0e0 !important;
}

/* Títulos e headers */
h1, h2, h3, h4, h5, h6 {
    color: #1c1c1c !important;
    font-weight: 600 !important;
}

/* Linhas divisórias */
hr {
    border: 1px solid #e0e0e0 !important;
}

/* Métricas (cards de valores) */
div[data-testid="stMetricValue"] {
    color: #1f77b4 !important;
}
div[data-testid="stMetricLabel"] {
    color: #444444 !important;
}

/* Botões */
.stButton > button {
    background-color: #1f77b4 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 0.5rem 1.2rem !important;
    font-weight: 500 !important;
    transition: all 0.2s ease-in-out !important;
}
.stButton > button:hover {
    background-color: #155a8a !important;
}

/* Campos de input */
div[data-baseweb="input"] > input {
    background-color: #ffffff !important;
    color: #262730 !important;
    border: 1px solid #cccccc !important;
    border-radius: 6px !important;
}

/* Dataframes / tabelas */
[data-testid="stDataFrame"] {
    background-color: #ffffff !important;
    border-radius: 6px !important;
}

/* Rodapé e menu padrão */
footer, #MainMenu {
    visibility: hidden !important;
}

/* Corrige conflitos do tema claro */
[data-testid="stMarkdownContainer"] {
    color: #262730 !important;
}

/* Corrige gráficos Plotly sumindo */
.js-plotly-plot * {
    background-color: transparent !important;
}

/* Links */
a {
    color: #1f77b4 !important;
    text-decoration: none !important;
}
a:hover {
    text-decoration: underline !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 🚀 Função Principal
# ---------------------------------------------------------
def main():
    """Função principal do aplicativo"""
    
    # Cabeçalho
    render_header()
    
    # Barra lateral com navegação
    selected_page = render_sidebar()
    
    # Páginas
    if selected_page == "Dashboard":
        render_dashboard()
    elif selected_page == "Sobre o Sistema":
        render_sobre()
    elif selected_page == "Formação de Professores":
        render_formacao()
    elif selected_page == "Estatísticas por Região":
        render_estatisticas()
    elif selected_page == "Evolução Temporal":
        render_evolucao()
    elif selected_page == "Comparativos":
        render_comparativos()

# ---------------------------------------------------------
# ▶️ Execução
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
