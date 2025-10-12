"""
Componente de barra lateral com navegação
"""

import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar():
    """Renderiza a barra lateral com menu de navegação"""
    
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <h3 style="color: #1f77b4; margin: 0;">🧭 Navegação</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Menu de navegação
        selected_page = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Formação de Professores", 
                "Estatísticas por Região",
                "Evolução Temporal",
                "Comparativos"
            ],
            icons=[
                "house-fill",
                "mortarboard-fill", 
                "geo-alt-fill",
                "graph-up",
                "bar-chart-fill"
            ],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f0f2f6"},
                "icon": {"color": "#1f77b4", "font-size": "18px"}, 
                "nav-link": {
                    "color": "#262730",
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#1f77b4",
                    "background-color": "transparent"
                },
                "nav-link-selected": {"background-color": "#1f77b4", "color": "white"},
            }
        )
        
        st.markdown("---")
        
        # # Informações adicionais
        # st.markdown("""
        # <div style="padding: 1rem; background: #f8f9fa; border-radius: 8px; margin-top: 1rem;">
        #     <h4 style="color: #1f77b4; margin: 0 0 0.5rem 0;">📊 Sobre o Projeto</h4>
        #     <p style="font-size: 0.8rem; color: #666; margin: 0;">
        #         Este aplicativo analisa o fluxo de formação de professores através do CEFOPE, 
        #         fornecendo insights sobre a educação brasileira.
        #     </p>
        # </div>
        # """, unsafe_allow_html=True)
        
        # # Status do projeto
        # st.markdown("""
        # <div style="padding: 1rem; background: #e8f5e8; border-radius: 8px; margin-top: 1rem;">
        #     <h4 style="color: #28a745; margin: 0 0 0.5rem 0;">✅ Status</h4>
        #     <p style="font-size: 0.8rem; color: #666; margin: 0;">
        #         <strong>Versão:</strong> 1.0.0<br>
        #         <strong>Última atualização:</strong> Agosto 2025<br>
        #         <strong>Status:</strong> Em desenvolvimento
        #     </p>
        # </div>
        # """, unsafe_allow_html=True)
    
    return selected_page
