"""
Componente de cabeçalho do aplicativo
"""

import streamlit as st

def render_header():
    """Renderiza o cabeçalho principal do aplicativo"""
    
    # Cabeçalho principal
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #1f77b4, #ff7f0e); border-radius: 10px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; font-size: 2.5rem;">📚 CEFOPE</h1>
        <h2 style="color: white; margin: 0; font-size: 1.5rem;">Fluxo de Formação de Professores</h2>
        <p style="color: white; margin: 0.5rem 0 0 0; font-size: 1rem;">Análise e Visualização de Dados Educacionais</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Informações do desenvolvedor
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #f0f2f6; border-radius: 8px; border-left: 4px solid #1f77b4;">
            <p style="margin: 0; font-weight: bold; color: #1f77b4;">👨‍💻 Desenvolvedor: Gustavo Pereira</p>
            <p style="margin: 0.5rem 0 0 0; color: #666;">Projeto Acadêmico - Análise de Dados Educacionais</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
