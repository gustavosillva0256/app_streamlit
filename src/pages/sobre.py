"""
Página Sobre o Sistema - Sistema de Análise Educacional - ES
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def render_sobre():
    """Renderiza a página sobre o sistema"""
    
    st.title("ℹ️ Sobre o Sistema")
    st.markdown("Conheça o Sistema de Análise Educacional do Espírito Santo")
    st.markdown("---")
    
    # 1. VISÃO GERAL DO PROJETO
    st.markdown("## 🎯 Visão Geral do Projeto")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **O Sistema de Análise Educacional do Espírito Santo** é uma plataforma de visualização 
        e análise de dados educacionais que utiliza informações oficiais do Instituto Nacional 
        de Estudos e Pesquisas Educacionais (INEP) para fornecer insights sobre a educação 
        no estado do Espírito Santo.
        
        ### 🎯 **Objetivos Principais:**
        
        - **📊 Visualização de Dados**: Transformar dados complexos do INEP em visualizações 
        interativas e compreensíveis
        - **🔍 Análise Comparativa**: Permitir comparações entre municípios, regiões e 
        indicadores educacionais
        - **📈 Monitoramento**: Acompanhar evolução temporal dos indicadores educacionais
        - **📋 Transparência**: Disponibilizar informações educacionais de forma transparente 
        e acessível
        
        ### 👥 **Público-Alvo:**
        
        - Gestores educacionais
        - Pesquisadores em educação
        - Estudantes e acadêmicos
        - Profissionais da área educacional
        - Cidadãos interessados em educação
        """)
    
    with col2:
        # Gráfico de exemplo - distribuição de escolas por dependência
        st.markdown("**📊 Exemplo de Análise:**")
        
        dependencias = ['Estadual', 'Municipal', 'Federal', 'Privada']
        valores = [45.2, 32.8, 8.5, 13.5]
        
        fig = px.pie(
            values=valores,
            names=dependencias,
            title="Distribuição de Escolas por Dependência (ES)",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(height=300, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # 2. METODOLOGIA DE ANÁLISE
    st.markdown("## 🔬 Metodologia de Análise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📁 **Processamento de Dados:**
        
        **1. Coleta e Limpeza**
        - Download automático dos microdados do INEP
        - Filtros específicos para o Espírito Santo
        - Remoção de inconsistências e valores nulos
        - Validação de integridade dos dados
        
        **2. Transformação**
        - Agregação por município e região
        - Cálculo de indicadores educacionais
        - Normalização de dados para comparação
        - Criação de métricas derivadas
        
        **3. Análise**
        - Estatísticas descritivas
        - Análise de correlações
        - Comparações temporais e regionais
        - Identificação de tendências
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 **Técnicas Utilizadas:**
        
        **📊 Análise Estatística:**
        - Estatísticas descritivas (média, mediana, desvio padrão)
        - Análise de distribuição dos dados
        - Cálculo de percentis e quartis
        - Correlações entre variáveis
        
        **📈 Análise Temporal:**
        - Séries temporais de indicadores
        - Identificação de tendências
        - Análise de sazonalidade
        - Projeções baseadas em histórico
        
        **🗺️ Análise Geográfica:**
        - Comparações entre municípios
        - Análise regional
        - Identificação de disparidades
        - Mapeamento de indicadores
        """)
    
    st.markdown("---")
    
    # 3. PRINCIPAIS FUNCIONALIDADES
    st.markdown("## 🚀 Principais Funcionalidades")
    
    # Cards com funcionalidades
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #28a745; margin: 0 0 1rem 0;">📊 Dashboard Principal</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #333;">
                <li>Métricas em tempo real</li>
                <li>Indicadores principais</li>
                <li>Visão geral do estado</li>
                <li>Estatísticas descritivas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #fff3cd; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #856404; margin: 0 0 1rem 0;">📈 Análises Temporais</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #333;">
                <li>Evolução histórica</li>
                <li>Tendências identificadas</li>
                <li>Projeções futuras</li>
                <li>Análise sazonal</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: #d1ecf1; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #0c5460; margin: 0 0 1rem 0;">🗺️ Análise Regional</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #333;">
                <li>Comparações municipais</li>
                <li>Disparidades regionais</li>
                <li>Rankings educacionais</li>
                <li>Indicadores por localização</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Mais funcionalidades
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #f8d7da; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #721c24; margin: 0 0 1rem 0;">🔄 Comparativos</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #333;">
                <li>Benchmarks nacionais</li>
                <li>Comparações temporais</li>
                <li>Análise de gaps</li>
                <li>Recomendações estratégicas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #e2e3e5; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #383d41; margin: 0 0 1rem 0;">🎓 Formação de Professores</h4>
            <ul style="margin: 0; padding-left: 1.5rem; color: #333;">
                <li>Cursos técnicos disponíveis</li>
                <li>Distribuição por área</li>
                <li>Ofertas por município</li>
                <li>Análise de demanda</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 4. TECNOLOGIAS UTILIZADAS
    st.markdown("## 🛠️ Tecnologias Utilizadas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🐍 **Backend e Análise:**
        
        **Python 3.8+**
        - Linguagem principal do projeto
        - Biblioteca rica para análise de dados
        
        **Pandas & NumPy**
        - Manipulação e análise de dados
        - Processamento de grandes volumes
        - Operações estatísticas
        
        **Plotly**
        - Visualizações interativas
        - Gráficos dinâmicos
        - Dashboards responsivos
        """)
    
    with col2:
        st.markdown("""
        ### 🌐 **Frontend e Deploy:**
        
        **Streamlit**
        - Framework web para Python
        - Interface interativa
        - Deploy simplificado
        
        **Streamlit Cloud**
        - Hospedagem gratuita
        - Deploy automático
        - Escalabilidade
        
        **Git & GitHub**
        - Controle de versão
        - Colaboração
        - CI/CD integrado
        """)
    
    # Stack visual
    st.markdown("---")
    st.markdown("### 🏗️ Arquitetura do Sistema")
    
    # Diagrama simples da arquitetura
    st.markdown("""
    <div style="background: #f8f9fa; padding: 2rem; border-radius: 10px; text-align: center;">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
            <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px;">
                <h5 style="margin: 0; color: #1976d2;">📊 Dados INEP</h5>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Microdados Oficiais</p>
            </div>
            <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px;">
                <h5 style="margin: 0; color: #7b1fa2;">🔧 Processamento</h5>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Python + Pandas</p>
            </div>
            <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                <h5 style="margin: 0; color: #388e3c;">📱 Interface</h5>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Streamlit Web App</p>
            </div>
        </div>
        <div style="background: #fff3e0; padding: 1rem; border-radius: 8px;">
            <h5 style="margin: 0; color: #f57c00;">☁️ Deploy</h5>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Streamlit Cloud + GitHub</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 5. FONTE DOS DADOS
    st.markdown("## 📚 Fonte dos Dados")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🏛️ **INEP - Instituto Nacional de Estudos e Pesquisas Educacionais**
        
        **📊 Censo Escolar 2024:**
        - Dados oficiais mais recentes
        - 3.970 escolas do Espírito Santo
        - 78 municípios cobertos
        - Informações sobre professores, matrículas e turmas
        
        **📈 Microdados da Educação Básica:**
        - Dados detalhados por escola
        - Classificação por dependência administrativa
        - Informações de localização (urbana/rural)
        - Dados de infraestrutura
        
        **🎓 Suplemento de Cursos Técnicos:**
        - 584 cursos técnicos no ES
        - Informações por área de conhecimento
        - Dados de matrículas e ofertas
        - Distribuição municipal
        """)
    
    with col2:
        st.markdown("""
        ### 🔒 **Qualidade e Conformidade:**
        
        **✅ Dados Oficiais:**
        - Fonte governamental confiável
        - Metodologia padronizada
        - Validação institucional
        
        **🛡️ Conformidade LGPD:**
        - Apenas dados agregados
        - Nenhuma informação individual
        - Transparência na fonte
        - Dados públicos oficiais
        
        **📅 Atualização:**
        - Dados de 2024 (mais recentes)
        - Processamento em tempo real
        - Filtros específicos para ES
        - Validação automática
        """)
    
    # Estatísticas dos dados
    st.markdown("---")
    st.markdown("### 📊 Estatísticas dos Dados Processados")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Escolas Analisadas", "3.970", "100% do ES")
    
    with col2:
        st.metric("Municípios Cobertos", "78", "100% do ES")
    
    with col3:
        st.metric("Cursos Técnicos", "584", "Todas as áreas")
    
    with col4:
        st.metric("Ano dos Dados", "2024", "Mais recentes")
    
    st.markdown("---")
    
    # 6. LIMITAÇÕES E CONSIDERAÇÕES
    st.markdown("## ⚠️ Limitações e Considerações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔍 **Limitações dos Dados:**
        
        **📅 Frequência:**
        - Dados anuais (não mensais)
        - Atualização anual do INEP
        - Delay na publicação
        
        **📊 Cobertura:**
        - Apenas educação básica
        - Não inclui educação superior
        - Foco em escolas regulares
        
        **🎯 Escopo:**
        - Limitado ao Espírito Santo
        - Não inclui dados municipais específicos
        - Dados agregados por escola
        """)
    
    with col2:
        st.markdown("""
        ### 💡 **Considerações Importantes:**
        
        **📈 Interpretação:**
        - Análises baseadas em dados oficiais
        - Contexto temporal importante
        - Comparações relativas
        
        **🔄 Atualizações:**
        - Sistema atualizado anualmente
        - Dados históricos mantidos
        - Versões documentadas
        
        **🎓 Uso Acadêmico:**
        - Projeto de análise educacional
        - Foco em visualização de dados
        - Contribuição para transparência
        """)
    
    st.markdown("---")
    
    # 7. FUTURAS EXPANSÕES
    st.markdown("## 🚀 Futuras Expansões")
    
    st.markdown("""
    ### 🔮 **Roadmap do Projeto:**
    
    **📅 Curto Prazo:**
    - Integração com APIs do INEP em tempo real
    - Pipeline de dados automatizado
    - Validação de qualidade aprimorada
    
    **📈 Médio Prazo:**
    - Análise preditiva com Machine Learning
    - Mapas interativos por município
    - Relatórios automatizados
    - Comparações com outros estados
    
    **🎯 Longo Prazo:**
    - Dashboard preditivo
    - Indicadores de impacto educacional
    - API para integração externa
    - Expansão para outros estados
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="background: #f8f9fa; padding: 2rem; border-radius: 10px; text-align: center;">
        <h4 style="color: #1f77b4; margin: 0 0 1rem 0;">📚 Sistema de Análise Educacional - ES</h4>
        <p style="margin: 0; color: #666; font-size: 1.1rem;">
            Transformando dados educacionais em insights para uma educação melhor no Espírito Santo
        </p>
        <p style="margin: 1rem 0 0 0; color: #888; font-size: 0.9rem;">
            Projeto acadêmico desenvolvido para análise de dados educacionais do Brasil
        </p>
    </div>
    """, unsafe_allow_html=True)
