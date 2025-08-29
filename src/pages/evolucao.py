"""
Página de evolução temporal
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def render_evolucao():
    """Renderiza a página de evolução temporal"""
    
    st.title("📈 Evolução Temporal - CEFOPE")
    st.markdown("Análise de tendências e evolução dos indicadores ao longo do tempo")
    
    # Filtros temporais
    st.subheader("🔍 Filtros Temporais")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        periodo_analise = st.selectbox(
            "Período de Análise",
            ["Últimos 5 anos", "Últimos 10 anos", "Últimos 15 anos", "Todo o período"]
        )
    
    with col2:
        tipo_indicador = st.selectbox(
            "Indicador",
            ["Todos", "Matrículas", "Formações", "Cursos", "Satisfação", "Empregabilidade"]
        )
    
    with col3:
        granularidade = st.selectbox(
            "Granularidade",
            ["Anual", "Semestral", "Trimestral", "Mensal"]
        )
    
    st.markdown("---")
    
    # Visão geral da evolução
    st.subheader("📊 Visão Geral da Evolução")
    
    # Dados simulados de evolução anual
    anos = list(range(2015, 2026))
    evolucao_data = {
        "Ano": anos,
        "Matriculas": [3200, 3500, 3800, 4200, 4600, 5100, 5700, 6300, 6900, 7500, 8200],
        "Formacoes_Concluidas": [2800, 3100, 3400, 3800, 4200, 4700, 5200, 5800, 6400, 7000, 7600],
        "Cursos_Ativos": [45, 52, 58, 65, 72, 79, 87, 95, 103, 112, 121],
        "Taxa_Conclusao": [87.5, 88.6, 89.5, 90.5, 91.3, 92.2, 91.2, 92.1, 92.8, 93.3, 92.7],
        "Satisfacao_Media": [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.5, 4.6, 4.7, 4.7, 4.8]
    }
    
    df_evolucao = pd.DataFrame(evolucao_data)
    
    # Métricas de evolução
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        crescimento_total = ((df_evolucao['Matriculas'].iloc[-1] - df_evolucao['Matriculas'].iloc[0]) / df_evolucao['Matriculas'].iloc[0]) * 100
        st.metric(
            label="Crescimento Total",
            value=f"{crescimento_total:.1f}%",
            delta=f"+{crescimento_total:.1f}%",
            delta_color="normal"
        )
    
    with col2:
        media_crescimento_anual = df_evolucao['Matriculas'].pct_change().mean() * 100
        st.metric(
            label="Crescimento Médio Anual",
            value=f"{media_crescimento_anual:.1f}%",
            delta=f"+{media_crescimento_anual:.1f}%",
            delta_color="normal"
        )
    
    with col3:
        ano_maior_crescimento = df_evolucao.loc[df_evolucao['Matriculas'].pct_change().idxmax(), 'Ano']
        st.metric(
            label="Ano de Maior Crescimento",
            value=str(int(ano_maior_crescimento)),
            delta="Pico histórico",
            delta_color="normal"
        )
    
    with col4:
        tendencia_atual = "Positiva" if df_evolucao['Matriculas'].pct_change().iloc[-1] > 0 else "Negativa"
        st.metric(
            label="Tendência Atual",
            value=tendencia_atual,
            delta="Último ano",
            delta_color="normal" if tendencia_atual == "Positiva" else "inverse"
        )
    
    # Gráficos de evolução
    st.markdown("---")
    st.subheader("📈 Análise de Tendências")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Evolução das matrículas
        fig = px.line(
            df_evolucao,
            x="Ano",
            y="Matriculas",
            title="Evolução das Matrículas ao Longo do Tempo",
            labels={"Matriculas": "Quantidade de Matrículas"},
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Evolução da taxa de conclusão
        fig = px.line(
            df_evolucao,
            x="Ano",
            y="Taxa_Conclusao",
            title="Evolução da Taxa de Conclusão (%)",
            labels={"Taxa_Conclusao": "Taxa (%)"},
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Análise de sazonalidade
    st.markdown("---")
    st.subheader("🔄 Análise de Sazonalidade")
    
    # Dados simulados mensais para análise sazonal
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    matriculas_mensais = [1200, 1350, 1100, 980, 850, 720, 680, 750, 890, 1100, 1250, 1400]
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Padrão sazonal mensal
        fig = px.bar(
            x=meses,
            y=matriculas_mensais,
            title="Padrão Sazonal - Matrículas por Mês",
            labels={"x": "Mês", "y": "Matrículas"},
            color=matriculas_mensais,
            color_continuous_scale="Viridis"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Comparação entre anos (últimos 3 anos)
        anos_comparacao = [2023, 2024, 2025]
        dados_comparacao = {
            "Janeiro": [1100, 1150, 1200],
            "Fevereiro": [1250, 1300, 1350],
            "Março": [1000, 1050, 1100],
            "Abril": [900, 940, 980],
            "Maio": [800, 825, 850],
            "Junho": [680, 700, 720]
        }
        
        df_comparacao = pd.DataFrame(dados_comparacao, index=anos_comparacao)
        
        fig = px.line(
            df_comparacao.T,
            title="Comparação Mensal entre Anos",
            labels={"value": "Matrículas", "variable": "Ano"},
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Análise de correlação temporal
    st.markdown("---")
    st.subheader("🔗 Análise de Correlação Temporal")
    
    # Matriz de correlação entre indicadores ao longo do tempo
    indicadores_corr = ["Matrículas", "Formações", "Cursos", "Taxa_Conclusão", "Satisfação"]
    
    # Dados simulados para correlação
    matriz_corr_temporal = np.array([
        [1.0, 0.95, 0.87, 0.23, 0.45],
        [0.95, 1.0, 0.89, 0.31, 0.52],
        [0.87, 0.89, 1.0, 0.28, 0.48],
        [0.23, 0.31, 0.28, 1.0, 0.67],
        [0.45, 0.52, 0.48, 0.67, 1.0]
    ])
    
    fig = px.imshow(
        matriz_corr_temporal,
        x=indicadores_corr,
        y=indicadores_corr,
        title="Correlação entre Indicadores ao Longo do Tempo",
        color_continuous_scale="RdBu",
        aspect="auto"
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Projeções e tendências futuras
    st.markdown("---")
    st.subheader("🔮 Projeções e Tendências Futuras")
    
    # Dados simulados para projeção
    anos_projecao = list(range(2025, 2031))
    projecao_matriculas = [8200, 8900, 9600, 10300, 11000, 11700]
    
    # Dados históricos + projeção
    anos_completos = anos + anos_projecao[1:]
    matriculas_completas = df_evolucao['Matriculas'].tolist() + projecao_matriculas[1:]
    
    # Criando DataFrame com dados históricos e projeções
    df_projecao = pd.DataFrame({
        "Ano": anos_completos,
        "Matriculas": matriculas_completas,
        "Tipo": ["Histórico"] * len(anos) + ["Projeção"] * len(anos_projecao[1:])
    })
    
    # Gráfico com projeção
    fig = px.line(
        df_projecao,
        x="Ano",
        y="Matriculas",
        color="Tipo",
        title="Projeção de Matrículas (2025-2030)",
        labels={"Matriculas": "Quantidade de Matrículas"},
        markers=True
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    fig.add_vline(x=2025, line_dash="dash", line_color="red", annotation_text="Início das Projeções")
    st.plotly_chart(fig, use_container_width=True)
    
    # Análise de fatores de crescimento
    st.markdown("---")
    st.subheader("📊 Fatores que Influenciam o Crescimento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Fatores internos
        fatores_internos = ["Qualidade dos Cursos", "Metodologia", "Infraestrutura", "Corpo Docente"]
        impacto_interno = [85, 78, 72, 88]
        
        fig = px.bar(
            x=fatores_internos,
            y=impacto_interno,
            title="Impacto dos Fatores Internos (%)",
            labels={"x": "Fator", "y": "Impacto (%)"},
            color=impacto_interno,
            color_continuous_scale="Greens"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Fatores externos
        fatores_externos = ["Demanda de Mercado", "Políticas Públicas", "Concorrência", "Economia"]
        impacto_externo = [92, 85, 68, 75]
        
        fig = px.bar(
            x=fatores_externos,
            y=impacto_externo,
            title="Impacto dos Fatores Externos (%)",
            labels={"x": "Fator", "y": "Impacto (%)"},
            color=impacto_externo,
            color_continuous_scale="Blues"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Insights e recomendações
    st.markdown("---")
    st.subheader("💡 Insights e Recomendações")
    
    st.markdown("""
    **Principais insights da análise temporal:**
    
    📈 **Crescimento Consistente**: O CEFOPE apresenta crescimento sustentado de 
    aproximadamente 8-10% ao ano, indicando forte demanda e qualidade reconhecida.
    
    🎯 **Sazonalidade Identificada**: Existe padrão sazonal claro com picos em 
    janeiro/fevereiro e novembro/dezembro, relacionado ao calendário acadêmico.
    
    🔄 **Correlação entre Indicadores**: Matrículas e formações apresentam alta 
    correlação (0.95), enquanto taxa de conclusão tem correlação baixa com volume.
    
    **Recomendações estratégicas:**
    
    🚀 **Expansão Planejada**: Com base nas projeções, planejar aumento de 
    capacidade para atender demanda crescente até 2030.
    
    📅 **Gestão da Sazonalidade**: Desenvolver estratégias para suavizar variações 
    sazonais e manter fluxo constante de matrículas.
    
    🎓 **Foco na Qualidade**: Manter foco na qualidade dos cursos, pois é o 
    fator interno com maior impacto no crescimento.
    
    📊 **Monitoramento Contínuo**: Implementar sistema de monitoramento em tempo 
    real dos indicadores para ajustes rápidos na estratégia.
    """)
