"""
Página do Dashboard Principal - CEFOPE
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def render_dashboard():
    st.markdown("## 🏠 Dashboard Principal - CEFOPE")
    st.markdown("---")
    
    # Seção de introdução e bases de dados
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; margin-bottom: 2rem; color: white;">
        <h3 style="color: white; margin: 0 0 1rem 0;">📚 Sobre o Projeto</h3>
        <p style="font-size: 1.1rem; margin: 0 0 1rem 0; line-height: 1.6;">
            <strong>Fluxo de Formação de Professores no Espírito Santo</strong><br>
            Monitoramento, análise e previsão de indicadores da formação continuada através do CEFOPE.
        </p>
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px;">
            <h4 style="color: white; margin: 0 0 0.5rem 0;">🗄️ Bases de Dados Utilizadas</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; font-size: 0.9rem;">
                <div>
                    <strong>🏛️ INEP:</strong> Censo Escolar, Educacenso, Sinopse Estatística
                </div>
                <div>
                    <strong>🏢 SEDU:</strong> Relatórios públicos, programas CEFOPE
                </div>
                <div>
                    <strong>🧪 Dados Simulados:</strong> Desenvolvimento e testes
                </div>
                <div>
                    <strong>🔒 Conformidade:</strong> LGPD - apenas dados agregados
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas principais
    st.markdown("### 📊 Métricas Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total de Professores (2024)",
            value="53.200",
            delta="+1.400",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Formações Realizadas",
            value="2.120",
            delta="+120",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Taxa de Crescimento",
            value="2.7%",
            delta="+0.3%",
            delta_color="normal"
        )
    
    with col4:
        st.metric(
            label="Municípios Atendidos",
            value="78",
            delta="0",
            delta_color="off"
        )
    
    st.markdown("---")
    
    # Gráficos principais
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Evolução Temporal")
        
        # Dados simulados para evolução
        anos = list(range(2018, 2025))
        professores = [45000, 46500, 47800, 49200, 50500, 51800, 53000, 54200]
        formacoes = [1200, 1350, 1480, 1620, 1750, 1880, 2000, 2120]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=anos, y=professores,
            mode='lines+markers',
            name='Total de Professores',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        fig.add_trace(go.Scatter(
            x=anos, y=formacoes,
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
            height=400,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🥧 Distribuição por Área")
        
        # Dados simulados para distribuição
        areas = ['Matemática', 'Português', 'História', 'Geografia', 'Ciências', 'Artes', 'Educação Física']
        valores = [25, 22, 18, 15, 12, 5, 3]
        
        fig = px.pie(
            values=valores,
            names=areas,
            title="Distribuição de Formações por Área do Conhecimento",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Gráfico de barras para dados regionais
    st.markdown("### 📍 Dados por Região")
    
    regioes = ['Metropolitana', 'Norte', 'Sul', 'Caparaó', 'Central']
    professores_regiao = [18500, 12500, 9800, 6800, 5600]
    formacoes_regiao = [680, 420, 320, 240, 200]
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Professores por Região', 'Formações por Região'),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )
    
    fig.add_trace(
        go.Bar(x=regioes, y=professores_regiao, name='Professores', marker_color='#1f77b4'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=regioes, y=formacoes_regiao, name='Formações', marker_color='#ff7f0e'),
        row=1, col=2
    )
    
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Indicadores de qualidade
    st.markdown("### 🎯 Indicadores de Qualidade")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #e8f5e8; border-radius: 10px;">
            <h4 style="color: #28a745; margin: 0;">📚 Taxa de Conclusão</h4>
            <h2 style="color: #28a745; margin: 0.5rem 0;">89.5%</h2>
            <p style="margin: 0; color: #666;">Meta: 90%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #fff3cd; border-radius: 10px;">
            <h4 style="color: #856404; margin: 0;">⭐ Satisfação</h4>
            <h2 style="color: #856404; margin: 0.5rem 0;">4.2/5.0</h2>
            <p style="margin: 0; color: #666;">Meta: 4.0/5.0</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #d1ecf1; border-radius: 10px;">
            <h4 style="color: #0c5460; margin: 0;">🎯 Aplicabilidade</h4>
            <h2 style="color: #0c5460; margin: 0.5rem 0;">87.3%</h2>
            <p style="margin: 0; color: #666;">Meta: 85%</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Seção de próximos passos
    st.markdown("### 🚀 Próximos Passos do Projeto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔄 Em Desenvolvimento:**
        - Integração com APIs oficiais do INEP
        - Pipeline de dados automatizado
        - Validação de qualidade em tempo real
        - Cache inteligente de dados
        """)
    
    with col2:
        st.markdown("""
        **🚀 Futuras Expansões:**
        - Dashboard preditivo com ML
        - Indicadores de impacto educacional
        - Mapas interativos por região
        - Relatórios automatizados
        """)
    
    # Informações técnicas sobre as bases de dados
    st.markdown("---")
    st.markdown("### 📋 Informações Técnicas das Bases de Dados")
    
    # Criar tabs para organizar as informações
    tab1, tab2, tab3 = st.tabs(["🏛️ INEP", "🏢 SEDU", "🧪 Dados Simulados"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Instituto Nacional de Estudos e Pesquisas Educacionais (INEP)**
            
            📊 **Censo Escolar**
            - Dados sobre escolas, professores e infraestrutura
            - Informações demográficas e geográficas
            - Estatísticas por município e região
            - Frequência: Anual
            
            📈 **Educacenso**
            - Dados detalhados sobre matrículas
            - Informações sobre docentes e gestores
            - Indicadores de qualidade educacional
            - Frequência: Anual
            
            📋 **Sinopse Estatística**
            - Resumos estatísticos consolidados
            - Séries históricas de indicadores
            - Comparações regionais e temporais
            - Frequência: Anual
            """)
        
        with col2:
            st.markdown("""
            **🔗 Acesso:**
            - Portal de dados abertos
            - APIs oficiais
            - Downloads diretos
            
            **📁 Formatos:**
            - CSV, JSON, Excel
            - Relatórios em PDF
            """)
    
    with tab2:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Secretaria de Estado da Educação (SEDU)**
            
            📋 **Relatórios Públicos**
            - Relatórios de gestão e prestação de contas
            - Dados sobre programas de formação continuada
            - Estatísticas de cursos e capacitações
            - Frequência: Trimestral/Anual
            
            🎯 **Programas CEFOPE**
            - Dados sobre cursos oferecidos
            - Informações sobre participantes
            - Metas e resultados alcançados
            - Frequência: Trimestral
            
            📊 **Indicadores de Desempenho**
            - Taxa de conclusão dos cursos
            - Satisfação dos participantes
            - Impacto na prática pedagógica
            - Frequência: Trimestral
            """)
        
        with col2:
            st.markdown("""
            **🔗 Acesso:**
            - Relatórios públicos
            - Portal da transparência
            - Solicitações via LAI
            
            **📁 Formatos:**
            - PDF, Excel
            - Dados estruturados
            """)
    
    with tab3:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Dados Simulados para Desenvolvimento**
            
            🔬 **Propósito:**
            - Validação de funcionalidades
            - Testes de performance
            - Demonstração de capacidades
            - Desenvolvimento iterativo
            
            📊 **Estrutura:**
            - Dados temporais (2018-2025)
            - Informações regionais (78 municípios do ES)
            - Múltiplas modalidades de formação
            - Indicadores de qualidade e impacto
            
            🔒 **Conformidade LGPD:**
            - Apenas dados agregados
            - Nenhuma informação individual
            - Foco em estatísticas públicas
            """)
        
        with col2:
            st.markdown("""
            **📅 Atualização:**
            - Em tempo real
            
            **📁 Formatos:**
            - JSON estruturado
            - Pandas DataFrames
            - APIs internas
            """)
    
    # Metadados resumidos
    st.markdown("---")
    st.markdown("### 📊 Metadados das Bases de Dados")
    
    metadados_resumo = pd.DataFrame({
        'Campo': ['ano', 'municipio', 'regiao', 'modalidade', 'area_conhecimento', 'participantes', 'carga_horaria'],
        'Tipo': ['Integer', 'String', 'String', 'String', 'String', 'Integer', 'Integer'],
        'Descrição': ['Ano de referência', 'Nome do município', 'Região geográfica', 'Tipo de formação', 'Área do conhecimento', 'Número de participantes', 'Carga horária em horas'],
        'Fonte': ['INEP', 'INEP', 'INEP', 'SEDU', 'SEDU', 'SEDU', 'SEDU']
    })
    
    st.dataframe(metadados_resumo, use_container_width=True)
    
    st.markdown("---")
    st.markdown("""
    <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; text-align: center;">
        <p style="margin: 0; color: #666;">
            <strong>📚 CEFOPE - Centro de Formação Continuada dos Profissionais da Educação</strong><br>
            Projeto acadêmico desenvolvido por Gustavo Pereira para análise da educação brasileira
        </p>
    </div>
    """, unsafe_allow_html=True)
