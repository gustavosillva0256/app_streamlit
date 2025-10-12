"""
Página de análises comparativas
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def render_comparativos():
    """Renderiza a página de análises comparativas"""
    
    st.title("📊 Análises Comparativas - CEFOPE")
    st.markdown("Comparações entre diferentes períodos, regiões e indicadores educacionais - Dados Reais 2024")
    
    # Carregar dados reais
    from services.data_service import DataService
    data_service = DataService()
    
    # Carregar dados
    escolas_df = data_service.get_data("escolas")
    municipios_df = data_service.get_data("municipios")
    dependencia_df = data_service.get_data("dependencia")
    localizacao_df = data_service.get_data("localizacao")
    cursos_df = data_service.get_data("cursos_tecnicos")
    
    # Seleção de tipo de comparação
    st.subheader("🔍 Tipo de Comparação")
    
    tipo_comparacao = st.selectbox(
        "Selecione o tipo de comparação",
        ["Municípios", "Dependências", "Localização", "Cursos Técnicos", "Indicadores"]
    )
    
    st.markdown("---")
    
    if tipo_comparacao == "Municípios":
        render_comparacao_municipios(municipios_df)
    elif tipo_comparacao == "Dependências":
        render_comparacao_dependencias(dependencia_df)
    elif tipo_comparacao == "Localização":
        render_comparacao_localizacao(localizacao_df)
    elif tipo_comparacao == "Cursos Técnicos":
        render_comparacao_cursos(cursos_df)
    elif tipo_comparacao == "Indicadores":
        render_comparacao_indicadores(escolas_df)

def render_comparacao_periodos():
    """Renderiza comparação entre períodos"""
    
    st.subheader("📅 Comparação entre Períodos")
    
    # Seleção de períodos
    col1, col2 = st.columns(2)
    
    with col1:
        periodo1 = st.selectbox(
            "Período 1",
            ["2015-2019", "2020-2024", "2015-2024", "2020-2025"]
        )
    
    with col2:
        periodo2 = st.selectbox(
            "Período 2",
            ["2020-2024", "2015-2019", "2020-2025", "2015-2024"]
        )
    
    # Dados simulados para comparação
    dados_periodos = {
        "Indicador": ["Matrículas", "Formações", "Cursos", "Taxa_Conclusão", "Satisfação"],
        "2015-2019": [18500, 16200, 290, 89.3, 4.3],
        "2020-2024": [31500, 28000, 495, 91.8, 4.6],
        "2015-2024": [50000, 44200, 785, 90.6, 4.5],
        "2020-2025": [39700, 35600, 616, 92.1, 4.7]
    }
    
    df_periodos = pd.DataFrame(dados_periodos)
    
    # Métricas comparativas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        crescimento_periodo1 = ((df_periodos[periodo1].iloc[0] - df_periodos[periodo1].iloc[0]) / df_periodos[periodo1].iloc[0]) * 100
        st.metric(
            label=f"Total {periodo1}",
            value=f"{df_periodos[periodo1].iloc[0]:,}",
            delta="Período base"
        )
    
    with col2:
        crescimento_periodo2 = ((df_periodos[periodo2].iloc[0] - df_periodos[periodo1].iloc[0]) / df_periodos[periodo1].iloc[0]) * 100
        st.metric(
            label=f"Total {periodo2}",
            value=f"{df_periodos[periodo2].iloc[0]:,}",
            delta=f"{crescimento_periodo2:+.1f}%",
            delta_color="normal" if crescimento_periodo2 > 0 else "inverse"
        )
    
    with col3:
        diferenca_absoluta = df_periodos[periodo2].iloc[0] - df_periodos[periodo1].iloc[0]
        st.metric(
            label="Diferença Absoluta",
            value=f"{diferenca_absoluta:+,}",
            delta="Variação"
        )
    
    with col4:
        crescimento_relativo = ((df_periodos[periodo2].iloc[0] / df_periodos[periodo1].iloc[0]) - 1) * 100
        st.metric(
            label="Crescimento Relativo",
            value=f"{crescimento_relativo:+.1f}%",
            delta="Comparação"
        )
    
    # Gráfico comparativo
    st.markdown("---")
    st.subheader("📈 Gráfico Comparativo")
    
    # Preparando dados para o gráfico
    indicadores_comp = df_periodos["Indicador"].tolist()
    valores_periodo1 = df_periodos[periodo1].tolist()
    valores_periodo2 = df_periodos[periodo2].tolist()
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name=periodo1,
        x=indicadores_comp,
        y=valores_periodo1,
        marker_color='#1f77b4'
    ))
    
    fig.add_trace(go.Bar(
        name=periodo2,
        x=indicadores_comp,
        y=valores_periodo2,
        marker_color='#ff7f0e'
    ))
    
    fig.update_layout(
        title=f"Comparação: {periodo1} vs {periodo2}",
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Análise de tendências
    st.markdown("---")
    st.subheader("📊 Análise de Tendências")
    
    # Calculando variações percentuais
    variacoes = []
    for i in range(len(indicadores_comp)):
        if valores_periodo1[i] != 0:
            variacao = ((valores_periodo2[i] - valores_periodo1[i]) / valores_periodo1[i]) * 100
            variacoes.append(variacao)
        else:
            variacoes.append(0)
    
    # Criando DataFrame de variações
    df_variacoes = pd.DataFrame({
        "Indicador": indicadores_comp,
        "Variação (%)": variacoes,
        "Tendência": ["Positiva" if v > 0 else "Negativa" if v < 0 else "Estável" for v in variacoes]
    })
    
    # Gráfico de variações
    fig = px.bar(
        df_variacoes,
        x="Indicador",
        y="Variação (%)",
        color="Tendência",
        title=f"Variação Percentual: {periodo1} → {periodo2}",
        color_discrete_map={"Positiva": "#28a745", "Negativa": "#dc3545", "Estável": "#6c757d"}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, width='stretch')
    
    # Tabela de variações
    st.subheader("📋 Resumo das Variações")
    st.dataframe(
        df_variacoes.style.format({
            "Variação (%)": "{:+.1f}%"
        }),
        width='stretch'
    )

def render_comparacao_regioes():
    """Renderiza comparação entre regiões"""
    
    st.subheader("🗺️ Comparação entre Regiões")
    
    # Seleção de regiões
    col1, col2 = st.columns(2)
    
    with col1:
        regiao1 = st.selectbox(
            "Região 1",
            ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
        )
    
    with col2:
        regiao2 = st.selectbox(
            "Região 2",
            ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"]
        )
    
    # Dados simulados por região
    dados_regioes = {
        "Indicador": ["Professores Formados", "Cursos Ativos", "Taxa de Conclusão", "Satisfação", "Empregabilidade"],
        "Norte": [850, 23, 85.2, 4.3, 92.1],
        "Nordeste": [2100, 45, 88.7, 4.5, 94.3],
        "Centro-Oeste": [1200, 28, 87.3, 4.4, 93.7],
        "Sudeste": [4500, 89, 89.1, 4.6, 95.8],
        "Sul": [3200, 67, 91.2, 4.7, 96.2]
    }
    
    df_regioes = pd.DataFrame(dados_regioes)
    
    # Métricas comparativas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label=f"{regiao1} - Formados",
            value=f"{df_regioes[regiao1].iloc[0]:,}",
            delta="Região selecionada"
        )
    
    with col2:
        st.metric(
            label=f"{regiao2} - Formados",
            value=f"{df_regioes[regiao2].iloc[0]:,}",
            delta="Região selecionada"
        )
    
    with col3:
        diferenca_formados = df_regioes[regiao2].iloc[0] - df_regioes[regiao1].iloc[0]
        st.metric(
            label="Diferença",
            value=f"{diferenca_formados:+,}",
            delta="Variação"
        )
    
    with col4:
        if df_regioes[regiao1].iloc[0] != 0:
            razao = df_regioes[regiao2].iloc[0] / df_regioes[regiao1].iloc[0]
            st.metric(
                label="Razão",
                value=f"{razao:.1f}x",
                delta="Multiplicador"
            )
    
    # Radar chart comparativo
    st.markdown("---")
    st.subheader("🎯 Radar Chart Comparativo")
    
    # Preparando dados para o radar chart
    indicadores_radar = df_regioes["Indicador"].tolist()
    valores_regiao1 = df_regioes[regiao1].tolist()
    valores_regiao2 = df_regioes[regiao2].tolist()
    
    # Normalizando valores para escala 0-100
    max_valores = [df_regioes[col].max() for col in [regiao1, regiao2]]
    valores_norm_regiao1 = [(v / max_valores[0]) * 100 for v in valores_regiao1]
    valores_norm_regiao2 = [(v / max_valores[1]) * 100 for v in valores_regiao2]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=valores_norm_regiao1,
        theta=indicadores_radar,
        fill='toself',
        name=regiao1,
        line_color='#1f77b4'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=valores_norm_regiao2,
        theta=indicadores_radar,
        fill='toself',
        name=regiao2,
        line_color='#ff7f0e'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title=f"Comparação de Indicadores: {regiao1} vs {regiao2}"
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Análise de competitividade
    st.markdown("---")
    st.subheader("🏆 Análise de Competitividade")
    
    # Calculando pontuação competitiva
    pontuacao_regiao1 = sum(valores_norm_regiao1) / len(valores_norm_regiao1)
    pontuacao_regiao2 = sum(valores_norm_regiao2) / len(valores_norm_regiao2)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem; background: #e3f2fd; border-radius: 8px;">
            <h4 style="color: #1976d2; margin: 0;">{regiao1}</h4>
            <h2 style="color: #1976d2; margin: 0.5rem 0;">{pontuacao_regiao1:.1f}/100</h2>
            <p style="margin: 0; color: #666;">Pontuação Competitiva</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem; background: #e8f5e8; border-radius: 8px;">
            <h4 style="color: #388e3c; margin: 0;">{regiao2}</h4>
            <h2 style="color: #388e3c; margin: 0.5rem 0;">{pontuacao_regiao2:.1f}/100</h2>
            <p style="margin: 0; color: #666;">Pontuação Competitiva</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Vencedor da comparação
    if pontuacao_regiao1 > pontuacao_regiao2:
        vencedor = regiao1
        diferenca_pontos = pontuacao_regiao1 - pontuacao_regiao2
    elif pontuacao_regiao2 > pontuacao_regiao1:
        vencedor = regiao2
        diferenca_pontos = pontuacao_regiao2 - pontuacao_regiao1
    else:
        vencedor = "Empate"
        diferenca_pontos = 0
    
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background: #fff3e0; border-radius: 8px; margin-top: 1rem;">
        <h4 style="color: #f57c00; margin: 0;">🏆 Resultado da Comparação</h4>
        <h3 style="color: #f57c00; margin: 0.5rem 0;">{vencedor}</h3>
        <p style="margin: 0; color: #666;">
            {'Diferença de ' + f"{diferenca_pontos:.1f} pontos" if diferenca_pontos > 0 else 'Regiões com desempenho equivalente'}
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_comparacao_programas():
    """Renderiza comparação entre programas"""
    
    st.subheader("🎓 Comparação entre Programas")
    
    # Seleção de programas
    col1, col2 = st.columns(2)
    
    with col1:
        programa1 = st.selectbox(
            "Programa 1",
            ["Licenciatura em Matemática", "Licenciatura em Português", "Pedagogia", "Formação Continuada em História"]
        )
    
    with col2:
        programa2 = st.selectbox(
            "Programa 2",
            ["Pedagogia", "Formação Continuada em História", "Licenciatura em Matemática", "Licenciatura em Português"]
        )
    
    # Dados simulados dos programas
    dados_programas = {
        "Indicador": ["Matrículas", "Concluídos", "Taxa de Conclusão", "Satisfação", "Empregabilidade"],
        "Licenciatura em Matemática": [450, 420, 93.3, 4.2, 96.2],
        "Licenciatura em Português": [380, 350, 92.1, 4.5, 94.8],
        "Pedagogia": [520, 480, 92.3, 4.7, 97.1],
        "Formação Continuada em História": [280, 250, 89.3, 4.3, 93.5]
    }
    
    df_programas = pd.DataFrame(dados_programas)
    
    # Gráfico de barras comparativo
    st.markdown("---")
    st.subheader("📊 Comparação de Indicadores")
    
    indicadores_prog = df_programas["Indicador"].tolist()
    valores_prog1 = df_programas[programa1].tolist()
    valores_prog2 = df_programas[programa2].tolist()
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name=programa1,
        x=indicadores_prog,
        y=valores_prog1,
        marker_color='#1f77b4'
    ))
    
    fig.add_trace(go.Bar(
        name=programa2,
        x=indicadores_prog,
        y=valores_prog2,
        marker_color='#ff7f0e'
    ))
    
    fig.update_layout(
        title=f"Comparação: {programa1} vs {programa2}",
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, width='stretch')

def render_comparacao_indicadores():
    """Renderiza comparação entre indicadores"""
    
    st.subheader("📈 Comparação entre Indicadores")
    
    # Seleção de indicadores
    col1, col2 = st.columns(2)
    
    with col1:
        indicador1 = st.selectbox(
            "Indicador 1",
            ["Matrículas", "Formações", "Taxa de Conclusão", "Satisfação", "Empregabilidade"]
        )
    
    with col2:
        indicador2 = st.selectbox(
            "Indicador 2",
            ["Empregabilidade", "Satisfação", "Taxa de Conclusão", "Formações", "Matrículas"]
        )
    
    # Dados simulados para correlação
    regioes_corr = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
    
    dados_correlacao = {
        "Região": regioes_corr,
        "Matrículas": [850, 2100, 1200, 4500, 3200],
        "Formações": [720, 1850, 1050, 4000, 2900],
        "Taxa de Conclusão": [85.2, 88.7, 87.3, 89.1, 91.2],
        "Satisfação": [4.3, 4.5, 4.4, 4.6, 4.7],
        "Empregabilidade": [92.1, 94.3, 93.7, 95.8, 96.2]
    }
    
    df_corr = pd.DataFrame(dados_correlacao)
    
    # Gráfico de dispersão
    st.markdown("---")
    st.subheader("🔗 Análise de Correlação")
    
    fig = px.scatter(
        df_corr,
        x=indicador1,
        y=indicador2,
        title=f"Correlação: {indicador1} vs {indicador2}",
        labels={indicador1: indicador1, indicador2: indicador2},
        color="Região",
        size="Taxa de Conclusão",
        hover_name="Região"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Coeficiente de correlação
    correlacao = df_corr[indicador1].corr(df_corr[indicador2])
    
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px; margin-top: 1rem;">
        <h4 style="color: #495057; margin: 0;">📊 Coeficiente de Correlação</h4>
        <h2 style="color: #495057; margin: 0.5rem 0;">{correlacao:.3f}</h2>
        <p style="margin: 0; color: #666;">
            {'Correlação forte' if abs(correlacao) > 0.7 else 'Correlação moderada' if abs(correlacao) > 0.3 else 'Correlação fraca'}
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_comparacao_benchmark():
    """Renderiza comparação com benchmarks externos"""
    
    st.subheader("🏆 Comparação com Benchmarks")
    
    # Seleção de benchmark
    benchmark = st.selectbox(
        "Selecione o benchmark",
        ["Média Nacional", "Top 10% das Instituições", "Padrão Internacional", "Meta CEFOPE 2030"]
    )
    
    # Dados simulados de benchmark
    dados_benchmark = {
        "Indicador": ["Taxa de Conclusão", "Satisfação dos Alunos", "Empregabilidade", "Qualidade dos Cursos"],
        "CEFOPE Atual": [91.2, 4.6, 95.8, 4.5],
        "Média Nacional": [87.3, 4.2, 92.1, 4.1],
        "Top 10%": [94.8, 4.8, 97.3, 4.7],
        "Padrão Internacional": [89.5, 4.4, 94.2, 4.3],
        "Meta CEFOPE 2030": [95.0, 4.8, 98.0, 4.8]
    }
    
    df_benchmark = pd.DataFrame(dados_benchmark)
    
    # Gráfico de radar comparativo
    st.markdown("---")
    st.subheader("🎯 Radar Chart vs Benchmark")
    
    indicadores_bench = df_benchmark["Indicador"].tolist()
    valores_cefope = df_benchmark["CEFOPE Atual"].tolist()
    valores_bench = df_benchmark[benchmark].tolist()
    
    # Normalizando valores
    max_valor = max(max(valores_cefope), max(valores_bench))
    valores_norm_cefope = [(v / max_valor) * 100 for v in valores_cefope]
    valores_norm_bench = [(v / max_valor) * 100 for v in valores_bench]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=valores_norm_cefope,
        theta=indicadores_bench,
        fill='toself',
        name='CEFOPE Atual',
        line_color='#1f77b4'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=valores_norm_bench,
        theta=indicadores_bench,
        fill='toself',
        name=benchmark,
        line_color='#ff7f0e'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title=f"CEFOPE vs {benchmark}"
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Análise de gap
    st.markdown("---")
    st.subheader("📊 Análise de Gap")
    
    gaps = []
    for i in range(len(indicadores_bench)):
        gap = valores_cefope[i] - valores_bench[i]
        gaps.append(gap)
    
    df_gaps = pd.DataFrame({
        "Indicador": indicadores_bench,
        "CEFOPE": valores_cefope,
        benchmark: valores_bench,
        "Gap": gaps,
        "Status": ["Acima" if g > 0 else "Abaixo" if g < 0 else "Alinhado" for g in gaps]
    })
    
    # Gráfico de gaps
    fig = px.bar(
        df_gaps,
        x="Indicador",
        y="Gap",
        color="Status",
        title=f"Gap de Performance: CEFOPE vs {benchmark}",
        color_discrete_map={"Acima": "#28a745", "Abaixo": "#dc3545", "Alinhado": "#6c757d"}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, width='stretch')
    
    # Tabela de gaps
    st.subheader("📋 Resumo dos Gaps")
    st.dataframe(
        df_gaps.style.format({
            "CEFOPE": "{:.1f}",
            benchmark: "{:.1f}",
            "Gap": "{:+.1f}"
        }),
        width='stretch'
    )
    
    # Recomendações baseadas no gap
    st.markdown("---")
    st.subheader("💡 Recomendações Baseadas no Gap")
    
    gaps_positivos = sum(1 for g in gaps if g > 0)
    gaps_negativos = sum(1 for g in gaps if g < 0)
    
    if gaps_positivos > gaps_negativos:
        st.success("🎉 **Excelente!** O CEFOPE está superando o benchmark na maioria dos indicadores.")
        st.markdown("**Recomendações:**")
        st.markdown("- Manter as práticas que estão gerando resultados superiores")
        st.markdown("- Compartilhar melhores práticas com outras instituições")
        st.markdown("- Estabelecer novos benchmarks mais desafiadores")
    elif gaps_negativos > gaps_positivos:
        st.warning("⚠️ **Atenção!** Existem oportunidades de melhoria em vários indicadores.")
        st.markdown("**Recomendações:**")
        st.markdown("- Identificar as causas dos gaps negativos")
        st.markdown("- Desenvolver planos de ação específicos")
        st.markdown("- Implementar melhorias baseadas em benchmarks")
    else:
        st.info("ℹ️ **Equilibrado!** O CEFOPE está alinhado com o benchmark.")
        st.markdown("**Recomendações:**")
        st.markdown("- Manter o equilíbrio atual")
        st.markdown("- Identificar oportunidades de crescimento")
        st.markdown("- Estabelecer metas mais ambiciosas")

def render_comparacao_municipios(municipios_df):
    """Renderiza comparação entre municípios"""
    
    st.subheader("🏙️ Comparação entre Municípios")
    
    if municipios_df is not None:
        # Top 10 municípios
        top_municipios = municipios_df.nlargest(10, 'Total_Professores')
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras
            fig = px.bar(
                top_municipios,
                x='Total_Professores',
                y='Municipio',
                orientation='h',
                title="Top 10 Municípios por Número de Professores",
                color='Total_Professores',
                color_continuous_scale='Blues',
                labels={'Total_Professores': 'Número de Professores', 'Municipio': 'Município'}
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Gráfico de pizza
            fig = px.pie(
                top_municipios,
                values='Total_Professores',
                names='Municipio',
                title="Distribuição de Professores - Top 10 Municípios"
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, width='stretch')
        
        # Tabela comparativa
        st.subheader("📋 Tabela Comparativa")
        st.dataframe(top_municipios, width='stretch')
    else:
        st.info("Dados de municípios não disponíveis")

def render_comparacao_dependencias(dependencia_df):
    """Renderiza comparação entre dependências"""
    
    st.subheader("🏫 Comparação entre Dependências Administrativas")
    
    if dependencia_df is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras
            fig = px.bar(
                dependencia_df,
                x='Dependencia',
                y='Total_Professores',
                title="Professores por Dependência",
                color='Total_Professores',
                color_continuous_scale='Greens',
                labels={'Total_Professores': 'Número de Professores', 'Dependencia': 'Dependência'}
            )
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Gráfico de pizza
            fig = px.pie(
                dependencia_df,
                values='Total_Professores',
                names='Dependencia',
                title="Distribuição de Professores por Dependência"
            )
            st.plotly_chart(fig, width='stretch')
        
        # Tabela comparativa
        st.subheader("📋 Tabela Comparativa")
        st.dataframe(dependencia_df, width='stretch')
    else:
        st.info("Dados de dependências não disponíveis")

def render_comparacao_localizacao(localizacao_df):
    """Renderiza comparação entre localizações"""
    
    st.subheader("🌍 Comparação entre Localizações")
    
    if localizacao_df is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras
            fig = px.bar(
                localizacao_df,
                x='Localizacao',
                y='Total_Professores',
                title="Professores por Localização",
                color='Total_Professores',
                color_continuous_scale='Oranges',
                labels={'Total_Professores': 'Número de Professores', 'Localizacao': 'Localização'}
            )
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Gráfico de pizza
            fig = px.pie(
                localizacao_df,
                values='Total_Professores',
                names='Localizacao',
                title="Distribuição de Professores por Localização"
            )
            st.plotly_chart(fig, width='stretch')
        
        # Tabela comparativa
        st.subheader("📋 Tabela Comparativa")
        st.dataframe(localizacao_df, width='stretch')
    else:
        st.info("Dados de localização não disponíveis")

def render_comparacao_cursos(cursos_df):
    """Renderiza comparação entre cursos técnicos"""
    
    st.subheader("🔧 Comparação entre Cursos Técnicos")
    
    if cursos_df is not None:
        # Top 15 cursos
        top_cursos = cursos_df['NO_CURSO_EDUC_PROFISSIONAL'].value_counts().head(15).reset_index()
        top_cursos.columns = ['Curso', 'Ofertas']
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras
            fig = px.bar(
                top_cursos,
                x='Ofertas',
                y='Curso',
                orientation='h',
                title="Top 15 Cursos Técnicos por Ofertas",
                color='Ofertas',
                color_continuous_scale='Viridis',
                labels={'Ofertas': 'Número de Ofertas', 'Curso': 'Curso Técnico'}
            )
            fig.update_layout(height=600)
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Gráfico de pizza
            fig = px.pie(
                top_cursos.head(10),
                values='Ofertas',
                names='Curso',
                title="Distribuição dos Top 10 Cursos Técnicos"
            )
            fig.update_layout(height=600)
            st.plotly_chart(fig, width='stretch')
        
        # Tabela comparativa
        st.subheader("📋 Tabela Comparativa")
        st.dataframe(top_cursos, width='stretch')
    else:
        st.info("Dados de cursos técnicos não disponíveis")

def render_comparacao_indicadores(escolas_df):
    """Renderiza comparação entre indicadores"""
    
    st.subheader("📊 Comparação entre Indicadores")
    
    if escolas_df is not None:
        # Calcular indicadores
        indicadores = {
            'Indicador': ['Total de Professores', 'Total de Matrículas', 'Total de Turmas', 'Média Prof/Escola', 'Média Mat/Escola'],
            'Valor': [
                int(escolas_df['TOTAL_PROFESSORES'].sum()),
                int(escolas_df['TOTAL_MATRICULAS'].sum()),
                int(escolas_df['TOTAL_TURMAS'].sum()),
                round(escolas_df['TOTAL_PROFESSORES'].mean(), 1),
                round(escolas_df['TOTAL_MATRICULAS'].mean(), 1)
            ]
        }
        
        df_indicadores = pd.DataFrame(indicadores)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras
            fig = px.bar(
                df_indicadores,
                x='Indicador',
                y='Valor',
                title="Comparação de Indicadores Educacionais",
                color='Valor',
                color_continuous_scale='Reds',
                labels={'Valor': 'Valor', 'Indicador': 'Indicador'}
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Gráfico de pizza (normalizado)
            df_normalizado = df_indicadores.copy()
            df_normalizado['Valor_Normalizado'] = df_normalizado['Valor'] / df_normalizado['Valor'].max() * 100
            
            fig = px.pie(
                df_normalizado,
                values='Valor_Normalizado',
                names='Indicador',
                title="Distribuição Relativa dos Indicadores (%)"
            )
            st.plotly_chart(fig, width='stretch')
        
        # Tabela comparativa
        st.subheader("📋 Tabela Comparativa")
        st.dataframe(df_indicadores, width='stretch')
    else:
        st.info("Dados de indicadores não disponíveis")
