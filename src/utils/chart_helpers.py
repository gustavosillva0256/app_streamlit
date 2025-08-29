"""
Utilitários para criação e personalização de gráficos
"""

import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Any, Optional, Union
import pandas as pd

def apply_default_theme(fig: Union[go.Figure, px.Figure]) -> Union[go.Figure, px.Figure]:
    """
    Aplica tema padrão aos gráficos
    
    Args:
        fig: Figura do Plotly
        
    Returns:
        Figura com tema aplicado
    """
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="#333333"
        ),
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    return fig

def create_metric_card(title: str, value: str, delta: str = "", 
                      delta_color: str = "normal") -> str:
    """
    Cria HTML para card de métrica
    
    Args:
        title: Título da métrica
        value: Valor principal
        delta: Variação (opcional)
        delta_color: Cor da variação
        
    Returns:
        HTML formatado
    """
    delta_html = ""
    if delta:
        delta_class = "positive" if delta_color == "normal" else "negative"
        delta_html = f'<span class="delta {delta_class}">{delta}</span>'
    
    return f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """

def create_line_chart(data: pd.DataFrame, x_col: str, y_col: str, 
                     title: str = "", color_col: Optional[str] = None,
                     markers: bool = True) -> go.Figure:
    """
    Cria gráfico de linha padronizado
    
    Args:
        data: DataFrame com os dados
        x_col: Coluna para eixo X
        y_col: Coluna para eixo Y
        title: Título do gráfico
        color_col: Coluna para colorir as linhas
        markers: Se deve mostrar marcadores
        
    Returns:
        Figura do Plotly
    """
    if color_col:
        fig = px.line(
            data, 
            x=x_col, 
            y=y_col,
            color=color_col,
            title=title,
            markers=markers
        )
    else:
        fig = px.line(
            data, 
            x=x_col, 
            y=y_col,
            title=title,
            markers=markers
        )
    
    fig = apply_default_theme(fig)
    return fig

def create_bar_chart(data: pd.DataFrame, x_col: str, y_col: str,
                     title: str = "", color_col: Optional[str] = None,
                     orientation: str = "v") -> go.Figure:
    """
    Cria gráfico de barras padronizado
    
    Args:
        data: DataFrame com os dados
        x_col: Coluna para eixo X
        y_col: Coluna para eixo Y
        title: Título do gráfico
        color_col: Coluna para colorir as barras
        orientation: Orientação ('v' para vertical, 'h' para horizontal)
        
    Returns:
        Figura do Plotly
    """
    if color_col:
        fig = px.bar(
            data,
            x=x_col if orientation == "v" else y_col,
            y=y_col if orientation == "v" else x_col,
            color=color_col,
            title=title,
            orientation=orientation
        )
    else:
        fig = px.bar(
            data,
            x=x_col if orientation == "v" else y_col,
            y=y_col if orientation == "v" else x_col,
            title=title,
            orientation=orientation
        )
    
    fig = apply_default_theme(fig)
    return fig

def create_pie_chart(data: pd.DataFrame, values_col: str, names_col: str,
                     title: str = "") -> go.Figure:
    """
    Cria gráfico de pizza padronizado
    
    Args:
        data: DataFrame com os dados
        values_col: Coluna com os valores
        names_col: Coluna com os nomes
        title: Título do gráfico
        
    Returns:
        Figura do Plotly
    """
    fig = px.pie(
        data,
        values=values_col,
        names=names_col,
        title=title,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig = apply_default_theme(fig)
    return fig

def create_scatter_plot(data: pd.DataFrame, x_col: str, y_col: str,
                        title: str = "", color_col: Optional[str] = None,
                        size_col: Optional[str] = None) -> go.Figure:
    """
    Cria gráfico de dispersão padronizado
    
    Args:
        data: DataFrame com os dados
        x_col: Coluna para eixo X
        y_col: Coluna para eixo Y
        title: Título do gráfico
        color_col: Coluna para colorir os pontos
        size_col: Coluna para tamanho dos pontos
        
    Returns:
        Figura do Plotly
    """
    fig = px.scatter(
        data,
        x=x_col,
        y=y_col,
        title=title,
        color=color_col,
        size=size_col,
        hover_name=data.index if 'index' in data.columns else None
    )
    
    fig = apply_default_theme(fig)
    return fig

def create_heatmap(data: pd.DataFrame, x_col: str, y_col: str, values_col: str,
                   title: str = "") -> go.Figure:
    """
    Cria mapa de calor padronizado
    
    Args:
        data: DataFrame com os dados
        x_col: Coluna para eixo X
        y_col: Coluna para eixo Y
        values_col: Coluna com os valores
        title: Título do gráfico
        
    Returns:
        Figura do Plotly
    """
    # Pivotar dados para formato de matriz
    pivot_data = data.pivot(index=y_col, columns=x_col, values=values_col)
    
    fig = px.imshow(
        pivot_data,
        title=title,
        color_continuous_scale="RdBu",
        aspect="auto"
    )
    
    fig = apply_default_theme(fig)
    return fig

def create_radar_chart(categories: List[str], values: List[float],
                       title: str = "", name: str = "Dados") -> go.Figure:
    """
    Cria gráfico de radar padronizado
    
    Args:
        categories: Lista de categorias
        values: Lista de valores
        title: Título do gráfico
        name: Nome da série de dados
        
    Returns:
        Figura do Plotly
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=name,
        line_color='#1f77b4'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) * 1.1]
            )),
        showlegend=True,
        title=title
    )
    
    fig = apply_default_theme(fig)
    return fig

def add_annotations_to_chart(fig: go.Figure, annotations: List[Dict[str, Any]]) -> go.Figure:
    """
    Adiciona anotações ao gráfico
    
    Args:
        fig: Figura do Plotly
        annotations: Lista de anotações
        
    Returns:
        Figura com anotações
    """
    for annotation in annotations:
        fig.add_annotation(
            x=annotation.get('x'),
            y=annotation.get('y'),
            text=annotation.get('text', ''),
            showarrow=annotation.get('showarrow', True),
            arrowhead=annotation.get('arrowhead', 2),
            arrowsize=annotation.get('arrowsize', 1),
            arrowwidth=annotation.get('arrowwidth', 2),
            arrowcolor=annotation.get('arrowcolor', '#333333'),
            bgcolor=annotation.get('bgcolor', 'rgba(255,255,255,0.8)'),
            bordercolor=annotation.get('bordercolor', '#333333'),
            borderwidth=annotation.get('borderwidth', 1)
        )
    
    return fig

def create_subplot_grid(rows: int, cols: int, 
                       subplot_titles: Optional[List[str]] = None) -> go.Figure:
    """
    Cria figura com subplots em grade
    
    Args:
        rows: Número de linhas
        cols: Número de colunas
        subplot_titles: Títulos dos subplots
        
    Returns:
        Figura com subplots
    """
    fig = go.Figure()
    
    fig = go.Figure()
    fig = go.Figure()
    
    # Criando subplots
    fig = go.Figure()
    
    # Adicionando subplots vazios
    for i in range(rows * cols):
        fig.add_trace(go.Scatter(x=[], y=[], visible=False))
    
    # Configurando layout de subplots
    fig.update_layout(
        grid=dict(rows=rows, columns=cols),
        subplot_titles=subplot_titles if subplot_titles else [f"Subplot {i+1}" for i in range(rows * cols)]
    )
    
    fig = apply_default_theme(fig)
    return fig

def export_chart_as_image(fig: go.Figure, filename: str, 
                          format: str = "png", width: int = 800, 
                          height: int = 600) -> None:
    """
    Exporta gráfico como imagem
    
    Args:
        fig: Figura do Plotly
        filename: Nome do arquivo
        format: Formato da imagem
        width: Largura da imagem
        height: Altura da imagem
    """
    try:
        fig.write_image(filename, width=width, height=height)
    except Exception as e:
        print(f"Erro ao exportar gráfico: {e}")
        print("Certifique-se de que o kaleido está instalado: pip install kaleido")

def create_dashboard_layout(figures: List[go.Figure], 
                           titles: Optional[List[str]] = None,
                           layout: str = "grid") -> go.Figure:
    """
    Cria layout de dashboard com múltiplos gráficos
    
    Args:
        figures: Lista de figuras
        titles: Títulos das figuras
        layout: Tipo de layout ('grid' ou 'vertical')
        
    Returns:
        Figura combinada
    """
    if not titles:
        titles = [f"Gráfico {i+1}" for i in range(len(figures))]
    
    if layout == "grid":
        rows = int(len(figures) ** 0.5) + (1 if len(figures) % 2 else 0)
        cols = 2
        fig = create_subplot_grid(rows, cols, titles)
    else:
        # Layout vertical
        fig = go.Figure()
        for i, (figure, title) in enumerate(zip(figures, titles)):
            fig.add_trace(figure.data[0])
            fig.update_layout(title=title)
    
    return fig
