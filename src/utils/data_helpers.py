"""
Utilitários para manipulação de dados
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional

def create_sample_data() -> Dict[str, pd.DataFrame]:
    """
    Cria dados de exemplo para demonstração do aplicativo
    
    Returns:
        Dict com DataFrames de exemplo
    """
    
    # Dados de evolução temporal
    anos = list(range(2015, 2026))
    evolucao_data = {
        "Ano": anos,
        "Matriculas": [3200, 3500, 3800, 4200, 4600, 5100, 5700, 6300, 6900, 7500, 8200],
        "Formacoes_Concluidas": [2800, 3100, 3400, 3800, 4200, 4700, 5200, 5800, 6400, 7000, 7600],
        "Cursos_Ativos": [45, 52, 58, 65, 72, 79, 87, 95, 103, 112, 121],
        "Taxa_Conclusao": [87.5, 88.6, 89.5, 90.5, 91.3, 92.2, 91.2, 92.1, 92.8, 93.3, 92.7],
        "Satisfacao_Media": [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.5, 4.6, 4.7, 4.7, 4.8]
    }
    
    # Dados por região
    regioes_data = {
        "Regiao": ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
        "Professores_Formados": [850, 2100, 1200, 4500, 3200],
        "Cursos_Ativos": [23, 45, 28, 89, 67],
        "Instituicoes_Parceiras": [12, 28, 18, 45, 32],
        "Taxa_Conclusao": [85.2, 88.7, 87.3, 89.1, 91.2],
        "Satisfacao_Media": [4.3, 4.5, 4.4, 4.6, 4.7]
    }
    
    # Dados dos programas
    programas_data = {
        "Programa": [
            "Licenciatura em Matemática",
            "Licenciatura em Português",
            "Pedagogia",
            "Formação Continuada em História",
            "Especialização em Educação Especial",
            "Mestrado em Educação"
        ],
        "Matriculas": [450, 380, 520, 280, 320, 180],
        "Concluidos": [420, 350, 480, 250, 290, 160],
        "Taxa_Conclusao": [93.3, 92.1, 92.3, 89.3, 90.6, 88.9],
        "Satisfacao": [4.2, 4.5, 4.7, 4.3, 4.6, 4.8],
        "Empregabilidade": [96.2, 94.8, 97.1, 93.5, 95.2, 98.5]
    }
    
    return {
        "evolucao": pd.DataFrame(evolucao_data),
        "regioes": pd.DataFrame(regioes_data),
        "programas": pd.DataFrame(programas_data)
    }

def calculate_growth_rate(data: pd.Series, periods: int = 1) -> float:
    """
    Calcula a taxa de crescimento entre dois períodos
    
    Args:
        data: Série temporal com os dados
        periods: Número de períodos para calcular o crescimento
        
    Returns:
        Taxa de crescimento em percentual
    """
    if len(data) < periods + 1:
        return 0.0
    
    initial_value = data.iloc[0]
    final_value = data.iloc[periods]
    
    if initial_value == 0:
        return 0.0
    
    return ((final_value - initial_value) / initial_value) * 100

def calculate_compound_annual_growth_rate(data: pd.Series) -> float:
    """
    Calcula a taxa de crescimento anual composta (CAGR)
    
    Args:
        data: Série temporal com os dados
        
    Returns:
        CAGR em percentual
    """
    if len(data) < 2:
        return 0.0
    
    initial_value = data.iloc[0]
    final_value = data.iloc[-1]
    periods = len(data) - 1
    
    if initial_value <= 0 or periods <= 0:
        return 0.0
    
    return ((final_value / initial_value) ** (1 / periods) - 1) * 100

def normalize_data(data: pd.Series, method: str = "minmax") -> pd.Series:
    """
    Normaliza dados para escala 0-1 ou 0-100
    
    Args:
        data: Série com os dados
        method: Método de normalização ('minmax' ou 'zscore')
        
    Returns:
        Série normalizada
    """
    if method == "minmax":
        min_val = data.min()
        max_val = data.max()
        if max_val == min_val:
            return pd.Series([0.5] * len(data), index=data.index)
        return (data - min_val) / (max_val - min_val) * 100
    
    elif method == "zscore":
        mean_val = data.mean()
        std_val = data.std()
        if std_val == 0:
            return pd.Series([0] * len(data), index=data.index)
        return (data - mean_val) / std_val
    
    else:
        raise ValueError("Método deve ser 'minmax' ou 'zscore'")

def create_time_series_data(start_year: int, end_year: int, 
                           base_value: float, growth_rate: float,
                           seasonality: Optional[Dict[str, float]] = None) -> pd.DataFrame:
    """
    Cria dados de série temporal simulados
    
    Args:
        start_year: Ano inicial
        end_year: Ano final
        base_value: Valor base inicial
        growth_rate: Taxa de crescimento anual
        seasonality: Dicionário com fatores sazonais por mês
        
    Returns:
        DataFrame com dados temporais
    """
    years = list(range(start_year, end_year + 1))
    data = []
    
    for year in years:
        # Crescimento anual
        annual_value = base_value * (1 + growth_rate/100) ** (year - start_year)
        
        if seasonality:
            for month in range(1, 13):
                month_name = pd.Timestamp(year, month, 1).strftime("%b")
                seasonal_factor = seasonality.get(month_name, 1.0)
                monthly_value = annual_value * seasonal_factor
                
                data.append({
                    "Ano": year,
                    "Mes": month,
                    "Mes_Nome": month_name,
                    "Valor": monthly_value
                })
        else:
            data.append({
                "Ano": year,
                "Valor": annual_value
            })
    
    return pd.DataFrame(data)

def calculate_correlation_matrix(data: pd.DataFrame, 
                               numeric_columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Calcula matriz de correlação entre colunas numéricas
    
    Args:
        data: DataFrame com os dados
        numeric_columns: Lista de colunas numéricas (se None, usa todas)
        
    Returns:
        DataFrame com matriz de correlação
    """
    if numeric_columns is None:
        numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    
    correlation_data = data[numeric_columns].corr()
    return correlation_data

def generate_summary_statistics(data: pd.DataFrame, 
                              group_by: Optional[str] = None) -> pd.DataFrame:
    """
    Gera estatísticas resumidas dos dados
    
    Args:
        data: DataFrame com os dados
        group_by: Coluna para agrupamento (opcional)
        
    Returns:
        DataFrame com estatísticas resumidas
    """
    if group_by:
        summary = data.groupby(group_by).agg({
            col: ['count', 'mean', 'std', 'min', 'max'] 
            for col in data.select_dtypes(include=[np.number]).columns
        }).round(2)
    else:
        summary = data.describe().round(2)
    
    return summary
