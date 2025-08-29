"""
Página de análise da formação de professores
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def render_formacao():
    """Renderiza a página de formação de professores"""
    
    st.title("🎓 Formação de Professores - CEFOPE")
    st.markdown("Análise detalhada do fluxo educacional e programas de formação")
    
    # Filtros
    st.subheader("🔍 Filtros de Análise")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tipo_formacao = st.selectbox(
            "Tipo de Formação",
            ["Todos", "Formação Inicial", "Formação Continuada", "Pós-Graduação"]
        )
    
    with col2:
        periodo = st.selectbox(
            "Período",
            ["Últimos 5 anos", "Últimos 3 anos", "Último ano", "Personalizado"]
        )
    
    with col3:
        area = st.selectbox(
            "Área de Conhecimento",
            ["Todas", "Matemática", "Português", "História", "Geografia", "Ciências", "Artes", "Educação Física"]
        )
    
    st.markdown("---")
    
    # Estatísticas da formação
    st.subheader("📊 Estatísticas da Formação")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total de Matrículas",
            value="15.234",
            delta="+8.7%",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Formações Concluídas",
            value="12.847",
            delta="+5.2%",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Em Andamento",
            value="2.387",
            delta="+12.3%",
            delta_color="normal"
        )
    
    with col4:
        st.metric(
            label="Taxa de Evasão",
            value="12.8%",
            delta="-2.1%",
            delta_color="inverse"
        )
    
    # Gráficos de análise
    st.markdown("---")
    st.subheader("📈 Análise Temporal da Formação")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Evolução mensal das matrículas
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        matriculas = [1200, 1350, 1100, 980, 850, 720, 680, 750, 890, 1100, 1250, 1400]
        
        fig = px.line(
            x=meses,
            y=matriculas,
            title="Matrículas por Mês (2025)",
            labels={"x": "Mês", "y": "Matrículas"},
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Distribuição por modalidade
        modalidades = ["Presencial", "Híbrido", "EAD"]
        quantidades = [45, 35, 20]
        
        fig = px.bar(
            x=modalidades,
            y=quantidades,
            title="Distribuição por Modalidade (%)",
            labels={"x": "Modalidade", "y": "Percentual"},
            color=quantidades,
            color_continuous_scale="Viridis"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Análise por programa
    st.markdown("---")
    st.subheader("🎯 Programas de Formação")
    
    # Dados simulados dos programas
    programas_data = {
        "Programa": [
            "Licenciatura em Matemática",
            "Licenciatura em Português",
            "Pedagogia",
            "Formação Continuada em História",
            "Especialização em Educação Especial",
            "Mestrado em Educação"
        ],
        "Matrículas": [450, 380, 520, 280, 320, 180],
        "Concluídos": [420, 350, 480, 250, 290, 160],
        "Taxa_Conclusao": [93.3, 92.1, 92.3, 89.3, 90.6, 88.9]
    }
    
    df_programas = pd.DataFrame(programas_data)
    
    # Gráfico de barras para programas
    fig = px.bar(
        df_programas,
        x="Programa",
        y="Matrículas",
        title="Matrículas por Programa",
        color="Taxa_Conclusao",
        color_continuous_scale="RdYlGn",
        labels={"Taxa_Conclusao": "Taxa de Conclusão (%)"}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabela detalhada
    st.subheader("📋 Detalhamento dos Programas")
    st.dataframe(
        df_programas.style.format({
            "Taxa_Conclusao": "{:.1f}%"
        }),
        use_container_width=True
    )
    
    # Indicadores de qualidade
    st.markdown("---")
    st.subheader("⭐ Indicadores de Qualidade da Formação")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Satisfação dos alunos
        satisfacao = [4.2, 4.5, 4.7, 4.3, 4.6, 4.8]
        programas = ["Matemática", "Português", "Pedagogia", "História", "Educ. Especial", "Mestrado"]
        
        fig = px.bar(
            x=programas,
            y=satisfacao,
            title="Satisfação dos Alunos por Programa",
            labels={"x": "Programa", "y": "Satisfação (1-5)"},
            color=satisfacao,
            color_continuous_scale="RdYlGn"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Taxa de empregabilidade
        empregabilidade = [96.2, 94.8, 97.1, 93.5, 95.2, 98.5]
        
        fig = px.bar(
            x=programas,
            y=empregabilidade,
            title="Taxa de Empregabilidade por Programa (%)",
            labels={"x": "Programa", "y": "Empregabilidade (%)"},
            color=empregabilidade,
            color_continuous_scale="Blues"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Informações sobre metodologia
    st.markdown("---")
    st.subheader("📚 Metodologia de Ensino")
    
    st.markdown("""
    **Nossa metodologia de formação é baseada em:**
    
    🎯 **Aprendizagem Baseada em Projetos**: Os alunos desenvolvem projetos reais 
    que os preparam para os desafios da sala de aula.
    
    🔄 **Formação Continuada**: Oferecemos programas de atualização e especialização 
    para professores em serviço.
    
    💻 **Tecnologia Educacional**: Integramos ferramentas digitais e metodologias 
    inovadoras em todos os nossos programas.
    
    🌍 **Perspectiva Global**: Nossos currículos incluem perspectivas internacionais 
    e melhores práticas educacionais.
    
    **Duração dos Programas:**
    - **Licenciaturas**: 4 anos (8 semestres)
    - **Pedagogia**: 4 anos (8 semestres)
    - **Formação Continuada**: 6 meses a 2 anos
    - **Especializações**: 1 a 2 anos
    - **Mestrado**: 2 anos (4 semestres)
    """)
