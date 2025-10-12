"""
Serviço para gerenciamento de dados
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import json
import os
import streamlit as st

class DataService:
    """Serviço para gerenciamento e manipulação de dados"""
    
    def __init__(self):
        """Inicializa o serviço de dados"""
        self.data_cache = {}
        self.data_sources = {}
        self.last_update = None
    
    def load_real_data(self) -> Dict[str, pd.DataFrame]:
        """
        Carrega dados reais do INEP para o Espírito Santo
        
        Returns:
            Dicionário com DataFrames dos dados reais
        """
        try:
            # Carregar dados das escolas do ES
            escolas_df = pd.read_csv('data/dados/escolas_es_2024.csv', encoding='utf-8')
            
            # Carregar dados dos cursos técnicos do ES
            cursos_df = pd.read_csv('data/dados/cursos_tecnicos_es_2024.csv', encoding='utf-8')
            
            # Processar dados das escolas
            escolas_processed = self._process_escolas_data(escolas_df)
            
            # Processar dados dos cursos
            cursos_processed = self._process_cursos_data(cursos_df)
            
            # Criar dados agregados para visualizações
            aggregated_data = self._create_aggregated_data(escolas_processed, cursos_processed)
            
            data = {
                "escolas": escolas_processed,
                "cursos_tecnicos": cursos_processed,
                **aggregated_data
            }
            
            # Armazenando no cache
            self.data_cache = data
            self.last_update = datetime.now()
            
            return data
            
        except Exception as e:
            print(f"Erro ao carregar dados reais: {e}")
            print("Carregando dados simulados como fallback...")
            return self.load_sample_data()
    
    def load_sample_data(self) -> Dict[str, pd.DataFrame]:
        """
        Carrega dados de exemplo para demonstração
        
        Returns:
            Dicionário com DataFrames de exemplo
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
        
        # Dados mensais para análise sazonal
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        matriculas_mensais = [1200, 1350, 1100, 980, 850, 720, 680, 750, 890, 1100, 1250, 1400]
        
        sazonal_data = {
            "Mes": meses,
            "Matriculas": matriculas_mensais,
            "Fator_Sazonal": [1.2, 1.35, 1.1, 0.98, 0.85, 0.72, 0.68, 0.75, 0.89, 1.1, 1.25, 1.4]
        }
        
        # Dados de estados
        estados_data = {
            "Estado": ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Bahia", "Paraná", "Rio Grande do Sul"],
            "Regiao": ["Sudeste", "Sudeste", "Sudeste", "Nordeste", "Sul", "Sul"],
            "Professores": [1800, 1200, 950, 850, 1100, 980],
            "Cursos": [35, 28, 22, 18, 25, 22],
            "Taxa_Conclusao": [91.2, 89.5, 88.7, 87.3, 92.1, 90.8]
        }
        
        # Criando DataFrames
        data = {
            "evolucao": pd.DataFrame(evolucao_data),
            "regioes": pd.DataFrame(regioes_data),
            "programas": pd.DataFrame(programas_data),
            "sazonal": pd.DataFrame(sazonal_data),
            "estados": pd.DataFrame(estados_data)
        }
        
        # Armazenando no cache
        self.data_cache = data
        self.last_update = datetime.now()
        
        return data
    
    def get_data(self, dataset_name: str) -> Optional[pd.DataFrame]:
        """
        Obtém um dataset específico
        
        Args:
            dataset_name: Nome do dataset
            
        Returns:
            DataFrame ou None se não encontrado
        """
        if not self.data_cache:
            self.load_real_data()
        
        return self.data_cache.get(dataset_name)
    
    def get_filtered_data(self, dataset_name: str, 
                         filters: Dict[str, Any]) -> Optional[pd.DataFrame]:
        """
        Obtém dados filtrados
        
        Args:
            dataset_name: Nome do dataset
            filters: Dicionário com filtros
            
        Returns:
            DataFrame filtrado ou None
        """
        df = self.get_data(dataset_name)
        if df is None:
            return None
        
        filtered_df = df.copy()
        
        for column, value in filters.items():
            if column in filtered_df.columns:
                if isinstance(value, (list, tuple)):
                    filtered_df = filtered_df[filtered_df[column].isin(value)]
                elif isinstance(value, dict):
                    if 'min' in value:
                        filtered_df = filtered_df[filtered_df[column] >= value['min']]
                    if 'max' in value:
                        filtered_df = filtered_df[filtered_df[column] <= value['max']]
                else:
                    filtered_df = filtered_df[filtered_df[column] == value]
        
        return filtered_df
    
    def get_summary_statistics(self, dataset_name: str, 
                              group_by: Optional[str] = None) -> Dict[str, Any]:
        """
        Obtém estatísticas resumidas de um dataset
        
        Args:
            dataset_name: Nome do dataset
            group_by: Coluna para agrupamento
            
        Returns:
            Dicionário com estatísticas
        """
        df = self.get_data(dataset_name)
        if df is None:
            return {}
        
        if group_by and group_by in df.columns:
            summary = df.groupby(group_by).agg({
                col: ['count', 'mean', 'std', 'min', 'max'] 
                for col in df.select_dtypes(include=[np.number]).columns
            }).round(2)
        else:
            summary = df.describe().round(2)
        
        return {
            "dataset": dataset_name,
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "summary": summary.to_dict() if hasattr(summary, 'to_dict') else summary,
            "last_update": self.last_update.isoformat() if self.last_update else None
        }
    
    def get_data_info(self) -> Dict[str, Any]:
        """
        Obtém informações sobre todos os datasets disponíveis
        
        Returns:
            Dicionário com informações dos datasets
        """
        if not self.data_cache:
            self.load_sample_data()
        
        info = {}
        for name, df in self.data_cache.items():
            info[name] = {
                "shape": df.shape,
                "columns": list(df.columns),
                "dtypes": df.dtypes.to_dict(),
                "memory_usage": df.memory_usage(deep=True).sum(),
                "null_counts": df.isnull().sum().to_dict()
            }
        
        return info
    
    def export_data(self, dataset_name: str, format: str = "csv", 
                    filename: Optional[str] = None) -> str:
        """
        Exporta dados para arquivo
        
        Args:
            dataset_name: Nome do dataset
            format: Formato de exportação
            filename: Nome do arquivo
            
        Returns:
            Caminho do arquivo exportado
        """
        df = self.get_data(dataset_name)
        if df is None:
            raise ValueError(f"Dataset '{dataset_name}' não encontrado")
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{dataset_name}_{timestamp}"
        
        if format.lower() == "csv":
            filepath = f"{filename}.csv"
            df.to_csv(filepath, index=False)
        elif format.lower() == "excel":
            filepath = f"{filename}.xlsx"
            df.to_excel(filepath, index=False)
        elif format.lower() == "json":
            filepath = f"{filename}.json"
            df.to_json(filepath, orient="records", indent=2)
        else:
            raise ValueError(f"Formato '{format}' não suportado")
        
        return filepath
    
    def create_derived_dataset(self, base_dataset: str, 
                              operations: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Cria dataset derivado com operações aplicadas
        
        Args:
            base_dataset: Nome do dataset base
            operations: Lista de operações a serem aplicadas
            
        Returns:
            DataFrame derivado
        """
        df = self.get_data(base_dataset)
        if df is None:
            raise ValueError(f"Dataset '{base_dataset}' não encontrado")
        
        derived_df = df.copy()
        
        for operation in operations:
            op_type = operation.get("type")
            
            if op_type == "filter":
                column = operation.get("column")
                value = operation.get("value")
                operator = operation.get("operator", "==")
                
                if operator == "==":
                    derived_df = derived_df[derived_df[column] == value]
                elif operator == "!=":
                    derived_df = derived_df[derived_df[column] != value]
                elif operator == ">":
                    derived_df = derived_df[derived_df[column] > value]
                elif operator == "<":
                    derived_df = derived_df[derived_df[column] < value]
                elif operator == ">=":
                    derived_df = derived_df[derived_df[column] >= value]
                elif operator == "<=":
                    derived_df = derived_df[derived_df[column] <= value]
                elif operator == "in":
                    derived_df = derived_df[derived_df[column].isin(value)]
            
            elif op_type == "groupby":
                columns = operation.get("columns", [])
                agg_functions = operation.get("agg_functions", {})
                derived_df = derived_df.groupby(columns).agg(agg_functions).reset_index()
            
            elif op_type == "sort":
                columns = operation.get("columns", [])
                ascending = operation.get("ascending", True)
                derived_df = derived_df.sort_values(columns, ascending=ascending)
            
            elif op_type == "select":
                columns = operation.get("columns", [])
                derived_df = derived_df[columns]
        
        return derived_df
    
    def get_data_quality_report(self, dataset_name: str) -> Dict[str, Any]:
        """
        Gera relatório de qualidade dos dados
        
        Args:
            dataset_name: Nome do dataset
            
        Returns:
            Dicionário com relatório de qualidade
        """
        df = self.get_data(dataset_name)
        if df is None:
            return {}
        
        report = {
            "dataset": dataset_name,
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "missing_percentage": (df.isnull().sum() / len(df) * 100).to_dict(),
            "duplicate_rows": df.duplicated().sum(),
            "data_types": df.dtypes.to_dict(),
            "unique_values": {col: df[col].nunique() for col in df.columns},
            "memory_usage": df.memory_usage(deep=True).sum()
        }
        
        # Estatísticas para colunas numéricas
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            report["numeric_stats"] = {
                col: {
                    "mean": df[col].mean(),
                    "std": df[col].std(),
                    "min": df[col].min(),
                    "max": df[col].max(),
                    "median": df[col].median()
                } for col in numeric_columns
            }
        
        return report
    
    def _process_escolas_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Processa dados das escolas do ES
        
        Args:
            df: DataFrame com dados das escolas
            
        Returns:
            DataFrame processado
        """
        # Criar colunas derivadas
        df_processed = df.copy()
        
        # Mapear códigos de dependência
        dep_mapping = {1: 'Federal', 2: 'Estadual', 3: 'Municipal', 4: 'Privada'}
        df_processed['TP_DEPENDENCIA_NOME'] = df_processed['TP_DEPENDENCIA'].map(dep_mapping)
        
        # Mapear códigos de localização
        loc_mapping = {1: 'Urbana', 2: 'Rural'}
        df_processed['TP_LOCALIZACAO_NOME'] = df_processed['TP_LOCALIZACAO'].map(loc_mapping)
        
        # Calcular total de professores por escola
        prof_cols = [col for col in df.columns if col.startswith('QT_DOC')]
        df_processed['TOTAL_PROFESSORES'] = df_processed[prof_cols].sum(axis=1, skipna=True)
        
        # Calcular total de matrículas por escola
        mat_cols = [col for col in df.columns if col.startswith('QT_MAT')]
        df_processed['TOTAL_MATRICULAS'] = df_processed[mat_cols].sum(axis=1, skipna=True)
        
        # Calcular total de turmas por escola
        tur_cols = [col for col in df.columns if col.startswith('QT_TUR')]
        df_processed['TOTAL_TURMAS'] = df_processed[tur_cols].sum(axis=1, skipna=True)
        
        return df_processed
    
    def _process_cursos_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Processa dados dos cursos técnicos do ES
        
        Args:
            df: DataFrame com dados dos cursos
            
        Returns:
            DataFrame processado
        """
        df_processed = df.copy()
        
        # Calcular total de matrículas por curso
        mat_cols = [col for col in df.columns if col.startswith('QT_MAT')]
        df_processed['TOTAL_MATRICULAS'] = df_processed[mat_cols].sum(axis=1, skipna=True)
        
        # Calcular total de cursos
        curso_cols = [col for col in df.columns if col.startswith('QT_CURSO')]
        df_processed['TOTAL_CURSOS'] = df_processed[curso_cols].sum(axis=1, skipna=True)
        
        return df_processed
    
    def _create_aggregated_data(self, escolas_df: pd.DataFrame, cursos_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """
        Cria dados agregados para visualizações
        
        Args:
            escolas_df: DataFrame das escolas
            cursos_df: DataFrame dos cursos
            
        Returns:
            Dicionário com dados agregados
        """
        # Dados por município
        municipios_data = escolas_df.groupby('NO_MUNICIPIO').agg({
            'TOTAL_PROFESSORES': 'sum',
            'TOTAL_MATRICULAS': 'sum',
            'TOTAL_TURMAS': 'sum',
            'CO_ENTIDADE': 'count'
        }).reset_index()
        municipios_data.columns = ['Municipio', 'Total_Professores', 'Total_Matriculas', 'Total_Turmas', 'Total_Escolas']
        
        # Dados por dependência
        dependencia_data = escolas_df.groupby('TP_DEPENDENCIA_NOME').agg({
            'TOTAL_PROFESSORES': 'sum',
            'TOTAL_MATRICULAS': 'sum',
            'CO_ENTIDADE': 'count'
        }).reset_index()
        dependencia_data.columns = ['Dependencia', 'Total_Professores', 'Total_Matriculas', 'Total_Escolas']
        
        # Dados por localização
        localizacao_data = escolas_df.groupby('TP_LOCALIZACAO_NOME').agg({
            'TOTAL_PROFESSORES': 'sum',
            'TOTAL_MATRICULAS': 'sum',
            'CO_ENTIDADE': 'count'
        }).reset_index()
        localizacao_data.columns = ['Localizacao', 'Total_Professores', 'Total_Matriculas', 'Total_Escolas']
        
        # Dados dos cursos técnicos por município
        cursos_municipio = cursos_df.groupby('NO_MUNICIPIO').agg({
            'TOTAL_MATRICULAS': 'sum',
            'TOTAL_CURSOS': 'sum',
            'NO_CURSO_EDUC_PROFISSIONAL': 'count'
        }).reset_index()
        cursos_municipio.columns = ['Municipio', 'Total_Matriculas', 'Total_Cursos', 'Ofertas_Cursos']
        
        # Top cursos técnicos
        top_cursos = cursos_df['NO_CURSO_EDUC_PROFISSIONAL'].value_counts().head(20).reset_index()
        top_cursos.columns = ['Curso', 'Ofertas']
        
        return {
            "municipios": municipios_data,
            "dependencia": dependencia_data,
            "localizacao": localizacao_data,
            "cursos_municipio": cursos_municipio,
            "top_cursos": top_cursos
        }
