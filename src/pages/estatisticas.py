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
    
    st.title("🗺️ Estatísticas por Região - ES")
    st.markdown("Análise geográfica da educação no Espírito Santo - Dados Reais 2024")
    
    # Carregar dados reais
    from services.data_service import DataService
    data_service = DataService()
    
    # Carregar dados
    municipios_df = data_service.get_data("municipios")
    escolas_df = data_service.get_data("escolas")
    cursos_df = data_service.get_data("cursos_tecnicos")
    
    # Seleção de região
    st.subheader("🔍 Filtros de Análise")
    
    # Seletor de região
    regioes = ["Todas", "Norte", "Sul", "Central", "Metropolitana"]
    regiao_selecionada = st.selectbox(
        "Região",
        regioes,
        key="regiao_estatisticas"
    )
    
    # Seleção de município
    st.subheader("🔍 Seleção de Município")
    
    if municipios_df is not None:
        # Ordenar municípios por número de professores
        municipios_ordenados = municipios_df.sort_values('Total_Professores', ascending=False)
        municipios_lista = ["Todos os Municípios"] + municipios_ordenados['Municipio'].tolist()
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            municipio_selecionado = st.selectbox(
                "Município",
                municipios_lista,
                key="municipio_estatisticas"
            )
        
        with col2:
            # Filtro por dependência
            dependencia_df = data_service.get_data("dependencia")
            if dependencia_df is not None:
                dependencias = ["Todas"] + dependencia_df['Dependencia'].tolist()
                dependencia_selecionada = st.selectbox(
                    "Dependência Administrativa",
                    dependencias,
                    key="dependencia_estatisticas"
                )
            else:
                dependencia_selecionada = "Todas"
    else:
        st.info("Carregando dados dos municípios...")
        municipio_selecionado = "Todos os Municípios"
        dependencia_selecionada = "Todas"
    
    st.markdown("---")
    
    # Aplicar filtros aos dados
    if municipios_df is not None:
        # Filtrar por município selecionado
        if municipio_selecionado != "Todos os Municípios":
            municipios_filtrados = municipios_df[municipios_df['Municipio'] == municipio_selecionado].copy()
        else:
            municipios_filtrados = municipios_df.copy()
        
        # Filtrar por dependência se aplicável
        if dependencia_selecionada != "Todas" and escolas_df is not None:
            # Filtrar escolas por dependência
            escolas_filtradas = escolas_df[escolas_df['TP_DEPENDENCIA_NOME'] == dependencia_selecionada]
            if not escolas_filtradas.empty:
                # Recalcular dados dos municípios baseado nas escolas filtradas
                municipios_filtrados = escolas_filtradas.groupby('NO_MUNICIPIO').agg({
                    'TOTAL_PROFESSORES': 'sum',
                    'TOTAL_MATRICULAS': 'sum',
                    'TOTAL_TURMAS': 'sum',
                    'CO_ENTIDADE': 'count'
                }).reset_index()
                municipios_filtrados.columns = ['Municipio', 'Total_Professores', 'Total_Matriculas', 'Total_Turmas', 'Total_Escolas']
        
        # Mostrar informações do filtro aplicado
        if municipio_selecionado != "Todos os Municípios" or dependencia_selecionada != "Todas":
            st.info(f"🔍 Filtros aplicados: Município = {municipio_selecionado}, Dependência = {dependencia_selecionada}")
    
    # Visão geral dos municípios
    st.subheader("📊 Visão Geral dos Municípios do ES")
    
    if municipios_df is not None:
        # Calcular métricas gerais usando dados filtrados
        total_professores = int(municipios_filtrados['Total_Professores'].sum())
        total_escolas = int(municipios_filtrados['Total_Escolas'].sum())
        total_matriculas = int(municipios_filtrados['Total_Matriculas'].sum())
        total_municipios = len(municipios_filtrados)
        
        # Métricas gerais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total de Professores",
                value=f"{total_professores:,}",
                delta="Dados INEP 2024",
                delta_color="normal"
            )
        
        with col2:
            st.metric(
                label="Total de Escolas",
                value=f"{total_escolas:,}",
                delta="Espírito Santo",
                delta_color="normal"
            )
        
        with col3:
            st.metric(
                label="Total de Matrículas",
                value=f"{total_matriculas:,}",
                delta="Educação Básica",
                delta_color="normal"
            )
        
        with col4:
            st.metric(
                label="Municípios Atendidos",
                value=f"{total_municipios}",
                delta="100% do ES",
                delta_color="normal"
            )
    else:
        st.info("Carregando dados dos municípios...")
    
    # Gráficos por município
    st.markdown("---")
    st.subheader("📈 Análise por Município")
    
    if municipios_df is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            # Top 15 municípios por número de professores (usando dados filtrados)
            top_municipios = municipios_filtrados.nlargest(15, 'Total_Professores')
            
            fig = px.bar(
                top_municipios,
                x="Total_Professores",
                y="Municipio",
                orientation='h',
                title="Top 15 Municípios por Número de Professores",
                color="Total_Professores",
                color_continuous_scale="Blues",
                labels={"Total_Professores": "Número de Professores", "Municipio": "Município"}
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=500
            )
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Distribuição de escolas por município (usando dados filtrados)
            top_escolas = municipios_filtrados.nlargest(15, 'Total_Escolas')
            
            fig = px.bar(
                top_escolas,
                x="Total_Escolas",
                y="Municipio",
                orientation='h',
                title="Top 15 Municípios por Número de Escolas",
                color="Total_Escolas",
                color_continuous_scale="Greens",
                labels={"Total_Escolas": "Número de Escolas", "Municipio": "Município"}
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=500
            )
            st.plotly_chart(fig, width='stretch')
    else:
        st.info("Carregando dados dos municípios...")
    
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
    st.plotly_chart(fig, width='stretch')
    
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
    st.plotly_chart(fig, width='stretch')
    
    # Tabela de dados por estado
    st.subheader("📋 Dados Detalhados por Estado")
    st.dataframe(
        df_estados.style.format({
            "Taxa_Conclusao": "{:.1f}%"
        }),
        width='stretch'
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
        st.plotly_chart(fig, width='stretch')
    
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
        st.plotly_chart(fig, width='stretch')
    
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
