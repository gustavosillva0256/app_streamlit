"""
Página principal do Dashboard
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def render_dashboard():
    """Renderiza a página principal do dashboard"""
    
    st.title("🏠 Dashboard Principal - CEFOPE")
    st.markdown("Visão geral dos indicadores de formação de professores")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total de Professores Formados",
            value="12.847",
            delta="+5.2%",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Cursos Ativos",
            value="156",
            delta="+12",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Instituições Parceiras",
            value="89",
            delta="+3",
            delta_color="normal"
        )
    
    with col4:
        st.metric(
            label="Taxa de Conclusão",
            value="87.3%",
            delta="+2.1%",
            delta_color="normal"
        )
    
    st.markdown("---")
    
    # Gráficos principais
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Evolução da Formação por Ano")
        
        # Dados simulados para demonstração
        anos = [2020, 2021, 2022, 2023, 2024, 2025]
        formados = [850, 920, 1100, 1250, 1380, 1500]
        
        fig = px.line(
            x=anos, 
            y=formados,
            title="Professores Formados por Ano",
            labels={"x": "Ano", "y": "Quantidade"},
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Distribuição por Área de Conhecimento")
        
        areas = ["Matemática", "Português", "História", "Geografia", "Ciências", "Artes", "Educação Física"]
        quantidades = [25, 22, 18, 15, 12, 5, 3]
        
        fig = px.pie(
            values=quantidades,
            names=areas,
            title="Distribuição por Área",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Mapa de calor de regiões
    st.markdown("---")
    st.subheader("🗺️ Distribuição Geográfica por Região")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Dados simulados por região
        regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
        formados_regiao = [850, 2100, 1200, 4500, 3200]
        
        fig = px.bar(
            x=regioes,
            y=formados_regiao,
            title="Professores Formados por Região",
            labels={"x": "Região", "y": "Quantidade"},
            color=formados_regiao,
            color_continuous_scale="Blues"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Indicadores de qualidade
    st.markdown("---")
    st.subheader("⭐ Indicadores de Qualidade")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #e3f2fd; border-radius: 8px;">
            <h4 style="color: #1976d2; margin: 0;">📚 Satisfação dos Alunos</h4>
            <h2 style="color: #1976d2; margin: 0.5rem 0;">4.7/5.0</h2>
            <p style="margin: 0; color: #666;">Excelente avaliação</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #e8f5e8; border-radius: 8px;">
            <h4 style="color: #388e3c; margin: 0;">🎓 Taxa de Empregabilidade</h4>
            <h2 style="color: #388e3c; margin: 0.5rem 0;">94.2%</h2>
            <p style="margin: 0; color: #666;">Alta inserção no mercado</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #fff3e0; border-radius: 8px;">
            <h4 style="color: #f57c00; margin: 0;">🏆 Reconhecimento MEC</h4>
            <h2 style="color: #f57c00; margin: 0.5rem 0;">A+</h2>
            <p style="margin: 0; color: #666;">Máxima avaliação</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Informações sobre o CEFOPE
    st.markdown("---")
    st.subheader("ℹ️ Sobre o CEFOPE")
    
    st.markdown("""
    O **Centro de Formação de Professores (CEFOPE)** é uma instituição dedicada à formação 
    e capacitação de educadores em todo o Brasil. Nossa missão é contribuir para a 
    melhoria da qualidade da educação através de programas de formação inicial e continuada 
    que atendam às necessidades do sistema educacional brasileiro.
    
    **Principais objetivos:**
    - Formar professores qualificados para a educação básica
    - Promover a formação continuada de educadores em serviço
    - Desenvolver pesquisas e inovações na área educacional
    - Contribuir para a melhoria dos indicadores educacionais do país
    """)
