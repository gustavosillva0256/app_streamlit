"""
Página de estatísticas por região
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def render_estatisticas():
    """Renderiza a página de estatísticas por região"""
    
    st.title("🗺️ Estatísticas por Região - CEFOPE")
    st.markdown("Análise geográfica da formação de professores em todo o Brasil")
    
    # Seleção de região
    st.subheader("🔍 Seleção de Região")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        regiao_selecionada = st.selectbox(
            "Região",
            ["Todas", "Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
        )
    
    with col2:
        estado_selecionado = st.selectbox(
            "Estado (se aplicável)",
            ["Todos os Estados"] + [
                "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
                "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
                "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
                "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
                "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
            ]
        )
    
    st.markdown("---")
    
    # Visão geral das regiões
    st.subheader("📊 Visão Geral das Regiões")
    
    # Dados simulados por região
    regioes_data = {
        "Região": ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
        "Professores_Formados": [850, 2100, 1200, 4500, 3200],
        "Cursos_Ativos": [23, 45, 28, 89, 67],
        "Instituicoes_Parceiras": [12, 28, 18, 45, 32],
        "Taxa_Conclusao": [85.2, 88.7, 87.3, 89.1, 91.2],
        "Satisfacao_Media": [4.3, 4.5, 4.4, 4.6, 4.7]
    }
    
    df_regioes = pd.DataFrame(regioes_data)
    
    # Métricas por região
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total de Professores",
            value=f"{df_regioes['Professores_Formados'].sum():,}",
            delta="+8.5%",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Cursos Ativos",
            value=f"{df_regioes['Cursos_Ativos'].sum()}",
            delta="+15",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Instituições",
            value=f"{df_regioes['Instituicoes_Parceiras'].sum()}",
            delta="+8",
            delta_color="normal"
        )
    
    with col4:
        st.metric(
            label="Taxa Média de Conclusão",
            value=f"{df_regioes['Taxa_Conclusao'].mean():.1f}%",
            delta="+1.2%",
            delta_color="normal"
        )
    
    # Gráficos regionais
    st.markdown("---")
    st.subheader("📈 Análise Regional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Professores formados por região
        fig = px.bar(
            df_regioes,
            x="Região",
            y="Professores_Formados",
            title="Professores Formados por Região",
            color="Professores_Formados",
            color_continuous_scale="Blues",
            labels={"Professores_Formados": "Quantidade"}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Taxa de conclusão por região
        fig = px.bar(
            df_regioes,
            x="Região",
            y="Taxa_Conclusao",
            title="Taxa de Conclusão por Região (%)",
            color="Taxa_Conclusao",
            color_continuous_scale="RdYlGn",
            labels={"Taxa_Conclusao": "Taxa (%)"}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Mapa de calor de indicadores
    st.markdown("---")
    st.subheader("🔥 Mapa de Calor de Indicadores")
    
    # Criando matriz de correlação simulada
    indicadores = ["Formados", "Cursos", "Instituições", "Conclusão", "Satisfação"]
    regioes_nomes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
    
    # Dados simulados para correlação
    matriz_corr = np.array([
        [1.0, 0.8, 0.7, 0.6, 0.5],
        [0.8, 1.0, 0.9, 0.8, 0.7],
        [0.7, 0.9, 1.0, 0.8, 0.6],
        [0.6, 0.8, 0.8, 1.0, 0.9],
        [0.5, 0.7, 0.6, 0.9, 1.0]
    ])
    
    fig = px.imshow(
        matriz_corr,
        x=indicadores,
        y=regioes_nomes,
        title="Correlação entre Indicadores por Região",
        color_continuous_scale="RdBu",
        aspect="auto"
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Análise detalhada por estado (simulada)
    st.markdown("---")
    st.subheader("🏛️ Análise por Estado")
    
    # Dados simulados por estado
    estados_data = {
        "Estado": ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Bahia", "Paraná", "Rio Grande do Sul"],
        "Região": ["Sudeste", "Sudeste", "Sudeste", "Nordeste", "Sul", "Sul"],
        "Professores": [1800, 1200, 950, 850, 1100, 980],
        "Cursos": [35, 28, 22, 18, 25, 22],
        "Taxa_Conclusao": [91.2, 89.5, 88.7, 87.3, 92.1, 90.8]
    }
    
    df_estados = pd.DataFrame(estados_data)
    
    # Filtro por região se aplicável
    if regiao_selecionada != "Todas":
        df_estados = df_estados[df_estados["Região"] == regiao_selecionada]
    
    # Gráfico de barras por estado
    fig = px.bar(
        df_estados,
        x="Estado",
        y="Professores",
        title=f"Professores Formados por Estado - {regiao_selecionada}",
        color="Taxa_Conclusao",
        color_continuous_scale="RdYlGn",
        labels={"Professores": "Quantidade", "Taxa_Conclusao": "Taxa de Conclusão (%)"}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela de dados por estado
    st.subheader("📋 Dados Detalhados por Estado")
    st.dataframe(
        df_estados.style.format({
            "Taxa_Conclusao": "{:.1f}%"
        }),
        use_container_width=True
    )
    
    # Indicadores de desenvolvimento educacional
    st.markdown("---")
    st.subheader("📚 Indicadores de Desenvolvimento Educacional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # IDEB por região (simulado)
        ideb_data = {
            "Região": ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
            "IDEB_Anos_Iniciais": [4.8, 4.9, 5.1, 5.8, 6.2],
            "IDEB_Anos_Finais": [4.2, 4.3, 4.6, 5.1, 5.5]
        }
        
        df_ideb = pd.DataFrame(ideb_data)
        
        fig = px.line(
            df_ideb,
            x="Região",
            y=["IDEB_Anos_Iniciais", "IDEB_Anos_Finais"],
            title="IDEB por Região",
            labels={"value": "IDEB", "variable": "Nível"},
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Investimento em educação por região
        investimento_data = {
            "Região": ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
            "Investimento_Per_Capita": [1200, 1350, 1500, 1800, 1650]
        }
        
        df_invest = pd.DataFrame(investimento_data)
        
        fig = px.bar(
            df_invest,
            x="Região",
            y="Investimento_Per_Capita",
            title="Investimento em Educação per Capita (R$)",
            color="Investimento_Per_Capita",
            color_continuous_scale="Greens",
            labels={"Investimento_Per_Capita": "Valor (R$)"}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Análise de tendências regionais
    st.markdown("---")
    st.subheader("📈 Tendências Regionais")
    
    st.markdown("""
    **Principais observações sobre as tendências regionais:**
    
    🏆 **Sudeste**: Mantém liderança em número de formações e qualidade, com forte 
    concentração de instituições de ensino superior.
    
    🚀 **Sul**: Apresenta crescimento consistente e alta qualidade, com destaque 
    para inovação pedagógica.
    
    📈 **Nordeste**: Mostra evolução significativa, especialmente em programas 
    de formação continuada.
    
    🔄 **Centro-Oeste**: Crescimento equilibrado com foco em formação específica 
    para a região.
    
    🌱 **Norte**: Desenvolvimento em expansão com programas adaptados às 
    necessidades locais.
    
    **Fatores que influenciam as diferenças regionais:**
    - Concentração de instituições de ensino superior
    - Investimento público em educação
    - Políticas estaduais de formação docente
    - Características socioeconômicas regionais
    - Demanda por professores em cada região
    """)
