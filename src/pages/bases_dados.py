"""
Página de Bases de Dados - CEFOPE
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def render_bases_dados():
    st.markdown("## 📚 Bases de Dados Utilizadas")
    st.markdown("---")
    
    # Introdução
    st.markdown("""
    <div style="background: #f0f8ff; padding: 1rem; border-radius: 8px; border-left: 4px solid #1f77b4;">
        <h4 style="color: #1f77b4; margin: 0 0 0.5rem 0;">ℹ️ Sobre as Bases de Dados</h4>
        <p style="margin: 0; color: #333;">
            Este projeto utiliza múltiplas fontes de dados para analisar o fluxo de formação de professores no Espírito Santo,
            garantindo transparência e conformidade com a LGPD.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs para organizar as diferentes bases
    tab1, tab2, tab3, tab4 = st.tabs(["🏛️ INEP", "🏢 SEDU", "🧪 Dados Simulados", "📊 Metadados"])
    
    with tab1:
        st.markdown("### 🏛️ Instituto Nacional de Estudos e Pesquisas Educacionais (INEP)")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Principais bases utilizadas:**
            
            📊 **Censo Escolar**
            - Dados sobre escolas, professores e infraestrutura
            - Informações demográficas e geográficas
            - Estatísticas por município e região
            
            📈 **Educacenso**
            - Dados detalhados sobre matrículas
            - Informações sobre docentes e gestores
            - Indicadores de qualidade educacional
            
            📋 **Sinopse Estatística**
            - Resumos estatísticos consolidados
            - Séries históricas de indicadores
            - Comparações regionais e temporais
            """)
        
        with col2:
            # Gráfico de exemplo com dados do INEP
            st.markdown("**Exemplo de Dados INEP:**")
            
            # Dados simulados para demonstração
            anos = list(range(2018, 2025))
            professores_es = [45000, 46500, 47800, 49200, 50500, 51800, 53000, 54200]
            formacoes_es = [1200, 1350, 1480, 1620, 1750, 1880, 2000, 2120]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=anos, y=professores_es,
                mode='lines+markers',
                name='Total de Professores',
                line=dict(color='#1f77b4', width=3),
                marker=dict(size=8)
            ))
            fig.add_trace(go.Scatter(
                x=anos, y=formacoes_es,
                mode='lines+markers',
                name='Formações Realizadas',
                line=dict(color='#ff7f0e', width=3),
                marker=dict(size=8),
                yaxis='y2'
            ))
            
            fig.update_layout(
                title="Evolução de Professores e Formações no ES",
                xaxis_title="Ano",
                yaxis_title="Total de Professores",
                yaxis2=dict(title="Formações Realizadas", overlaying='y', side='right'),
                height=300,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### 🏢 Secretaria de Estado da Educação (SEDU)")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Dados institucionais utilizados:**
            
            📋 **Relatórios Públicos**
            - Relatórios de gestão e prestação de contas
            - Dados sobre programas de formação continuada
            - Estatísticas de cursos e capacitações
            
            🎯 **Programas CEFOPE**
            - Dados sobre cursos oferecidos
            - Informações sobre participantes
            - Metas e resultados alcançados
            
            📊 **Indicadores de Desempenho**
            - Taxa de conclusão dos cursos
            - Satisfação dos participantes
            - Impacto na prática pedagógica
            """)
        
        with col2:
            st.markdown("**Exemplo de Dados SEDU:**")
            
            # Dados simulados para demonstração
            modalidades = ['Presencial', 'Híbrido', 'EAD']
            participantes = [45, 30, 25]
            satisfacao = [4.2, 4.0, 3.8]
            
            fig = px.pie(
                values=participantes,
                names=modalidades,
                title="Distribuição por Modalidade",
                color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
            )
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### 🧪 Dados Simulados para Testes")
        
        st.markdown("""
        **Propósito dos dados simulados:**
        
        🔬 **Desenvolvimento e Testes**
        - Validação de funcionalidades
        - Testes de performance
        - Demonstração de capacidades
        
        📊 **Estrutura dos Dados Simulados**
        - Dados temporais (2018-2025)
        - Informações regionais (78 municípios do ES)
        - Múltiplas modalidades de formação
        - Indicadores de qualidade e impacto
        """)
        
        # Exemplo de dados simulados
        st.markdown("**Exemplo de Estrutura de Dados:**")
        
        # Criar dados simulados de exemplo
        dados_exemplo = pd.DataFrame({
            'Município': ['Vitória', 'Vila Velha', 'Serra', 'Linhares', 'Cachoeiro'],
            'Região': ['Metropolitana', 'Metropolitana', 'Metropolitana', 'Norte', 'Sul'],
            'Professores_2018': [5200, 4800, 4500, 3200, 3800],
            'Professores_2024': [5800, 5300, 5000, 3600, 4200],
            'Formações_2024': [180, 165, 150, 110, 130],
            'Taxa_Conclusao': [0.92, 0.89, 0.91, 0.87, 0.90]
        })
        
        st.dataframe(dados_exemplo, use_container_width=True)
        
        # Gráfico de evolução por região
        regioes = ['Metropolitana', 'Norte', 'Sul', 'Caparaó', 'Central']
        crescimento = [12.5, 15.2, 13.8, 14.1, 16.3]
        
        fig = px.bar(
            x=regioes,
            y=crescimento,
            title="Crescimento de Professores por Região (2018-2024)",
            color=crescimento,
            color_continuous_scale='Blues'
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("### 📊 Metadados e Documentação")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Informações Técnicas:**
            
            📅 **Frequência de Atualização**
            - Censo Escolar: Anual
            - Educacenso: Anual
            - Dados SEDU: Trimestral
            - Dados Simulados: Em tempo real
            
            🔒 **Conformidade LGPD**
            - Apenas dados agregados
            - Nenhuma informação individual
            - Foco em estatísticas públicas
            
            📁 **Formatos Suportados**
            - CSV, JSON, Excel
            - APIs quando disponíveis
            - Relatórios em PDF
            """)
        
        with col2:
            st.markdown("""
            **Estrutura de Dados:**
            
            🗂️ **Dimensões Principais**
            - Temporal (Ano, Mês, Trimestre)
            - Geográfica (Município, Região, Estado)
            - Categórica (Modalidade, Área, Nível)
            
            📊 **Indicadores Calculados**
            - Taxa de crescimento
            - Distribuições percentuais
            - Médias e medianas
            - Correlações e tendências
            """)
        
        # Tabela de metadados
        st.markdown("**Tabela de Metadados:**")
        
        metadados = pd.DataFrame({
            'Campo': ['ano', 'municipio', 'regiao', 'modalidade', 'area_conhecimento', 'participantes', 'carga_horaria'],
            'Tipo': ['Integer', 'String', 'String', 'String', 'String', 'Integer', 'Integer'],
            'Descrição': ['Ano de referência', 'Nome do município', 'Região geográfica', 'Tipo de formação', 'Área do conhecimento', 'Número de participantes', 'Carga horária em horas'],
            'Fonte': ['INEP', 'INEP', 'INEP', 'SEDU', 'SEDU', 'SEDU', 'SEDU']
        })
        
        st.dataframe(metadados, use_container_width=True)
    
    # Seção de próximos passos
    st.markdown("---")
    st.markdown("""
    <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #28a745;">
        <h4 style="color: #28a745; margin: 0 0 0.5rem 0;">🚀 Próximos Passos</h4>
        <ul style="margin: 0; color: #333;">
            <li>Integração com APIs oficiais do INEP</li>
            <li>Desenvolvimento de pipeline de dados automatizado</li>
            <li>Implementação de validação de qualidade dos dados</li>
            <li>Criação de dashboard preditivo com machine learning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
